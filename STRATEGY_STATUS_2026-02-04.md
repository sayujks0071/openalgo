# Live Paper Trading Status Report

Date: 2026-02-04
Time: 13:36 PM IST

## Summary
All 4 strategies are running and logging properly.

## Live Status (with PID + Uptime)
Running and logging:
- ai_hybrid_reliance_20260203095647.py (hardened): PID 57871, uptime 02:37:09
- ai_hybrid_reliance.py: PID 76733, uptime 00:14:17
- supertrend_vwap_banknifty.py: PID 76734, uptime 00:14:17
- supertrend_vwap_nifty.py: PID 76735, uptime 00:14:17

## Real-time Monitoring
```
tail -f /Users/mac/openalgo/openalgo/live_*.log
```

## Recent Log Excerpts
ai_hybrid_reliance_20260203095647.py (hardened, last 5 lines):
```
2026-02-04 13:26:14,707 | INFO | 📊 Cycle 296 | Pos: 1 | Orders: 1/10 | Open: 16 | Filled: 0
2026-02-04 13:28:44,873 | INFO | 📊 Cycle 301 | Pos: 1 | Orders: 1/10 | Open: 16 | Filled: 0
2026-02-04 13:31:15,043 | INFO | 📊 Cycle 306 | Pos: 1 | Orders: 1/10 | Open: 16 | Filled: 0
2026-02-04 13:33:45,239 | INFO | 📊 Cycle 311 | Pos: 1 | Orders: 1/10 | Open: 16 | Filled: 0
2026-02-04 13:36:15,419 | INFO | 📊 Cycle 316 | Pos: 1 | Orders: 1/10 | Open: 16 | Filled: 0
```

ai_hybrid_reliance.py (last 5 lines):
```
Insufficient data for sector strength check (0 rows). Defaulting to allow trades.
Status: RSI=1.4 | Price=130.19 | BB=[129.67, 133.03] | Vol=53548
Insufficient data for sector strength check (0 rows). Defaulting to allow trades.
Status: RSI=1.4 | Price=130.19 | BB=[129.67, 133.03] | Vol=53548
Insufficient data for sector strength check (0 rows). Defaulting to allow trades.
```

supertrend_vwap_banknifty.py (last 5 lines):
```
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
```

supertrend_vwap_nifty.py (last 5 lines):
```
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
```

## Notes
Strategies will continue running until market close (3:30 PM IST) or manual stop.
