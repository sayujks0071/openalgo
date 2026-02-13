#!/usr/bin/env python3
"""
Enable All Strategies for Live Trading
WARNING: This will start ALL strategies - use with caution!
"""

import requests
import json
import os
import sys

# Configuration
OPENALGO_URL = "https://algo.endoscopicspinehyderabad.in"
API_KEY = os.getenv("OPENALGO_API_KEY", "68042aa7ba93928ee399c3b620f0b5b8fbcecd17d7ac565b865dc672a346e46b")

def get_all_strategies():
    """Fetch all strategies from OpenAlgo"""
    try:
        url = f"{OPENALGO_URL}/pythonstrategy/api/strategies"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch strategies: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching strategies: {e}")
        return None


def start_strategy(strategy_id, strategy_name):
    """Start a single strategy"""
    try:
        url = f"{OPENALGO_URL}/pythonstrategy/start/{strategy_id}"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        
        response = requests.post(url, headers=headers)
        
        if response.status_code in [200, 201]:
            print(f"✅ Started: {strategy_name}")
            return True
        else:
            data = response.json() if response.headers.get('content-type') == 'application/json' else {}
            message = data.get('message', response.text)
            print(f"⚠️  {strategy_name}: {message}")
            return False
    except Exception as e:
        print(f"❌ Error starting {strategy_name}: {e}")
        return False


def enable_schedule(strategy_id, strategy_name):
    """Enable schedule for a strategy"""
    try:
        url = f"{OPENALGO_URL}/pythonstrategy/toggle_schedule/{strategy_id}"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        
        response = requests.post(url, headers=headers)
        
        if response.status_code in [200, 201]:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error enabling schedule for {strategy_name}: {e}")
        return False


def main():
    print("=" * 70)
    print("⚠️  WARNING: ENABLING ALL STRATEGIES FOR LIVE TRADING")
    print("=" * 70)
    print()
    print("This will:")
    print("  1. Fetch all your strategies")
    print("  2. Enable scheduling for all")
    print("  3. Start all strategies immediately")
    print()
    print("⚠️  IMPORTANT:")
    print("  - Make sure you have sufficient funds in your trading account")
    print("  - All strategies will trade with REAL MONEY")
    print("  - Monitor positions actively")
    print("  - Have risk management in place")
    print()
    
    # Check for --confirm flag
    if "--confirm" not in sys.argv:
        confirm = input("Type 'YES' to proceed or anything else to cancel: ")
        
        if confirm != "YES":
            print("\n❌ Operation cancelled.")
            return
    else:
        print("✅ Auto-confirmed via --confirm flag\n")
    
    print("\n" + "=" * 70)
    print("📊 FETCHING STRATEGIES")
    print("=" * 70)
    
    strategies = get_all_strategies()
    
    if not strategies:
        print("❌ Could not fetch strategies. Check your API key and connection.")
        return
    
    print(f"\n✅ Found {len(strategies)} strategies\n")
    
    # Show all strategies
    print("=" * 70)
    print("STRATEGY LIST")
    print("=" * 70)
    for i, strat in enumerate(strategies, 1):
        name = strat.get('name', 'Unnamed')
        status = "Running" if strat.get('is_running') else "Stopped"
        scheduled = "Scheduled" if strat.get('is_scheduled') else "Not Scheduled"
        print(f"{i:2d}. {name:40s} {status:10s} {scheduled}")
    
    print("\n" + "=" * 70)
    print("🚀 STARTING ALL STRATEGIES")
    print("=" * 70)
    print()
    
    results = []
    for strat in strategies:
        strategy_id = strat.get('id')
        strategy_name = strat.get('name', 'Unnamed')
        
        if not strategy_id:
            continue
        
        # Enable scheduling first
        enable_schedule(strategy_id, strategy_name)
        
        # Start the strategy
        success = start_strategy(strategy_id, strategy_name)
        results.append((strategy_name, success))
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    
    successful = sum(1 for _, success in results if success)
    total = len(results)
    
    print(f"\nSuccessfully started: {successful}/{total} strategies\n")
    
    print("✅ Successfully Started:")
    for name, success in results:
        if success:
            print(f"   - {name}")
    
    if successful < total:
        print("\n⚠️  Could Not Start:")
        for name, success in results:
            if not success:
                print(f"   - {name}")
    
    print("\n" + "=" * 70)
    print("📈 NEXT STEPS")
    print("=" * 70)
    print("\n1. Monitor your dashboard:")
    print(f"   {OPENALGO_URL}/dashboard")
    print("\n2. Check Python Strategies page:")
    print(f"   {OPENALGO_URL}/pythonstrategy")
    print("\n3. Monitor your trading account")
    print("\n4. Watch for order notifications")
    print("\n5. Be ready to stop strategies if needed")
    print("\n" + "=" * 70)
    print("\n⚠️  TRADING IS NOW LIVE - Monitor actively! ⚠️")
    print()


if __name__ == "__main__":
    main()
