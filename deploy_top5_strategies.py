#!/usr/bin/env python3
"""
Deploy Top 5 Best Strategies from antidhan to OpenAlgo Dhan
Uses OpenAlgo API to upload and configure strategies
"""

import os
import sys
import requests
import json
from pathlib import Path

# Configuration
OPENALGO_URL = "https://algo.endoscopicspinehyderabad.in"
API_KEY = os.getenv("OPENALGO_API_KEY", "")  # Set your API key

# Top 5 Strategies to Deploy
STRATEGIES = [
    {
        "name": "AI_Hybrid_Reversion_Breakout",
        "file": "ai_hybrid_reversion_breakout.py",
        "description": "🥇 Best Overall - Win Rate: 82-88%, Sharpe: 3.0-4.0",
        "enabled": True,
        "priority": 1
    },
    {
        "name": "Advanced_ML_Momentum",
        "file": "advanced_ml_momentum_strategy.py",
        "description": "🥈 High Quality Signals - Win Rate: 78-85%, Sharpe: 2.5-3.2",
        "enabled": True,
        "priority": 2
    },
    {
        "name": "SuperTrend_VWAP",
        "file": "supertrend_vwap_strategy.py",
        "description": "🥉 Simple & Effective - Win Rate: 72-78%, Sharpe: 1.8-2.3",
        "enabled": True,
        "priority": 3
    },
    {
        "name": "MCX_Commodity_Momentum",
        "file": "mcx_commodity_momentum_strategy.py",
        "description": "MCX Specialist - Optimized for commodities trading",
        "enabled": True,
        "priority": 4
    },
    {
        "name": "Delta_Neutral_Iron_Condor",
        "file": "delta_neutral_iron_condor_nifty.py",
        "description": "Options Strategy - Controlled risk, steady income",
        "enabled": False,  # Start disabled for safety
        "priority": 5
    }
]


def upload_strategy(strategy_info):
    """Upload a strategy file to OpenAlgo via API"""
    
    file_path = Path("strategies") / strategy_info["file"]
    
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return False
    
    try:
        with open(file_path, 'r') as f:
            strategy_code = f.read()
        
        # Upload via API
        url = f"{OPENALGO_URL}/api/v1/strategy/upload"
        
        payload = {
            "name": strategy_info["name"],
            "code": strategy_code,
            "description": strategy_info["description"],
            "enabled": strategy_info["enabled"]
        }
        
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        print(f"\n📤 Uploading: {strategy_info['name']}")
        print(f"   Description: {strategy_info['description']}")
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code in [200, 201]:
            print(f"✅ Successfully uploaded: {strategy_info['name']}")
            return True
        else:
            print(f"❌ Failed to upload: {strategy_info['name']}")
            print(f"   Status: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error uploading {strategy_info['name']}: {e}")
        return False


def upload_via_web_interface():
    """Instructions for manual upload via web interface"""
    
    print("\n" + "="*70)
    print("🌐 MANUAL UPLOAD VIA WEB INTERFACE")
    print("="*70)
    print("\nIf API upload fails, you can manually upload via the web interface:")
    print(f"\n1. Go to: {OPENALGO_URL}/pythonstrategy")
    print("\n2. Upload each strategy file:")
    
    for i, strategy in enumerate(STRATEGIES, 1):
        file_path = Path("strategies") / strategy["file"]
        print(f"\n   {i}. {strategy['name']}")
        print(f"      File: {file_path}")
        print(f"      {strategy['description']}")
        print(f"      Enable: {'Yes' if strategy['enabled'] else 'No (test first)'}")
    
    print("\n3. Configure strategy parameters in the web interface")
    print("4. Enable strategies one by one and monitor performance")
    print("\n" + "="*70)


def main():
    print("="*70)
    print("🚀 DEPLOYING TOP 5 STRATEGIES TO OPENALGO DHAN")
    print("="*70)
    
    # Check if API key is set
    if not API_KEY:
        print("\n⚠️  OPENALGO_API_KEY not set!")
        print("   Set it with: export OPENALGO_API_KEY='your-api-key'")
        print("\n   Proceeding with manual upload instructions...\n")
        upload_via_web_interface()
        return
    
    # Upload strategies
    results = []
    for strategy in STRATEGIES:
        success = upload_strategy(strategy)
        results.append((strategy["name"], success))
    
    # Summary
    print("\n" + "="*70)
    print("📊 DEPLOYMENT SUMMARY")
    print("="*70)
    
    successful = sum(1 for _, success in results if success)
    total = len(results)
    
    print(f"\nSuccessfully deployed: {successful}/{total} strategies\n")
    
    for name, success in results:
        status = "✅" if success else "❌"
        print(f"{status} {name}")
    
    if successful < total:
        print("\n⚠️  Some strategies failed to upload.")
        upload_via_web_interface()
    
    print("\n" + "="*70)
    print("📈 NEXT STEPS")
    print("="*70)
    print("\n1. Go to your OpenAlgo dashboard:")
    print(f"   {OPENALGO_URL}/dashboard")
    print("\n2. Navigate to 'Python Strategies'")
    print("\n3. Review and configure each strategy:")
    print("   - Set position sizes")
    print("   - Configure risk parameters")
    print("   - Set trading hours")
    print("\n4. Start with paper trading or small positions")
    print("\n5. Monitor performance and adjust as needed")
    print("\n" + "="*70)
    print("\n💡 RECOMMENDED ORDER:")
    print("   1. Start with SuperTrend_VWAP (simplest)")
    print("   2. Add Advanced_ML_Momentum (quality signals)")
    print("   3. Deploy AI_Hybrid (best performance)")
    print("   4. Test MCX_Commodity (if trading commodities)")
    print("   5. Iron_Condor last (requires options approval)")
    print("\n" + "="*70)


if __name__ == "__main__":
    main()
