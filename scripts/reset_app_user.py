import os
import sys

# Setup path
sys.path.insert(0, os.getcwd())

from database.user_db import User, db_session, add_user, find_user_by_username
from dotenv import load_dotenv

# Load env for PEPPER
load_dotenv()


def reset_user():
    username = "sks20417"
    email = "test@example.com"
    password = "password123"

    try:
        user = User.query.filter_by(username=username).first()
        if user:
            print(f"Found user {username}. Resetting password...")
            user.set_password(password)
            db_session.commit()
            print("Password reset successfully.")
        else:
            print(f"User {username} not found. Creating...")
            # Check if any admin exists
            admin = find_user_by_username()
            is_admin = True if not admin else False

            new_user = add_user(username, email, password, is_admin=is_admin)
            if new_user:
                print("User created successfully.")
            else:
                print("Failed to create user.")

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    reset_user()
