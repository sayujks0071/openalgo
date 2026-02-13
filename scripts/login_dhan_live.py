import os
import sys

# Setup path to include project root (openalgo/openalgo)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from database.auth_db import upsert_auth, db_session


def login_dhan_live(username="sks20417"):
    try:
        # Get API Key from environment
        from dotenv import load_dotenv

        load_dotenv()

        broker_api_key = os.getenv("BROKER_API_KEY")
        if not broker_api_key:
            print("Error: BROKER_API_KEY not found in environment variables.")
            return

        print(f"Read BROKER_API_KEY from env: {broker_api_key[:15]}...")

        if ":::" in broker_api_key:
            client_id, access_token = broker_api_key.split(":::")
        else:
            print("Error: BROKER_API_KEY format incorrect. Expected CLIENT_ID:::ACCESS_TOKEN")
            return

        print(f"Found user {username}. Updating for Live Dhan using upsert_auth...")

        # upsert_auth handles encryption and cache invalidation
        # It takes: name, auth_token, broker, feed_token, user_id, revoke
        upsert_auth(
            name=username,
            auth_token=access_token,
            broker="dhan",
            feed_token=access_token,
            user_id=client_id,
            revoke=False,
        )
        print("User logged in to Dhan Live (DB updated with ENCRYPTED token).")

    except Exception as e:
        print(f"Error logging in: {e}")
        import traceback

        traceback.print_exc()
    finally:
        db_session.remove()


if __name__ == "__main__":
    login_dhan_live()
