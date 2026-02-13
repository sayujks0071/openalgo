import os
import sys

# Setup path
sys.path.insert(0, os.getcwd())

from database.auth_db import get_first_available_api_key, ApiKeys, verify_api_key, db_session, Auth
from database.auth_db import decrypt_token


def reveal_keys():
    try:
        keys = ApiKeys.query.all()
        for k in keys:
            if k.api_key_encrypted:
                raw_key = decrypt_token(k.api_key_encrypted)
                if raw_key:
                    print(f"API_KEY: {raw_key}")
                    return  # Just need one
    finally:
        db_session.remove()


if __name__ == "__main__":
    reveal_keys()
