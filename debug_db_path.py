import os
import sys
from sqlalchemy import create_engine, inspect

# Setup path
sys.path.insert(0, os.getcwd())

from database.auth_db import Auth, db_session, engine


def check_db():
    print(f"CWD: {os.getcwd()}")
    print(f"DATABASE_URL: {os.environ.get('DATABASE_URL')}")
    print(f"Engine URL: {engine.url}")

    # Check rows
    users = Auth.query.all()
    print(f"Auth Rows: {len(users)}")
    for user in users:
        print(f"User: {user.name}, Broker: '{user.broker}', Revoked: {user.is_revoked}")


if __name__ == "__main__":
    check_db()
