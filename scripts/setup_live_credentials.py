import os
import sys
from sqlalchemy import text
from dotenv import load_dotenv

# Setup path
sys.path.insert(0, os.getcwd())

from database.auth_db import engine, encrypt_token


def setup_live_credentials(username="sks20417"):
    load_dotenv()

    api_key = os.getenv("BROKER_API_KEY")
    client_id = os.getenv(
        "BROKER_API_SECRET"
    )  # Dhan uses Client ID as secret in some contexts, or vice versa.
    # Actually, usually BROKER_API_KEY is the Access Token for Dhan in this repo's context (based on previous .env)
    # And BROKER_API_SECRET is the Client ID.

    if not api_key or not client_id:
        print("Error: BROKER_API_KEY or BROKER_API_SECRET not found in .env")
        return

    # Check if key is valid/present
    if ":::" in api_key:
        # It might be in format CLIENT_ID:::TOKEN
        parts = api_key.split(":::")
        if len(parts) == 2:
            token = parts[1]
        else:
            token = api_key
    else:
        token = api_key

    if len(token) < 50:
        print(f"Warning: Token seems too short ({len(token)} chars). Please check BROKER_API_KEY.")

    encrypted_auth = encrypt_token(token)
    print(f"Encrypted Auth generated.")

    with engine.connect() as conn:
        print(f"Updating user {username} to LIVE mode...")
        # Update to use 'dhan' (Live) instead of 'dhan_sandbox'
        # Set is_revoked to False
        stmt = text(
            "UPDATE auth SET broker='dhan', auth=:auth, is_revoked=0, feed_token=:feed_token WHERE name=:name"
        )

        # feed_token is often same as auth or distinct. For Dhan, we might just use the same token or a placeholder if handled by the broker class.
        # process_dhan.py usually handles login.
        # But here we are forcefully setting it.
        # Let's set feed_token same as auth token for now, or empty if it auto-generates.
        # The login_user.py used "sandbox_feed_token".

        result = conn.execute(
            stmt,
            {
                "name": username,
                "auth": encrypted_auth,
                "feed_token": token,  # Usually needed for websocket
            },
        )
        conn.commit()
        print(f"Rows updated: {result.rowcount}")

        # Verify
        result = conn.execute(
            text("SELECT name, broker, is_revoked FROM auth WHERE name=:name"),
            {"name": username},
        )
        row = result.fetchone()
        print(f"Verification: {row}")


if __name__ == "__main__":
    setup_live_credentials()
