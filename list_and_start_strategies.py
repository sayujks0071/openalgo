#!/usr/bin/env python3
"""
List and optionally start all Python strategies
Works without web authentication
"""
import os
import glob

# Find all strategy files
strategies_dir = "/Users/mac/openalgo/openalgo/strategies/scripts"
strategy_files = glob.glob(f"{strategies_dir}/*.py")

# Filter out __pycache__ and utility files
strategy_files = [f for f in strategy_files if not f.endswith("__init__.py")]

print("=" * 70)
print(f"Found {len(strategy_files)} Python Strategy Files")
print("=" * 70)
print()

for i, filepath in enumerate(sorted(strategy_files), 1):
    filename = os.path.basename(filepath)
    strategy_name = filename.replace('.py', '')
    print(f"{i:2d}. {strategy_name}")

print()
print("=" * 70)
print("STATUS")
print("=" * 70)
print()
print("⚠️  IMPORTANT:")
print("   These strategies are FILES on disk")
print("   They're configured to auto-start on server launch")
print("   But they're failing because:")
print()
print("   1. ❌ Broker authentication is invalid (expired token)")
print("   2. ❌ You need fresh Dhan credentials")
print()
print("=" * 70)
print("TO FIX")
print("=" * 70)
print()
print("Option 1: Get Fresh Dhan Sandbox Token")
print("   1. Login at: https://api.dhan.co")
print("   2. Go to Sandbox section")
print("   3. Generate new Access Token")
print("   4. Update BROKER_API_KEY in .env file")
print("   5. Restart OpenAlgo server")
print()
print("Option 2: Use Dhan Live (Real Trading)")
print("   1. Get Live API credentials from Dhan")
print("   2. Update .env with live credentials")
print("   3. Change broker from 'dhan_sandbox' to 'dhan'")
print("   4. Restart server")
print()
print("=" * 70)
print()
print("Currently the strategies START but immediately fail")
print("because they can't authenticate with the broker.")
print()
