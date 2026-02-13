import os
import sys

# Setup path
sys.path.insert(0, os.getcwd())

from database.auth_db import get_first_available_api_key, ApiKeys, verify_api_key, db_session, Auth
from database.auth_db import decrypt_token


def check_keys():
    try:
        # Check Auth first
        auths = Auth.query.all()
        print(f"Total Auth records: {len(auths)}")
        for a in auths:
            print(f"Auth User: {a.name}, Broker: {a.broker}, Revoked: {a.is_revoked}")
        keys = ApiKeys.query.all()

        print(f"Total keys found: {len(keys)}")
        for k in keys:
            print(f"ID: {k.id}, User: {k.user_id}")
            # Try to decrypt
            try:
                # get_first_available_api_key uses ApiKeys.query.first()
                # But we want to test THIS key.
                if k.api_key_encrypted:
                    raw_key = decrypt_token(k.api_key_encrypted)
                    print(f"  Decrypted: {bool(raw_key)}")  # don't print full key for security
                    if raw_key:
                        # Verify validity
                        is_valid = verify_api_key(raw_key)
                        print(f"  Verification Result (using verify_api_key): {bool(is_valid)}")
                        if is_valid:
                            print(f"  Valid for User: {is_valid}")
                        else:
                            print(f"  INVALID KEY! (Mismatch or expiry)")
                    else:
                        print(f"  Decryption failed (result Empty)")
                else:
                    print(f"  No encrypted key")
            except Exception as e:
                print(f"  Error checking key: {e}")

    finally:
        db_session.remove()


if __name__ == "__main__":
    check_keys()
