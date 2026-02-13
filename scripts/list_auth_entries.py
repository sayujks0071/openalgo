import os
import sys

# Setup path
sys.path.insert(0, os.getcwd())

from database.auth_db import Auth, ApiKeys, db_session


def list_entries():
    try:
        print("\n--- AUTH TABLE ---")
        entries = Auth.query.all()
        print(f"{'ID':<5} | {'Name':<40} | {'Broker':<15} | {'User ID':<20} | {'Is Revoked':<10}")
        print("-" * 100)
        for entry in entries:
            user_id_str = str(entry.user_id) if entry.user_id else "N/A"
            print(
                f"{entry.id:<5} | {entry.name:<40} | {entry.broker:<15} | {user_id_str:<20} | {entry.is_revoked:<10}"
            )

        print("\n--- API KEYS TABLE ---")
        keys = ApiKeys.query.all()
        print(f"{'ID':<5} | {'User ID':<40} | {'Created At':<30}")
        print("-" * 80)
        for k in keys:
            print(f"{k.id:<5} | {k.user_id:<40} | {str(k.created_at):<30}")

    finally:
        db_session.remove()


if __name__ == "__main__":
    list_entries()
