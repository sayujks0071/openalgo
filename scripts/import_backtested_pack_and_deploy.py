#!/usr/bin/env python3
"""
Import + backtest + deploy a curated live strategy pack for OpenAlgo.

What this script does:
1. Loads advanced strategy scripts that expose generate_signal()
2. Downloads recent historical data from local OpenAlgo API (live broker-backed)
3. Runs a lightweight signal backtest for each strategy
4. Selects top strategies by score + risk gates
5. Rewrites strategies/strategy_configs.json for scheduled live deployment
6. Saves a JSON report for audit

Usage:
  ./.venv/bin/python scripts/import_backtested_pack_and_deploy.py --count 10
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import logging
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import pandas as pd
import pytz
from openalgo import api as openalgo_api

IST = pytz.timezone("Asia/Kolkata")
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from database.auth_db import get_api_key_for_tradingview

SCRIPTS_DIR = BASE_DIR / "strategies" / "scripts"
CONFIG_PATH = BASE_DIR / "strategies" / "strategy_configs.json"
REPORT_PATH = BASE_DIR / "logs" / "strategy_pack_deploy_report.json"

# Silence noisy per-call strategy loggers during backtest loop.
logging.disable(logging.CRITICAL)

# Strategy archetype sources (internet references used for this pack design)
STRATEGY_SOURCES: Dict[str, str] = {
    "vwap_volume_breakout": "https://www.investopedia.com/terms/v/vwap.asp",
    "keltner_adx_trend": "https://www.investopedia.com/terms/k/keltnerchannel.asp",
    "psar_rsi_scalp": "https://www.investopedia.com/terms/p/parabolicindicator.asp",
    "donchian_breakout": "https://www.investopedia.com/terms/d/donchianchannels.asp",
    "stochastic_macd_momentum": "https://www.investopedia.com/terms/s/stochasticoscillator.asp",
    "mean_reversion_pro": "https://www.investopedia.com/terms/m/meanreversion.asp",
    "rsi_mean_reversion": "https://www.investopedia.com/terms/r/rsi.asp",
    "triple_confirmation": "https://www.investopedia.com/terms/m/macd.asp",
    "turtle_breakout": "https://www.investopedia.com/articles/trading/08/turtle-trading.asp",
    "ichimoku_cloud_trend": "https://www.investopedia.com/terms/i/ichimoku-cloud.asp",
    "faber_trend_following": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461",
    "time_series_momentum": "https://www.sciencedirect.com/science/article/pii/S0304405X11002613",
    "rsi2_pullback": "https://chartschool.stockcharts.com/table-of-contents/trading-strategies-and-models/trading-strategies/rsi-2",
    "bollinger_mean_reversion": "https://www.quantifiedstrategies.com/bollinger-bands-trading-strategy/",
    "dual_momentum_proxy": "https://www.quantifiedstrategies.com/dual-momentum-trading-strategy/",
}


@dataclass
class StrategySpec:
    strategy_id: str
    file_name: str
    symbol: str
    exchange: str
    interval: str


def now_ist_iso() -> str:
    return datetime.now(IST).isoformat()


def load_module_from_path(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, str(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def parse_signal(output: Any) -> str:
    if isinstance(output, tuple) and output:
        return str(output[0]).upper()
    if isinstance(output, dict):
        for key in ("signal", "action", "side"):
            if key in output:
                return str(output[key]).upper()
    if isinstance(output, str):
        return output.upper()
    return "HOLD"


def choose_specs() -> List[StrategySpec]:
    # Curated strategy universe with backtest-capable scripts (generate_signal).
    return [
        StrategySpec("vwap_volume_breakout", "vwap_volume_breakout.py", "INFY", "NSE", "5m"),
        StrategySpec("keltner_adx_trend", "keltner_adx_trend.py", "TCS", "NSE", "15m"),
        StrategySpec("psar_rsi_scalp", "psar_rsi_scalp.py", "HDFCBANK", "NSE", "5m"),
        StrategySpec("donchian_breakout", "donchian_breakout.py", "SBIN", "NSE", "15m"),
        StrategySpec(
            "stochastic_macd_momentum", "stochastic_macd_momentum.py", "NIFTY", "NSE_INDEX", "15m"
        ),
        StrategySpec("mean_reversion_pro", "mean_reversion_pro.py", "RELIANCE", "NSE", "15m"),
        StrategySpec("rsi_mean_reversion", "rsi_mean_reversion.py", "RELIANCE", "NSE", "15m"),
        StrategySpec("triple_confirmation", "triple_confirmation.py", "RELIANCE", "NSE", "15m"),
        StrategySpec("turtle_breakout", "turtle_breakout.py", "NIFTY", "NSE_INDEX", "1h"),
        StrategySpec(
            "ichimoku_cloud_trend", "ichimoku_cloud_trend.py", "BANKNIFTY", "NSE_INDEX", "1h"
        ),
        StrategySpec("faber_trend_following", "faber_trend_following.py", "NIFTY", "NSE_INDEX", "1h"),
        StrategySpec("time_series_momentum", "time_series_momentum.py", "BANKNIFTY", "NSE_INDEX", "1h"),
        StrategySpec("rsi2_pullback", "rsi2_pullback.py", "HDFCBANK", "NSE", "15m"),
        StrategySpec("bollinger_mean_reversion", "bollinger_mean_reversion.py", "INFY", "NSE", "15m"),
        StrategySpec("dual_momentum_proxy", "dual_momentum_proxy.py", "RELIANCE", "NSE", "1h"),
    ]


def fetch_history(client, symbol: str, exchange: str, interval: str, days: int) -> pd.DataFrame:
    end_date = datetime.now(IST).date()
    start_date = end_date - timedelta(days=days)
    df = client.history(
        symbol=symbol,
        exchange=exchange,
        interval=interval,
        start_date=start_date.strftime("%Y-%m-%d"),
        end_date=end_date.strftime("%Y-%m-%d"),
    )
    if not isinstance(df, pd.DataFrame):
        df = pd.DataFrame(df)
    if df.empty:
        return df
    if "timestamp" not in df.columns:
        # openalgo client sometimes returns timestamp in index
        df = df.reset_index()
    sort_col = "timestamp" if "timestamp" in df.columns else df.columns[0]
    df = df.sort_values(sort_col).reset_index(drop=True)
    return df


def max_drawdown(equity_curve: List[float]) -> float:
    if not equity_curve:
        return 0.0
    eq = np.array(equity_curve, dtype=float)
    peaks = np.maximum.accumulate(eq)
    dd = (peaks - eq) / np.where(peaks == 0, 1.0, peaks)
    return float(np.max(dd))


def backtest_strategy(mod, df: pd.DataFrame, symbol: str) -> Dict[str, Any]:
    # Keep bars bounded for speed; warmup still enough for indicators.
    max_bars = 320 if len(df) > 320 else len(df)
    df = df.iloc[-max_bars:].copy()
    if len(df) < 150:
        return {
            "status": "error",
            "error": "insufficient_data",
            "bars": len(df),
        }

    warmup = min(120, max(50, len(df) // 10))

    pos = 0  # -1 short, 0 flat, 1 long
    entry = 0.0
    closed_rets: List[float] = []
    equity = 1.0
    equity_curve: List[float] = []

    step = max(1, len(df) // 180)
    for i in range(warmup, len(df), step):
        view = df.iloc[: i + 1].copy()
        try:
            out = mod.generate_signal(view, symbol=symbol)
            sig = parse_signal(out)
        except Exception:
            sig = "HOLD"

        price = float(view.iloc[-1]["close"])
        if price <= 0:
            equity_curve.append(equity)
            continue

        # close/reverse logic
        if pos == 1 and sig == "SELL":
            r = (price - entry) / entry
            closed_rets.append(r)
            equity *= 1.0 + r
            pos = -1
            entry = price
        elif pos == -1 and sig == "BUY":
            r = (entry - price) / entry
            closed_rets.append(r)
            equity *= 1.0 + r
            pos = 1
            entry = price
        elif pos == 0:
            if sig == "BUY":
                pos = 1
                entry = price
            elif sig == "SELL":
                pos = -1
                entry = price

        mtm_equity = equity
        if pos == 1 and entry > 0:
            mtm_equity = equity * (1.0 + (price - entry) / entry)
        elif pos == -1 and entry > 0:
            mtm_equity = equity * (1.0 + (entry - price) / entry)
        equity_curve.append(mtm_equity)

    # close at last bar
    if pos != 0 and len(df) > 0:
        last = float(df.iloc[-1]["close"])
        if entry > 0:
            r = (last - entry) / entry if pos == 1 else (entry - last) / entry
            closed_rets.append(r)
            equity *= 1.0 + r

    trades = len(closed_rets)
    wins = sum(1 for x in closed_rets if x > 0)
    win_rate = float(wins / trades) if trades else 0.0
    total_return = float(equity - 1.0)
    mdd = max_drawdown(equity_curve)
    avg_ret = float(np.mean(closed_rets)) if trades else 0.0
    std_ret = float(np.std(closed_rets)) if trades else 0.0
    sharpe_like = (avg_ret / std_ret * np.sqrt(trades)) if std_ret > 0 else 0.0

    pass_gates = trades >= 4 and total_return > 0 and mdd <= 0.40 and win_rate >= 0.30
    score = (total_return * 100.0) + (win_rate * 25.0) + (sharpe_like * 4.0) - (mdd * 80.0)

    return {
        "status": "ok",
        "bars": len(df),
        "trades": trades,
        "wins": wins,
        "win_rate": round(win_rate, 4),
        "total_return": round(total_return, 4),
        "max_drawdown": round(mdd, 4),
        "sharpe_like": round(sharpe_like, 4),
        "score": round(score, 4),
        "pass_gates": pass_gates,
    }


def deploy_configs(
    selected: List[StrategySpec],
    user_id: str,
    risk_env: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    if CONFIG_PATH.exists():
        config_data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    else:
        config_data = {}

    selected_ids = {s.strategy_id for s in selected}
    now = now_ist_iso()

    # Disable all existing user-owned configs by default.
    for sid, cfg in list(config_data.items()):
        if cfg.get("user_id") == user_id:
            cfg["is_scheduled"] = False
            cfg["is_running"] = False
            cfg["pid"] = None

    # Upsert selected pack.
    for spec in selected:
        cfg = config_data.get(spec.strategy_id, {})
        cfg.update(
            {
                "name": spec.strategy_id.replace("_", " "),
                "file_path": f"strategies/scripts/{spec.file_name}",
                "file_name": spec.file_name,
                "symbol": spec.symbol,
                "exchange": spec.exchange,
                "interval": spec.interval,
                "script_args": ["--symbol", spec.symbol, "--port", "5000"],
                "env": risk_env or {},
                "is_running": False,
                "is_scheduled": True,
                "created_at": cfg.get("created_at", now),
                "user_id": user_id,
                "schedule_start": "09:15",
                "schedule_stop": "15:30",
                "schedule_days": ["mon", "tue", "wed", "thu", "fri"],
                "pid": None,
                "manually_stopped": False,
            }
        )
        # Keep history if already present
        if "last_started" in cfg and cfg["last_started"] is None:
            cfg.pop("last_started", None)
        config_data[spec.strategy_id] = cfg

    CONFIG_PATH.write_text(json.dumps(config_data, indent=2, ensure_ascii=False), encoding="utf-8")
    return config_data


def main() -> int:
    parser = argparse.ArgumentParser(description="Import + backtest + deploy live strategy pack")
    parser.add_argument("--count", type=int, default=10, help="Number of strategies to deploy")
    parser.add_argument("--user", type=str, default="sks20417", help="OpenAlgo username")
    parser.add_argument("--host", type=str, default="http://127.0.0.1:5000", help="OpenAlgo host")
    parser.add_argument(
        "--days", type=int, default=90, help="Backtest lookback days for history fetch"
    )
    parser.add_argument(
        "--selection-mode",
        type=str,
        choices=["strict", "score"],
        default="strict",
        help="strict=pass gates first, score=top-ranked candidates with min trade filter",
    )
    parser.add_argument(
        "--min-trades",
        type=int,
        default=1,
        help="Minimum trade count required in score mode",
    )
    parser.add_argument(
        "--max-daily-loss-abs",
        type=float,
        default=2500.0,
        help="Per-strategy daily loss circuit breaker in INR",
    )
    parser.add_argument(
        "--max-consec-losses",
        type=int,
        default=2,
        help="Per-strategy consecutive losing exits before stop",
    )
    parser.add_argument(
        "--max-position-qty",
        type=int,
        default=1,
        help="Per-strategy max net position quantity",
    )
    parser.add_argument("--dry-run", action="store_true", help="Do not write strategy configs")
    args = parser.parse_args()

    api_key = get_api_key_for_tradingview(args.user)
    if not api_key:
        raise SystemExit(f"No API key found for user {args.user}")

    # Avoid strategy import failures for local backtest path.
    import os

    os.environ.setdefault("OPENALGO_APIKEY", "dummy")

    client = openalgo_api(api_key=api_key, host=args.host)
    specs = choose_specs()

    # Fetch data per unique symbol/exchange/interval once.
    data_cache: Dict[Tuple[str, str, str], pd.DataFrame] = {}
    for s in specs:
        key = (s.symbol, s.exchange, s.interval)
        if key not in data_cache:
            data_cache[key] = fetch_history(client, s.symbol, s.exchange, s.interval, args.days)

    results: List[Dict[str, Any]] = []
    for s in specs:
        path = SCRIPTS_DIR / s.file_name
        if not path.exists():
            results.append(
                {"strategy_id": s.strategy_id, "status": "error", "error": f"missing_file:{path}"}
            )
            continue
        try:
            mod = load_module_from_path(path)
            if not hasattr(mod, "generate_signal"):
                results.append(
                    {
                        "strategy_id": s.strategy_id,
                        "status": "error",
                        "error": "missing_generate_signal",
                    }
                )
                continue
            df = data_cache[(s.symbol, s.exchange, s.interval)]
            bt = backtest_strategy(mod, df, s.symbol)
            bt.update(
                {
                    "strategy_id": s.strategy_id,
                    "symbol": s.symbol,
                    "exchange": s.exchange,
                    "interval": s.interval,
                    "source_url": STRATEGY_SOURCES.get(s.strategy_id, ""),
                }
            )
            results.append(bt)
        except Exception as exc:
            results.append({"strategy_id": s.strategy_id, "status": "error", "error": str(exc)})

    ok_results = [r for r in results if r.get("status") == "ok"]
    gated = [r for r in ok_results if r.get("pass_gates")]
    if args.selection_mode == "strict":
        pool = gated if gated else ok_results
    else:
        pool = [r for r in ok_results if int(r.get("trades", 0)) >= max(0, args.min_trades)]
        if not pool:
            pool = ok_results

    ranked = sorted(pool, key=lambda x: x.get("score", -1e9), reverse=True)
    top = ranked[: max(1, min(args.count, len(ranked)))]
    selected_ids = {r["strategy_id"] for r in top}
    selected_specs = [s for s in specs if s.strategy_id in selected_ids]

    risk_env = {
        "OA_GUARDRAILS": "1",
        "OA_MAX_CONSEC_LOSSES": str(args.max_consec_losses),
        "OA_MAX_DAILY_LOSS_ABS": str(args.max_daily_loss_abs),
        "OA_MAX_POSITION_QTY": str(args.max_position_qty),
        "OA_EXIT_ON_BREACH": "1",
    }

    if not args.dry_run:
        deploy_configs(selected_specs, args.user, risk_env=risk_env)

    summary = {
        "generated_at_ist": now_ist_iso(),
        "user": args.user,
        "host": args.host,
        "history_lookback_days": args.days,
        "dry_run": args.dry_run,
        "requested_count": args.count,
        "selection_mode": args.selection_mode,
        "min_trades_filter": args.min_trades,
        "selected_count": len(selected_specs),
        "selected_strategy_ids": [s.strategy_id for s in selected_specs],
        "risk_env": risk_env,
        "results": results,
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
