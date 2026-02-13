import os
import sys
import json
import logging

sys.path.insert(0, os.getcwd())
# Also add the parent directory to path to find 'broker' if running from scripts/
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test_dhan_connection")

try:
    from dotenv import load_dotenv

    # Load .env from the package root (openalgo/openalgo/.env)
    dotenv_path = os.path.join(parent_dir, ".env")
    load_dotenv(dotenv_path)

    # We need to simulate the environment that the broker module expects
    # The broker module reads BROKER_API_KEY from env
    # And we just need to use the data API provided there.

    from broker.dhan.api.data import BrokerData

    # Extract access token from env for initializing BrokerData
    broker_api_key = os.getenv("BROKER_API_KEY")
    if not broker_api_key:
        print("BROKER_API_KEY not found")
        sys.exit(1)

    client_id, access_token = broker_api_key.split(":::")

    print(f"Initializing BrokerData with Client ID: {client_id}")

    # Initialize BrokerData
    bd = BrokerData(access_token)

    # Try to fetch quotes for a known symbol (e.g. SBIN on NSE)
    print("Fetching quotes for SBIN (NSE)...")
    try:
        quote = bd.get_quotes("SBIN", "NSE")
        print("\n--- Quote Response ---")
        print(json.dumps(quote, indent=2))

        if quote.get("ltp", 0) > 0 or quote.get("prev_close", 0) > 0:
            print("\n✅ SUCCESS: Successfully fetched quote data from Dhan Live!")
        else:
            print(
                "\n⚠️ WARNING: Quote data seems empty or zero. Market might be closed or symbol invalid."
            )

    except Exception as e:
        print(f"\n❌ ERROR fetching quotes: {e}")
        # Print full exception for debugging
        import traceback

        traceback.print_exc()

except ImportError as e:
    print(f"Import Error: {e}")
    print("Ensure you are running this from the project root and all dependencies are installed.")
except Exception as e:
    print(f"Unexpected Error: {e}")
