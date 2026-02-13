# utils/config.py

import os

from dotenv import load_dotenv

# Load environment variables from .env file.
# By default, do NOT override already-set environment variables so that
# deployments (Docker/Railway/systemd) and CLI overrides work as expected.
dotenv_override = os.getenv("OPENALGO_DOTENV_OVERRIDE", "").lower() in ("1", "true", "yes")
load_dotenv(override=dotenv_override)


def get_broker_api_key():
    return os.getenv("BROKER_API_KEY")


def get_broker_api_secret():
    return os.getenv("BROKER_API_SECRET")


def get_login_rate_limit_min():
    return os.getenv("LOGIN_RATE_LIMIT_MIN", "5 per minute")


def get_login_rate_limit_hour():
    return os.getenv("LOGIN_RATE_LIMIT_HOUR", "25 per hour")


def get_host_server():
    return os.getenv("HOST_SERVER", "http://127.0.0.1:5000")
