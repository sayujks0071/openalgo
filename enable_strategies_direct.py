#!/usr/bin/env python3
"""
Enable All Strategies - Direct Database Access
Bypasses web authentication
"""
import os
import sys
from sqlalchemy import text

sys.path.insert(0, os.getcwd())
from database.auth_db import engine

OPENALGO_API_KEY = "cf02b763dd0ea379cf1476f37a48ab54faceefa4f76721305bde79485d061e9c"

def enable_all_strategies_direct():
    """Enable all strategies by updating database directly"""
    
    with engine.connect() as conn:
        # Get all strategies
        result = conn.execute(text("SELECT id, name, is_scheduled FROM strategy"))
        strategies = result.fetchall()
        
        print(f"Found {len(strategies)} strategies\n")
        print("=" * 70)
        
        enabled_count = 0
        for strategy_id, name, is_scheduled in strategies:
            print(f"Strategy: {name}")
            
            # Enable scheduling
            if not is_scheduled:
                conn.execute(
                    text("UPDATE strategy SET is_scheduled = 1 WHERE id = :id"),
                    {"id": strategy_id}
                )
                print(f"  ✅ Scheduling enabled")
                enabled_count += 1
            else:
                print(f"  ℹ️  Already scheduled")
        
        conn.commit()
        
        print("\n" + "=" * 70)
        print(f"✅ Enabled scheduling for {enabled_count} strategies")
        print("=" * 70)
        print("\nNote: Strategies are now scheduled but not running.")
        print("They will start automatically at their scheduled times.")
        print("To start them immediately, use the web UI or API.")
        
        # Show all scheduled strategies
        result = conn.execute(
            text("SELECT name, is_scheduled, is_running FROM strategy WHERE is_scheduled = 1")
        )
        scheduled = result.fetchall()
        
        print(f"\n📊 Scheduled Strategies ({len(scheduled)}):")
        for name, is_scheduled, is_running in scheduled:
            status = "🟢 Running" if is_running else "⏸️  Stopped"
            print(f"  {status} {name}")

if __name__ == "__main__":
    try:
        enable_all_strategies_direct()
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
