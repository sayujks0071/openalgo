import os
import sys

# Setup path
sys.path.insert(0, os.getcwd())

from database.auth_db import Auth, db_session
from dotenv import load_dotenv

load_dotenv()


def login_user(username="sks20417"):
    try:
        user = Auth.query.filter_by(name=username).first()
        if user:
            print(f"Updating user {username}...")
            user.broker = "dhan"
            user.auth = os.getenv("BROKER_API_KEY")
            user.is_revoked = False
            user.feed_token = "live_feed_token"  # Dhan doesn't use feed token separately usually, but keeping string for schema
            db_session.commit()
            print("User logged in (DB updated).")

            # Verify persistence
            db_session.expire_all()  # valid technique to reload from DB
            user_verify = Auth.query.filter_by(name=username).first()
            print(f"VERIFICATION: Broker: {user_verify.broker}, Revoked: {user_verify.is_revoked}")
        else:
            print(f"User {username} not found in Auth table.")
            # Create user?
            new_user = Auth(
                name=username,
                broker="dhan",
                auth=os.getenv("BROKER_API_KEY"),
                is_revoked=False,
                feed_token="live_feed_token",
                user_id=username,
            )
            db_session.add(new_user)
            db_session.commit()
            print("User created and logged in.")

    except Exception as e:
        print(f"Error logging in: {e}")
    finally:
        db_session.remove()


if __name__ == "__main__":
    login_user()
