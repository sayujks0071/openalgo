import os
from datetime import datetime, timedelta
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load env
load_dotenv(Path(__file__).resolve().parent / ".env", override=False)

HOST = os.getenv("HOST_SERVER", os.getenv("OPENALGO_HOST", "http://127.0.0.1:5000"))

API_KEY = os.getenv("OPENALGO_APIKEY") or os.getenv("OPENALGO_API_KEY")
if not API_KEY:
    try:
        from database.auth_db import get_first_available_api_key

        API_KEY = get_first_available_api_key()
    except Exception:
        API_KEY = None

if not API_KEY:
    raise SystemExit(
        "OPENALGO_APIKEY/OPENALGO_API_KEY not set and no API key found in DB. "
        "Run openalgo/scripts/regenerate_openalgo_api_key.py or create a key in the UI."
    )


def check_history(symbol, exchange="NSE"):
    print(f"\n🔍 Checking {symbol} ({exchange})...")
    url = f"{HOST}/api/v1/history"

    start_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    end_date = datetime.now().strftime("%Y-%m-%d")

    payload = {
        "apikey": API_KEY,
        "symbol": symbol,
        "exchange": exchange,
        "interval": "15m",
        "start_date": start_date,
        "end_date": end_date,
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        data = response.json()

        if data.get("status") == "success":
            candles = data.get("data", [])
            print(f"✅ Fetched {len(candles)} candles.")
            if candles:
                last_candle = candles[-1]
                print(f"🕒 Last Candle: {last_candle}")

                # Check for today's data (simple string check)
                today_str = datetime.now().strftime("%Y-%m-%d")
                today_count = sum(1 for c in candles if today_str in str(c.get("datetime", "")))
                if today_count > 0:
                    print(f"✅ Found {today_count} candles for TODAY ({today_str})")
                else:
                    print(f"⚠️  NO candles found for TODAY ({today_str}) in the response.")
        else:
            print(f"❌ API Error: {data}")

    except Exception as e:
        print(f"❌ Request Failed: {e}")


if __name__ == "__main__":
    check_history("RELIANCE")
    check_history("NIFTY", "NSE_INDEX")
    check_history("BANKNIFTY", "NSE_INDEX")
