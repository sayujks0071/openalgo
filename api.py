import os
from typing import Any, Dict, Optional

import pandas as pd
import requests


class api:
    """Minimal OpenAlgo API client for local strategy execution."""

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

    def history(
        self,
        symbol: str,
        exchange: str,
        interval: str,
        start_date: str,
        end_date: str,
        source: Optional[str] = None,
    ) -> pd.DataFrame:
        payload = {
            "symbol": symbol,
            "exchange": exchange,
            "interval": interval,
            "start_date": start_date,
            "end_date": end_date,
        }
        if source:
            payload["source"] = source
        response = self._post("history", payload)
        if response.get("status") == "success":
            data = response.get("data", [])
            if data:
                return pd.DataFrame(data)
        if not source:
            payload["source"] = "db"
            response = self._post("history", payload)
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
