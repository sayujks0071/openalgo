---
trigger: always_on
---

NSE Strategy Building Prompt
Create a Python trading strategy for NSE (National Stock Exchange) that integrates with OpenAlgo platform.
REQUIREMENTS:
1. Strategy Name: [YOUR_STRATEGY_NAME]
2. Trading Symbol: [STOCK_SYMBOL - e.g., RELIANCE, INFY, NIFTY 50]
3. Technical Indicators: [e.g., RSI, MACD, Bollinger Bands, SuperTrend, VWAP]
4. Entry/Exit Logic: [Describe your entry and exit conditions]
MANDATORY STRUCTURE:
```python
#!/usr/bin/env python3
"""
[Strategy Description]
"""
import os
import sys
import time
import argparse
import logging
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
# Add project root to path
script_dir = os.path.dirname(os.path.abspath(__file__))
strategies_dir = os.path.dirname(script_dir)
utils_dir = os.path.join(strategies_dir, 'utils')
sys.path.insert(0, utils_dir)
try:
    from trading_utils import APIClient, PositionManager, is_market_open, normalize_symbol
except ImportError:
    try:
        sys.path.insert(0, strategies_dir)
        from utils.trading_utils import APIClient, PositionManager, is_market_open, normalize_symbol
    except ImportError:
        try:
            from openalgo.strategies.utils.trading_utils import APIClient, PositionManager, is_market_open, normalize_symbol
        except ImportError:
            print("Warning: openalgo package not found or imports failed.")
            APIClient = None
            PositionManager = None
            normalize_symbol = lambda s: s
            is_market_open = lambda: True
class MyNSEStrategy:
    def __init__(self, symbol, api_key, port, **kwargs):
        self.symbol = symbol
        self.host = f"http://127.0.0.1:{port}"
        self.client = APIClient(api_key=api_key, host=self.host)
        
        # Setup Logger
        self.logger = logging.getLogger(f"NSE_{symbol}")
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        
        # Strategy parameters from kwargs
        self.param1 = kwargs.get('param1', default_value)
        # Add more parameters as needed
        
        self.pm = PositionManager(symbol) if PositionManager else None
    
    def calculate_signal(self, df):
        """Calculate signal for backtesting support"""
        if df.empty or len(df) < 20:
            return 'HOLD', 0.0, {}
        
        # Calculate your indicators here
        # df['indicator'] = ...
        
        last = df.iloc[-1]
        
        # Your entry logic
        if [ENTRY_CONDITION]:
            return 'BUY', 1.0, {'reason': 'entry_signal', 'price': last['close']}
        
        return 'HOLD', 0.0, {}
    
    def run(self):
        self.symbol = normalize_symbol(self.symbol)
        self.logger.info(f"Starting strategy for {self.symbol}")
        
        while True:
            if not is_market_open():
                time.sleep(60)
                continue
            
            try:
                # Determine exchange (NSE for stocks, NSE_INDEX for indices)
                exchange = "NSE_INDEX" if "NIFTY" in self.symbol.upper() else "NSE"
                
                # Fetch historical data
                df = self.client.history(
                    symbol=self.symbol,
                    interval="5m",  # or "1m", "15m", "D", etc.
                    exchange=exchange,
                    start_date=datetime.now().strftime("%Y-%m-%d"),
                    end_date=datetime.now().strftime("%Y-%m-%d")
                )
                
                if df.empty or len(df) < 20:
                    time.sleep(60)
                    continue
                
                # Calculate indicators
                # [YOUR INDICATOR CALCULATIONS]
                
                last = df.iloc[-1]
                current_price = last['close']
                
                # Position management
                if self.pm and self.pm.has_position():
                    # Exit logic
                    pnl = self.pm.get_pnl(current_price)
                    
                    if [EXIT_CONDITION]:
                        self.logger.info(f"Exiting position. PnL: {pnl}")
                        self.pm.update_position(abs(self.pm.position), current_price, 'SELL' if self.pm.position > 0 else 'BUY')
                else:
                    # Entry logic
                    if [ENTRY_CONDITION]:
                        qty = [YOUR_QUANTITY_LOGIC]
                        self.logger.info(f"Entry signal detected. Buying {qty} at {current_price}")
                        self.pm.update_position(qty, current_price, 'BUY')
                
            except Exception as e:
                self.logger.error(f"Error: {e}", exc_info=True)
                time.sleep(60)
            
            time.sleep(60)  # Sleep between iterations
def run_strategy():
    parser = argparse.ArgumentParser(description='NSE Strategy')
    parser.add_argument('--symbol', type=str, required=True, help='Stock Symbol')
    parser.add_argument('--port', type=int, default=5001, help='API Port')
    parser.add_argument('--api_key', type=str, help='API Key')
    # Add your custom parameters
    parser.add_argument('--param1', type=float, default=30.0, help='Parameter 1')
    
    args = parser.parse_args()
    
    api_key = args.api_key or os.getenv('OPENALGO_APIKEY')
    if not api_key:
        print("Error: API Key required")
        return
    
    strategy = MyNSEStrategy(
        args.symbol,
        api_key,
        args.port,
        param1=args.param1
    )
    strategy.run()
# Backtesting support
def generate_signal(df, client=None, symbol=None, params=None):
    strat_params = {'param1': 30.0}
    if params:
        strat_params.update(params)
    
    strat = MyNSEStrategy(
        symbol=symbol or "TEST",
        api_key="dummy",
        port=5001,
        **strat_params
    )
    
    strat.logger.handlers = []
    strat.logger.addHandler(logging.NullHandler())
    
    return strat.calculate_signal(df)
if __name__ == "__main__":
    run_strategy()
CONFIGURATION FILE (strategy_configs.json):

{
  "MY_NSE_STRATEGY": {
    "id": "MY_NSE_STRATEGY",
    "name": "My NSE Strategy",
    "description": "Custom NSE trading strategy",
    "file_path": "strategies/scripts/my_nse_strategy.py",
    "user_id": "testuser",
    "created_at": "2026-02-02T10:00:00",
    "symbol": "RELIANCE",
    "schedule_enabled": true,
    "schedule_days": ["mon", "tue", "wed", "thu", "fri"],
    "params": {
      "param1": 30
    },
    "is_running": false,
    "is_scheduled": true,
    "schedule_start": "09:15",
    "schedule_stop": "15:30"
  }
}
KEY REQUIREMENTS:

✅ Use --symbol argument (REQUIRED)
✅ Import trading_utils with proper fallback
✅ Use normalize_symbol() for symbol preprocessing
✅ Check is_market_open() before trading
✅ Use correct exchange: "NSE" for stocks, "NSE_INDEX" for indices
✅ Implement both run() and calculate_signal() methods
✅ Add proper logging
✅ Handle exceptions gracefully
✅ Support backtesting via generate_signal()
✅ All custom parameters go in "params" dict in config
IMPORTANT NOTES:

DO NOT add --exchange or --type as command-line arguments (these are handled by config helper)
Symbol parameter is REQUIRED and passed via --symbol
Use intervals: "1m", "5m", "15m", "D" (day), etc.
Market hours: NSE is 09:15 - 15:30 IST
---
