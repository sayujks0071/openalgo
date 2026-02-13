#!/usr/bin/env python3
"""
Strategy Watchdog Service

Monitors scheduled strategy processes every N seconds and enforces:
1. Process health checks during scheduled windows.
2. Risk-breach hard stop (based on strategy log keywords).
3. State repair when config says running but PID is dead.
4. Optional Telegram alerts.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import signal
import sys
import time
from datetime import datetime, time as dt_time
from pathlib import Path
from typing import Any

import requests
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")
BASE_DIR = Path(__file__).resolve().parents[1]
CONFIG_PATH = BASE_DIR / "strategies" / "strategy_configs.json"
WATCHDOG_LOG_PATH = BASE_DIR / "logs" / "strategy_watchdog.log"
WATCHDOG_STATE_PATH = BASE_DIR / "logs" / "strategy_watchdog_state.json"
PID_FILE = BASE_DIR / "logs" / "strategy_watchdog.pid"
STRATEGY_LOG_DIR = BASE_DIR / "log" / "strategies"

BREACH_KEYWORDS = (
    "CIRCUIT BREAKER",
    "Max daily loss",
    "consecutive losses",
    "Trading halted",
)

logger = logging.getLogger("strategy_watchdog")


def setup_logging() -> None:
    WATCHDOG_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [WATCHDOG] %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(WATCHDOG_LOG_PATH, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def now_ist() -> datetime:
    return datetime.now(IST)


def now_ist_iso() -> str:
    return now_ist().isoformat()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def write_json_atomic(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(path)


def is_pid_running(pid: int | None) -> bool:
    if not pid:
        return False
    try:
        os.kill(int(pid), 0)
        return True
    except Exception:
        return False


def terminate_pid(pid: int, grace_seconds: float = 5.0) -> bool:
    if not is_pid_running(pid):
        return True
    try:
        os.kill(pid, signal.SIGTERM)
    except Exception:
        return False

    deadline = time.time() + grace_seconds
    while time.time() < deadline:
        if not is_pid_running(pid):
            return True
        time.sleep(0.2)

    try:
        os.kill(pid, signal.SIGKILL)
        return not is_pid_running(pid)
    except Exception:
        return False


def parse_hhmm(value: str | None, fallback: dt_time) -> dt_time:
    if not value:
        return fallback
    try:
        hh, mm = value.split(":")
        return dt_time(hour=int(hh), minute=int(mm))
    except Exception:
        return fallback


def should_run_now(cfg: dict[str, Any], current: datetime) -> bool:
    if not cfg.get("is_scheduled"):
        return False
    if cfg.get("manually_stopped"):
        return False

    day_key = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"][current.weekday()]
    days = cfg.get("schedule_days") or ["mon", "tue", "wed", "thu", "fri"]
    days = [str(d).lower() for d in days]
    if day_key not in days:
        return False

    start_t = parse_hhmm(cfg.get("schedule_start"), dt_time(9, 15))
    stop_t = parse_hhmm(cfg.get("schedule_stop"), dt_time(15, 30))
    return start_t <= current.time() <= stop_t


def tail_text(path: Path, max_bytes: int = 65536) -> str:
    try:
        with path.open("rb") as fh:
            fh.seek(0, os.SEEK_END)
            size = fh.tell()
            fh.seek(max(0, size - max_bytes), os.SEEK_SET)
            data = fh.read()
        return data.decode("utf-8", errors="ignore")
    except Exception:
        return ""


def latest_log_for_strategy(strategy_id: str) -> Path | None:
    candidates = list(STRATEGY_LOG_DIR.glob(f"{strategy_id}_*_IST.log"))
    if not candidates:
        return None
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0]


def log_shows_breach(strategy_id: str) -> tuple[bool, str]:
    log_path = latest_log_for_strategy(strategy_id)
    if not log_path:
        return False, ""
    text = tail_text(log_path)
    for keyword in BREACH_KEYWORDS:
        if keyword.lower() in text.lower():
            return True, keyword
    return False, ""


def load_state() -> dict[str, Any]:
    return load_json(WATCHDOG_STATE_PATH, default={"alerts": {}})


def save_state(state: dict[str, Any]) -> None:
    write_json_atomic(WATCHDOG_STATE_PATH, state)


def emit_alert(state: dict[str, Any], dedupe_key: str, message: str, min_interval_sec: int = 300) -> None:
    now_ts = time.time()
    last_ts = float(state.get("alerts", {}).get(dedupe_key, 0))
    if now_ts - last_ts < min_interval_sec:
        return
    state.setdefault("alerts", {})[dedupe_key] = now_ts
    save_state(state)

    logger.warning(message)
    token = os.getenv("WATCHDOG_TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("WATCHDOG_TELEGRAM_CHAT_ID", "").strip()
    if token and chat_id:
        try:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            requests.post(url, json={"chat_id": chat_id, "text": message}, timeout=10)
        except Exception as exc:
            logger.error(f"Failed to send Telegram alert: {exc}")


def enforce_cycle() -> None:
    config = load_json(CONFIG_PATH, default={})
    if not isinstance(config, dict):
        logger.error("Invalid strategy config format")
        return

    state = load_state()
    current = now_ist()
    dirty = False

    for strategy_id, cfg in config.items():
        if not isinstance(cfg, dict):
            continue
        if not cfg.get("is_scheduled"):
            continue

        pid = cfg.get("pid")
        pid_int = int(pid) if isinstance(pid, int) or (isinstance(pid, str) and pid.isdigit()) else None
        running = is_pid_running(pid_int)
        should_run = should_run_now(cfg, current)

        # Kill immediately if strategy was manually stopped but process is still alive.
        if cfg.get("manually_stopped") and running:
            if terminate_pid(pid_int):
                cfg["is_running"] = False
                cfg["pid"] = None
                cfg["last_stopped"] = now_ist_iso()
                dirty = True
                emit_alert(
                    state,
                    f"{strategy_id}:manual_stopped_running",
                    f"[WATCHDOG] Stopped {strategy_id}: manually_stopped=true but PID {pid_int} was alive.",
                )
            continue

        # Risk breach check from latest strategy log.
        if running:
            breach, keyword = log_shows_breach(strategy_id)
            if breach:
                stopped = terminate_pid(pid_int)
                cfg["is_running"] = False
                cfg["pid"] = None
                cfg["manually_stopped"] = True
                cfg["paused_reason"] = "risk_breach"
                cfg["paused_message"] = f"Watchdog stopped after breach keyword: {keyword}"
                cfg["last_stopped"] = now_ist_iso()
                dirty = True
                emit_alert(
                    state,
                    f"{strategy_id}:risk_breach",
                    (
                        f"[WATCHDOG] Risk breach for {strategy_id} (keyword='{keyword}'). "
                        f"PID {pid_int} {'stopped' if stopped else 'stop_failed'}."
                    ),
                    min_interval_sec=60,
                )
                continue

        # Repair stale running state.
        if cfg.get("is_running") and not running:
            cfg["is_running"] = False
            cfg["pid"] = None
            cfg["last_stopped"] = now_ist_iso()
            dirty = True
            emit_alert(
                state,
                f"{strategy_id}:dead_pid",
                f"[WATCHDOG] {strategy_id} marked running but PID {pid_int} is dead.",
            )

        # Enforce schedule window strictly for safety.
        if running and not should_run:
            stopped = terminate_pid(pid_int)
            cfg["is_running"] = False
            cfg["pid"] = None
            cfg["last_stopped"] = now_ist_iso()
            dirty = True
            emit_alert(
                state,
                f"{strategy_id}:outside_window",
                (
                    f"[WATCHDOG] {strategy_id} running outside schedule; "
                    f"PID {pid_int} {'stopped' if stopped else 'stop_failed'}."
                ),
            )

        # During active schedule window, alert if process is missing.
        if should_run and not running:
            emit_alert(
                state,
                f"{strategy_id}:missing_during_window",
                f"[WATCHDOG] {strategy_id} should be running now but no live PID.",
                min_interval_sec=180,
            )

    if dirty:
        write_json_atomic(CONFIG_PATH, config)


def acquire_pid_file() -> bool:
    PID_FILE.parent.mkdir(parents=True, exist_ok=True)
    existing = load_json(PID_FILE, default={})
    existing_pid = existing.get("pid") if isinstance(existing, dict) else None
    if isinstance(existing_pid, int) and is_pid_running(existing_pid):
        return False
    write_json_atomic(PID_FILE, {"pid": os.getpid(), "started_at": now_ist_iso()})
    return True


def release_pid_file() -> None:
    try:
        if PID_FILE.exists():
            data = load_json(PID_FILE, default={})
            if isinstance(data, dict) and data.get("pid") == os.getpid():
                PID_FILE.unlink(missing_ok=True)
    except Exception:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(description="Strategy watchdog process monitor")
    parser.add_argument("--interval", type=int, default=60, help="Watchdog cycle interval in seconds")
    parser.add_argument("--once", action="store_true", help="Run one cycle and exit")
    args = parser.parse_args()

    setup_logging()
    if not acquire_pid_file():
        logger.info("Watchdog already running; exiting duplicate process.")
        return 0

    logger.info("Strategy watchdog started")
    logger.info(f"Using config: {CONFIG_PATH}")
    logger.info(f"Using strategy logs: {STRATEGY_LOG_DIR}")

    try:
        if args.once:
            enforce_cycle()
            return 0

        while True:
            try:
                enforce_cycle()
            except Exception as exc:
                logger.error(f"Watchdog cycle error: {exc}")
            time.sleep(max(5, args.interval))
    finally:
        release_pid_file()


if __name__ == "__main__":
    raise SystemExit(main())
