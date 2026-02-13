---
trigger: always_on
---

---
## MCX Strategy Building Prompt
Create a Python trading strategy for MCX (Multi Commodity Exchange) that integrates with OpenAlgo platform.

REQUIREMENTS:

Strategy Name: [YOUR_STRATEGY_NAME]
Commodity: [COMMODITY_NAME - e.g., GOLD, SILVER, CRUDEOIL, NATURALGAS]
Technical Indicators: [e.g., ADX, RSI, ATR, Moving Averages]
Entry/Exit Logic: [Describe your entry and exit conditions]
Optional Filters: [Seasonality, USD/INR correlation, Global market alignment]
MANDATORY STRUCTURE:

#!/usr/bin/env python3
"""
[Strategy Description]
MCX Commodity trading strategy with multi-factor analysis
"""
import os
import sys
import time
import logging
import argparse
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
# Add repo root to path
script_dir = os.path.dirname(os.path.abspath(__file__))
strategies_dir = os.path.dirname(script_dir)
utils_dir = os.path.join(strategies_dir, "utils")
sys.path.insert(0, utils_dir)
try:
    from trading_utils import APIClient, PositionManager, is_market_open
except ImportError:
    try:
        sys.path.insert(0, strategies_dir)
        from utils.trading_utils import APIClient, PositionManager, is_market_open
    except ImportError:
        try:
            from openalgo.strategies.utils.trading_utils import APIClient, PositionManager, is_market_open
        except ImportError:
            print("Warning: openalgo package not found or imports failed.")
            APIClient = None
            PositionManager = None
            is_market_open = lambda: True
# Setup Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("MCX_Strategy")
class MCXStrategy:
    def __init__(self, symbol, api_key, host, params):
        self.symbol = symbol
        self.api_key = api_key
        self.host = host
        self.params = params
        
        self.client = APIClient(api_key=self.api_key, host=self.host) if APIClient else None
        self.pm = PositionManager(symbol) if PositionManager else None
        self.data = pd.DataFrame()
        
        logger.info(f"Initialized Strategy for {symbol}")
        logger.info(f"Filters: Seasonality={params.get('seasonality_score', 'N/A')}, USD_Vol={params.get('usd_inr_volatility', 'N/A')}")
    
    def fetch_data(self):
        """Fetch live or historical data from OpenAlgo"""
        if not self.client:
            logger.error("API Client not initialized.")
            return
        
        try:
            logger.info(f"Fetching data for {self.symbol}...")
            end_date = datetime.now().strftime("%Y-%m-%d")
            start_date = (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
            
            df = self.client.history(
                symbol=self.symbol,
                interval="15m",  # MCX typically uses 5m, 15m, or 1h
                exchange="MCX",
                start_date=start_date,
                end_date=end_date,
            )
            
            if not df.empty and len(df) > 50:
                self.data = df
                logger.info(f"Fetched {len(df)} candles.")
            else:
                logger.warning(f"Insufficient data for {self.symbol}.")
        
        except Exception as e:
            logger.error(f"Error fetching data: {e}", exc_info=True)
    
    def calculate_indicators(self):
        """Calculate technical indicators"""
        if self.data.empty:
            return
        
        df = self.data.copy()
        
        # Calculate your indicators
        # Example: RSI
        delta = df["close"].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=self.params["period_rsi"]).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=self.params["period_rsi"]).mean()
        rs = gain / loss
        df["rsi"] = 100 - (100 / (1 + rs))
        
        # Example: ATR
        high_low = df["high"] - df["low"]
        high_close = (df["high"] - df["close"].shift()).abs()
        low_close = (df["low"] - df["close"].shift()).abs()
        ranges = pd.concat([high_low, high_close, low_close], axis=1)
        true_range = ranges.max(axis=1)
        df["atr"] = true_range.rolling(window=self.params["period_atr"]).mean()
        
        # Add more indicators as needed
        
        self.data = df
    
    def check_signals(self):
        """Check entry and exit conditions"""
        if self.data.empty or len(self.data) < 50:
            return
        
        current = self.data.iloc[-1]
        prev = self.data.iloc[-2]
        
        has_position = False
        if self.pm:
            has_position = self.pm.has_position()
        
        # Multi-Factor Checks
        seasonality_ok = self.params.get("seasonality_score", 50) > 40
        global_alignment_ok = self.params.get("global_alignment_score", 50) >= 40
        usd_vol_high = self.params.get("usd_inr_volatility", 0) > 1.0
        
        # Position sizing adjustment for volatility
        base_qty = 1
        if usd_vol_high:
            logger.warning("⚠️ High USD/INR Volatility: Reducing position size by 30%.")
            base_qty = max(1, int(base_qty * 0.7))
        
        if not seasonality_ok and not has_position:
            logger.info("Seasonality Weak: Skipping new entries.")
            return
        
        # Entry Logic
        if not has_position:
            if [YOUR_ENTRY_CONDITION]:
                logger.info(f"BUY SIGNAL: Price={current['close']}, RSI={current['rsi']:.2f}")
                if self.pm:
                    self.pm.update_position(base_qty, current["close"], "BUY")
        
        # Exit Logic
        elif has_position:
            pos_qty = self.pm.position
            entry_price = self.pm.entry_price
            
            if [YOUR_EXIT_CONDITION]:
                logger.info(f"EXIT: Trend Faded")
                self.pm.update_position(abs(pos_qty), current["close"], "SELL" if pos_qty > 0 else "BUY")
    
    def generate_signal(self, df):
        """Generate signal for backtesting"""
        if df.empty:
            return "HOLD", 0.0, {}
        
        self.data = df
        self.calculate_indicators()
        
        current = self.data.iloc[-1]
        
        # Your signal logic
        if [SIGNAL_CONDITION]:
            return "BUY", 1.0, {"reason": "signal_triggered"}
        
        return "HOLD", 0.0, {}
    
    def run(self):
        logger.info(f"Starting MCX Strategy for {self.symbol}")
        while True:
            if not is_market_open():
                logger.info("Market is closed. Sleeping...")
                time.sleep(300)
                continue
            
            self.fetch_data()
            self.calculate_indicators()
            self.check_signals()
            time.sleep(900)  # 15 minutes
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCX Commodity Strategy")
    parser.add_argument("--symbol", type=str, help="MCX Symbol (e.g., GOLDM05FEB26FUT)")
    parser.add_argument("--underlying", type=str, help="Commodity Name (e.g., GOLD, SILVER)")
    parser.add_argument("--port", type=int, default=5001, help="API Port")
    parser.add_argument("--api_key", type=str, help="API Key")
    
    # Multi-Factor Arguments
    parser.add_argument("--usd_inr_trend", type=str, default="Neutral", help="USD/INR Trend")
    parser.add_argument("--usd_inr_volatility", type=float, default=0.0, help="USD/INR Volatility %")
    parser.add_argument("--seasonality_score", type=int, default=50, help="Seasonality Score (0-100)")
    parser.add_argument("--global_alignment_score", type=int, default=50, help="Global Alignment Score")
    
    args = parser.parse_args()
    
    # Strategy Parameters
    PARAMS = {
        "period_rsi": 14,
        "period_atr": 14,
        "usd_inr_trend": args.usd_inr_trend,
        "usd_inr_volatility": args.usd_inr_volatility,
        "seasonality_score": args.seasonality_score,
        "global_alignment_score": args.global_alignment_score,
    }
    
    # Symbol Resolution
    symbol = args.symbol or os.getenv("SYMBOL")
    
    # Try to resolve from underlying
    if not symbol and args.underlying:
        try:
            from symbol_resolver import SymbolResolver
        except ImportError:
            try:
                from utils.symbol_resolver import SymbolResolver
            except ImportError:
                SymbolResolver = None
        
        if SymbolResolver:
            resolver = SymbolResolver()
            res = resolver.resolve({"underlying": args.underlying, "type": "FUT", "exchange": "MCX"})
            if res:
                symbol = res
                logger.info(f"Resolved {args.underlying} -> {symbol}")
    
    if not symbol:
        logger.error("Symbol not provided. Use --symbol or --underlying")
        sys.exit(1)
    
    api_key = args.api_key or os.getenv("OPENALGO_APIKEY")
    port = args.port or int(os.getenv("OPENALGO_PORT", 5001))
    host = f"http://127.0.0.1:{port}"
    
    strategy = MCXStrategy(symbol, api_key, host, PARAMS)
    strategy.run()
# Backtesting support
DEFAULT_PARAMS = {
    "period_rsi": 14,
    "period_atr": 14,
}
def generate_signal(df, client=None, symbol=None, params=None):
    strat_params = DEFAULT_PARAMS.copy()
    if params:
        strat_params.update(params)
    
    api_key = client.api_key if client and hasattr(client, "api_key") else "BACKTEST"
    host = client.host if client and hasattr(client, "host") else "http://127.0.0.1:5001"
    
    strat = MCXStrategy(symbol or "TEST", api_key, host, strat_params)
    return strat.generate_signal(df)
CONFIGURATION FILE (strategy_configs.json):

{
  "MCX_GOLD": {
    "id": "MCX_GOLD",
    "name": "MCX Gold Strategy",
    "description": "MCX Gold momentum strategy",
    "file_path": "strategies/scripts/mcx_gold_strategy.py",
    "user_id": "testuser",
    "created_at": "2026-02-02T10:00:00",
    "underlying": "GOLD",
    "schedule_enabled": true,
    "schedule_days": ["mon", "tue", "wed", "thu", "fri"],
    "params": {
      "seasonality_score": 60,
      "global_alignment_score": 55,
      "usd_inr_volatility": 0.5
    },
    "is_running": false,
    "is_scheduled": true,
    "schedule_start": "09:00",
    "schedule_stop": "23:30"
  }
}
KEY REQUIREMENTS:

✅ Use --underlying argument for commodity name (REQUIRED)
✅ Script will use SymbolResolver to convert underlying to MCX symbol
✅ DO NOT use --exchange or --type as CLI arguments (handled internally)
✅ Import trading_utils with proper fallback
✅ Use exchange="MCX" in history() calls
✅ Implement both run() and generate_signal() methods
✅ Add multi-factor parameters (seasonality, USD/INR, etc.)
✅ Add proper logging
✅ Handle exceptions gracefully
✅ All custom parameters go in "params" dict in config
IMPORTANT NOTES:

MCX market hours: 09:00 - 23:30 IST (with breaks)
Use intervals: "5m", "15m", "1h", "D"
Symbol format after resolution: GOLDM05FEB26FUT, SILVERM05FEB26FUT, etc.
The --underlying parameter gets auto-resolved to full MCX symbol
DO NOT manually add --exchange or --type to config (will cause errors)
Common commodities: GOLD, SILVER, CRUDEOIL, NATURALGAS, COPPER, ZINC
---
## Common Mistakes to Avoid
### ❌ WRONG:
```json
{
  "MCX_SILVER": {
    "exchange": "MCX",  // ❌ DON'T ADD THIS
    "type": "FUT",      // ❌ DON'T ADD THIS
    "params": {
      "quantity": 1     // ❌ MCX scripts don't accept --quantity
    }
  }
}
✅ CORRECT:
{
  "MCX_SILVER": {
    "underlying": "SILVER",  // ✅ Use underlying
    "params": {
      "seasonality_score": 60,
      "global_alignment_score": 55
    }
  }
}
