import os
from datetime import datetime
from typing import Any, Dict, Optional

import pandas as pd
import requests


def normalize_symbol(symbol: str) -> str:
    return symbol.replace(" ", "").upper()


def is_market_open(now: Optional[datetime] = None) -> bool:
    now = now or datetime.now()
    if now.weekday() >= 5:
        return False
    market_open = now.replace(hour=9, minute=15, second=0, microsecond=0)
    market_close = now.replace(hour=15, minute=30, second=0, microsecond=0)
    return market_open <= now <= market_close


def calculate_intraday_vwap(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    df = df.copy()
    if "volume" not in df.columns:
        df["volume"] = 0
    typical_price = (df["high"] + df["low"] + df["close"]) / 3.0
    cumulative_vp = (typical_price * df["volume"]).cumsum()
    cumulative_vol = df["volume"].cumsum().replace(0, pd.NA)
    df["vwap"] = cumulative_vp / cumulative_vol
    df["vwap_dev"] = (df["close"] - df["vwap"]) / df["vwap"]
    return df


class APIClient:
    def __init__(self, api_key: str, host: Optional[str] = None, timeout: int = 30):
        if not api_key:
            raise ValueError("api_key is required")
        self.api_key = api_key
        self.host = host or os.getenv("OPENALGO_HOST", "http://127.0.0.1:5000")
        self.timeout = timeout

    def _post(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.host.rstrip('/')}/api/v1/{path.lstrip('/')}"
        data = dict(payload)
        data["apikey"] = self.api_key
        resp = requests.post(url, json=data, timeout=self.timeout)
        try:
            return resp.json()
        except Exception:
            return {"status": "error", "message": "Invalid JSON response", "raw": resp.text}

    def history(self, **kwargs) -> pd.DataFrame:
        response = self._post("history", kwargs)
        if response.get("status") == "success":
            data = response.get("data", [])
            if data:
                return pd.DataFrame(data)
        # Fallback to historify DB if API returns no rows
        if "source" not in kwargs:
            fallback = dict(kwargs)
            fallback["source"] = "db"
            response = self._post("history", fallback)
            if response.get("status") == "success":
                data = response.get("data", [])
                if data:
                    return pd.DataFrame(data)
        return pd.DataFrame()

    def placesmartorder(self, **kwargs) -> Dict[str, Any]:
        return self._post("placesmartorder", kwargs)

    def placeorder(self, **kwargs) -> Dict[str, Any]:
        return self._post("placeorder", kwargs)

    def positionbook(self) -> Dict[str, Any]:
        return self._post("positionbook", {})

    def orderbook(self) -> Dict[str, Any]:
        return self._post("orderbook", {})


class PositionManager:
    def __init__(self, symbol: str, exchange: Optional[str] = None, product: Optional[str] = None, quantity: Optional[int] = None):
        self.symbol = normalize_symbol(symbol)
        self.exchange = (exchange or os.getenv("EXCHANGE", "NSE")).upper()
        self.product = (product or os.getenv("PRODUCT", "MIS")).upper()
        self.default_qty = int(quantity or os.getenv("QUANTITY", "1"))
        api_key = os.getenv("OPENALGO_APIKEY")
        host = os.getenv("OPENALGO_HOST", "http://127.0.0.1:5000")
        if not api_key:
            raise ValueError("OPENALGO_APIKEY not set")
        self.client = APIClient(api_key=api_key, host=host)
        self.strategy = os.getenv("STRATEGY_NAME", f"strategy_{self.symbol}")

    def _fetch_net_position(self) -> int:
        try:
            resp = self.client.positionbook()
            if resp.get("status") != "success":
                return 0
            for pos in resp.get("data", []):
                if normalize_symbol(pos.get("symbol", "")) == self.symbol and pos.get("exchange", "").upper() == self.exchange:
                    try:
                        return int(float(pos.get("quantity", 0)))
                    except Exception:
                        return 0
        except Exception:
            return 0
        return 0

    def get_net_position(self) -> int:
        return self._fetch_net_position()

    def _place(self, action: str, qty: int, position_size: int) -> Dict[str, Any]:
        return self.client.placesmartorder(
            strategy=self.strategy,
            symbol=self.symbol,
            action=action,
            exchange=self.exchange,
            price_type="MARKET",
            product=self.product,
            quantity=qty,
            position_size=position_size,
        )

    def update_position(self, qty: int, price: float, action: str) -> Dict[str, Any]:
        current = self.get_net_position()
        new_pos = current + qty if action.upper() == "BUY" else current - qty
        return self._place(action.upper(), qty, new_pos)

    def execute_trade(self, action: str, details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        qty = self.default_qty
        current = self.get_net_position()
        new_pos = current + qty if action.upper() == "BUY" else current - qty
        return self._place(action.upper(), qty, new_pos)
