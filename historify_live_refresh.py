#!/usr/bin/env python3
"""
Continuously refresh historify data for sandbox strategies.

This keeps 1m candles moving so strategies can generate signals outside
market hours when IGNORE_MARKET_HOURS=1.
"""

import os
import sys
import time
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services.historify_service import download_data as service_download_data
from database.auth_db import get_api_key_for_tradingview


USER_ID = os.getenv("OPENALGO_USER_ID", "sks20417")
SYMBOLS = [
    {"symbol": "RELIANCE", "exchange": "NSE"},
    {"symbol": "NIFTY", "exchange": "NSE_INDEX"},
    {"symbol": "BANKNIFTY", "exchange": "NSE_INDEX"},
]
INTERVALS = ["1m"]
SLEEP_SECONDS = int(os.getenv("HISTORIFY_REFRESH_SEC", "60"))
LOOKBACK_DAYS = int(os.getenv("HISTORIFY_LOOKBACK_DAYS", "2"))


def log(msg: str) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def get_api_key() -> str | None:
    try:
        return get_api_key_for_tradingview(USER_ID)
    except Exception as exc:
        log(f"Error getting API key for {USER_ID}: {exc}")
        return None


def download_once(api_key: str) -> int:
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=LOOKBACK_DAYS)).strftime("%Y-%m-%d")
    total_rows = 0

    for sym in SYMBOLS:
        for interval in INTERVALS:
            try:
                success, response, _ = service_download_data(
                    symbol=sym["symbol"],
                    exchange=sym["exchange"],
                    interval=interval,
                    start_date=start_date,
                    end_date=end_date,
                    api_key=api_key,
                )
                if success:
                    data = response.get("data", {})
                    rows = int(data.get("records", data.get("rows_inserted", 0)) or 0)
                    total_rows += rows
                    log(
                        f"Downloaded {rows} rows for {sym['symbol']} {sym['exchange']} {interval}"
                    )
                else:
                    log(
                        f"Download failed for {sym['symbol']} {sym['exchange']} {interval}: "
                        f"{response.get('message', 'unknown error')}"
                    )
            except Exception as exc:
                log(f"Exception downloading {sym['symbol']} {interval}: {exc}")

    return total_rows


def main() -> None:
    log("Historify live refresh started")
    while True:
        api_key = get_api_key()
        if not api_key:
            log("No API key available yet. Retrying in 60s.")
            time.sleep(60)
            continue

        rows = download_once(api_key)
        log(f"Cycle complete. Total rows inserted: {rows}")
        time.sleep(SLEEP_SECONDS)


if __name__ == "__main__":
    main()
