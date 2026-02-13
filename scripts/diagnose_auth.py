import os
import sys

# Setup path
sys.path.insert(0, os.getcwd())

from dotenv import load_dotenv

load_dotenv()


def diagnose():
    print("Diagnosing Auto-Login Logic...")

    username = "sks20417"
    print(f"Checking user: {username}")

    try:
        from database.auth_db import get_auth_token_dbquery

        auth_obj = get_auth_token_dbquery(username)

        if not auth_obj:
            print("❌ auth_obj is None. User not found in Auth table.")
            return

        print(f"✅ Auth Object Found: ID={auth_obj.id}")
        print(f"   Broker: {auth_obj.broker}")
        print(f"   Is Revoked: {auth_obj.is_revoked}")
        print(f"   Auth Token Present: {bool(auth_obj.auth)}")

        if auth_obj and auth_obj.broker and not auth_obj.is_revoked:
            print("✅ CONDITIONS MET: should auto-login.")
        else:
            print("❌ CONDITIONS FAILED.")
            if not auth_obj.broker:
                print("   - Missing broker")
            if auth_obj.is_revoked:
                print("   - Revoked")

    except Exception as e:
        print(f"❌ Exception: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    diagnose()
