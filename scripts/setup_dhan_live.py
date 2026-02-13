import os
import sys
import argparse
from sqlalchemy import text

# Add parent directory to path to import from openalgo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from database.auth_db import engine, encrypt_token
except ImportError:
    # Fallback if running from root
    sys.path.insert(0, os.getcwd())
    from database.auth_db import engine, encrypt_token


def update_env_file(client_id):
    """Update BROKER_API_KEY in .env file"""
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")

    if not os.path.exists(env_path):
        print(f"Error: .env file not found at {env_path}")
        return False

    try:
        with open(env_path, "r") as f:
            lines = f.readlines()

        new_lines = []
        key_updated = False

        for line in lines:
            if line.strip().startswith("BROKER_API_KEY ="):
                new_lines.append(f"BROKER_API_KEY = '{client_id}'\n")
                key_updated = True
            elif line.strip().startswith("BROKER_API_KEY="):
                new_lines.append(f"BROKER_API_KEY='{client_id}'\n")
                key_updated = True
            else:
                new_lines.append(line)

        if not key_updated:
            # If not found, append it
            new_lines.append(f"\nBROKER_API_KEY = '{client_id}'\n")

        with open(env_path, "w") as f:
            f.writelines(new_lines)

        print(f"Updated .env with Client ID: {client_id}")
        return True
    except Exception as e:
        print(f"Error updating .env: {e}")
        return False


def update_database(username, client_id, access_token):
    """Update auth table with live credentials"""
    try:
        encrypted_auth = encrypt_token(access_token)

        with engine.connect() as conn:
            print(f"Updating user {username} for LIVE Dhan...")

            # Using raw SQL to ensure direct update
            stmt = text(
                "UPDATE auth SET broker='dhan', auth=:auth, is_revoked=0, feed_token=:feed_token, user_id=:client_id WHERE name=:name"
            )

            result = conn.execute(
                stmt,
                {
                    "name": username,
                    "auth": encrypted_auth,
                    "feed_token": "live_token",
                    "client_id": client_id,
                },
            )
            conn.commit()

            if result.rowcount > 0:
                print(f"Database updated successfully for user {username}")
            else:
                print(f"User {username} not found. Creating new user...")
                # Insert new user
                stmt_insert = text(
                    "INSERT INTO auth (name, broker, auth, is_revoked, feed_token, user_id) VALUES (:name, 'dhan', :auth, 0, :feed_token, :client_id)"
                )
                conn.execute(
                    stmt_insert,
                    {
                        "name": username,
                        "auth": encrypted_auth,
                        "feed_token": "live_token",
                        "client_id": client_id,
                    },
                )
                conn.commit()
                print(f"Created new user {username}")

            return True
    except Exception as e:
        print(f"Error updating database: {e}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Setup Dhan LIVE Credentials")
    parser.add_argument("--client_id", required=True, help="Dhan Client ID")
    parser.add_argument("--access_token", required=True, help="Dhan Access Token (JWT)")
    parser.add_argument("--username", default="sks20417", help="OpenAlgo Username")

    args = parser.parse_args()

    print("--- Setting up Dhan LIVE ---")

    if update_env_file(args.client_id):
        if update_database(args.username, args.client_id, args.access_token):
            print("\nSetup Complete!")
            print("Please restart the OpenAlgo server for .env changes to verify.")
        else:
            print("\nDatabase update failed.")
    else:
        print("\n.env update failed.")
