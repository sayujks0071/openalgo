#!/usr/bin/env python3
"""
Regenerate (rotate) the OpenAlgo API key for a user in the local database.

This updates the `api_keys` table used by `/api/v1/*` authentication and is the
key strategy scripts should use via `OPENALGO_APIKEY` / `OPENALGO_API_KEY`.
"""

from __future__ import annotations

import argparse
import secrets
import sys
from pathlib import Path


def load_env(openalgo_dir: Path) -> None:
    try:
        from dotenv import load_dotenv

        load_dotenv(openalgo_dir / ".env", override=False)
    except Exception:
        pass


def get_default_user_id() -> str | None:
    try:
        from sqlalchemy import desc

        from database.auth_db import Auth

        auth_obj = Auth.query.filter_by(is_revoked=False).order_by(desc(Auth.id)).first()
        return auth_obj.name if auth_obj else None
    except Exception:
        return None


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    openalgo_dir = script_dir.parent
    sys.path.insert(0, str(openalgo_dir))
    load_env(openalgo_dir)

    parser = argparse.ArgumentParser(description="Rotate local OpenAlgo API key")
    parser.add_argument("--user-id", default=None, help="User id to rotate (defaults to active auth user)")
    parser.add_argument(
        "--length-bytes",
        type=int,
        default=32,
        help="Token length in bytes (hex string will be 2x chars)",
    )
    args = parser.parse_args()

    user_id = args.user_id or get_default_user_id()
    if not user_id:
        print("❌ Could not determine user_id (no active auth session). Provide --user-id.")
        return 2

    api_key = secrets.token_hex(max(16, int(args.length_bytes)))

    from database.auth_db import upsert_api_key

    upsert_api_key(user_id=user_id, api_key=api_key)

    print("✅ OpenAlgo API key rotated.")
    print(f"user_id: {user_id}")
    print(f"api_key: {api_key}")
    print("\nSet in your environment for strategy scripts, e.g.:")
    print("  export OPENALGO_APIKEY='<api_key>'")
    print("  export OPENALGO_API_KEY='<api_key>'")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

