#!/usr/bin/env python3
"""
Download Historical Data for Strategy Testing (Direct Database Approach)

This script directly uses OpenAlgo's services to download historical data
and store it in the DuckDB database, bypassing the HTTP API layer.
"""

import sys
import os

# Add OpenAlgo to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from datetime import datetime, timedelta
import time

# Import OpenAlgo services
from services.historify_service import download_data as service_download_data
from database.auth_db import get_api_key_for_tradingview

# Configuration
USER_ID = "sks20417"  # From database

# Symbols to download
SYMBOLS = [
    {"symbol": "RELIANCE", "exchange": "NSE"},
    {"symbol": "NIFTY", "exchange": "NSE_INDEX"},
    {"symbol": "BANKNIFTY", "exchange": "NSE_INDEX"},
]

# Intervals to download (1m and D are storage intervals)
INTERVALS = ["1m", "D"]

# Date range (last 30 days)
END_DATE = datetime.now().strftime("%Y-%m-%d")
START_DATE = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")


def get_api_key():
    """Get API key for the user."""
    try:
        api_key = get_api_key_for_tradingview(USER_ID)
        if api_key:
            print(f"✅ Retrieved API key for user: {USER_ID}")
            return api_key
        else:
            print(f"❌ No API key found for user: {USER_ID}")
            return None
    except Exception as e:
        print(f"❌ Error getting API key: {e}")
        return None


def download_symbol_data(symbol, exchange, interval, api_key):
    """Download data for a single symbol/interval combination."""
    print(f"\n📥 Downloading {symbol} ({exchange}) - {interval} interval")
    print(f"   Date range: {START_DATE} to {END_DATE}")

    try:
        success, response, status_code = service_download_data(
            symbol=symbol,
            exchange=exchange,
            interval=interval,
            start_date=START_DATE,
            end_date=END_DATE,
            api_key=api_key,
        )

        if success:
            data = response.get("data", {})
            rows = data.get("records", data.get("rows_inserted", 0))
            print(f"   ✅ Success! Inserted {rows} rows")
            return True, rows
        else:
            error = response.get("message", "Unknown error")
            print(f"   ❌ Failed: {error}")
            return False, 0

    except Exception as e:
        print(f"   ❌ Error: {e}")
        import traceback

        traceback.print_exc()
        return False, 0


def verify_data():
    """Verify that data was stored in the database."""
    print("\n🔍 Verifying data in database...")

    try:
        import duckdb

        conn = duckdb.connect("db/historify.duckdb")

        # Get total rows
        total = conn.execute("SELECT COUNT(*) FROM market_data").fetchone()[0]
        print(f"   Total rows in market_data: {total:,}")

        if total == 0:
            print("   ⚠️  No data found in database")
            conn.close()
            return False

        # Get per-symbol counts
        results = conn.execute(
            "SELECT symbol, exchange, interval, COUNT(*) as count, "
            "MIN(timestamp) as first_date, MAX(timestamp) as last_date "
            "FROM market_data GROUP BY symbol, exchange, interval ORDER BY symbol, interval"
        ).fetchall()

        print("\n   Per-symbol breakdown:")
        for row in results:
            symbol, exchange, interval, count, first_date, last_date = row
            print(
                f"   - {symbol:15} ({exchange:10}) {interval:3}: {count:,} rows ({first_date} to {last_date})"
            )

        conn.close()
        return total > 0

    except Exception as e:
        print(f"   ❌ Error verifying data: {e}")
        import traceback

        traceback.print_exc()
        return False


def main():
    print("=" * 70)
    print("OpenAlgo Historical Data Download (Direct Database)")
    print("=" * 70)

    # Get API key
    api_key = get_api_key()
    if not api_key:
        print("\n❌ Cannot proceed without API key.")
        print("   Please ensure user 'sks20417' has an API key generated.")
        sys.exit(1)

    total_success = 0
    total_failed = 0
    total_rows = 0

    # Download data for each symbol and interval
    for symbol_info in SYMBOLS:
        symbol = symbol_info["symbol"]
        exchange = symbol_info["exchange"]

        for interval in INTERVALS:
            success, rows = download_symbol_data(symbol, exchange, interval, api_key)

            if success:
                total_success += 1
                total_rows += rows
            else:
                total_failed += 1

            # Small delay between requests
            time.sleep(2)

    # Summary
    print("\n" + "=" * 70)
    print("Download Summary")
    print("=" * 70)
    print(f"✅ Successful: {total_success}")
    print(f"❌ Failed: {total_failed}")
    print(f"📊 Total rows inserted: {total_rows:,}")

    # Verify data
    if total_rows > 0:
        verify_data()

    print("\n" + "=" * 70)

    if total_failed > 0:
        print("\n⚠️  Some downloads failed. This might be because:")
        print("   1. Broker is not authenticated (login to Dhan Sandbox)")
        print("   2. Market is closed and historical data is not available")
        print("   3. Symbol names need adjustment")
        print("\n   You can check broker auth status in the database:")
        print("   sqlite3 db/openalgo.db 'SELECT * FROM auth;'")

        if total_success == 0:
            sys.exit(1)

    if total_success > 0:
        print("\n✅ Successfully downloaded data for some symbols!")
        print("   Strategies should now be able to fetch historical data.")
        sys.exit(0)


if __name__ == "__main__":
    main()
