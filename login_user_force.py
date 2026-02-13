import os
import sys
from sqlalchemy import text

# Setup path
sys.path.insert(0, os.getcwd())

from database.auth_db import engine, encrypt_token


def force_login(username="sks20417"):
    # Real Dhan Sandbox Token
    token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJwYXJ0bmVySWQiOiIiLCJkaGFuQ2xpZW50SWQiOiIyNTA4MDQxMjA2Iiwid2ViaG9va1VybCI6IiIsImlzcyI6ImRoYW4iLCJleHAiOjE3NzI1NTk0MTN9.U05-7OiHvhNzxjoouJLmcxCi2Jybz0fzXTX1IvJhI4slZ3mVf_53JZGjTU5pQfFPmG2pTg8IfimU5ztIGj1nUw"
    encrypted_auth = encrypt_token(token)
    print(f"Encrypted Auth: {encrypted_auth}")
    with engine.connect() as conn:
        print(f"Updating user {username} via RAW SQL...")
        stmt = text(
            "UPDATE auth SET broker='dhan_sandbox', auth=:auth, is_revoked=0, feed_token='sandbox_feed_token' WHERE name=:name"
        )
        result = conn.execute(stmt, {"name": username, "auth": encrypted_auth})
        conn.commit()
        print(f"Rows matched/updated: {result.rowcount}")

        # Verify
        result = conn.execute(
            text("SELECT name, broker, is_revoked, auth FROM auth WHERE name=:name"),
            {"name": username},
        )
        row = result.fetchone()
        print(f"VERIFICATION (Raw SQL): {row}")


if __name__ == "__main__":
    force_login()
