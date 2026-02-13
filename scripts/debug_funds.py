import os
import sys
import json

# Setup path
sys.path.insert(0, os.getcwd())

from dotenv import load_dotenv

load_dotenv()


# Mock logger
class Logger:
    def info(self, msg):
        print(f"INFO: {msg}")

    def error(self, msg):
        print(f"ERROR: {msg}")


import broker.dhan.api.funds

broker.dhan.api.funds.logger = Logger()

from broker.dhan.api.funds import get_margin_data
from database.auth_db import get_auth_token_dbquery


def debug():
    username = "sks20417"
    print(f"getting token for {username}")
    auth_obj = get_auth_token_dbquery(username)

    if not auth_obj:
        print("User not found")
        return

    token = auth_obj.auth
    # Decrypt if needed (but auth_db usually returns object with encrypted/decrypted?
    # Wait, auth_obj.auth is ENCRYPTED in DB object.
    # We need to use get_auth_token(username) which decrypts it.

    from database.auth_db import get_auth_token

    token = get_auth_token(username)

    print(f"Token: {token[:10]}...")

    print("Calling get_margin_data...")
    data = get_margin_data(token)
    print("Result:")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    debug()
