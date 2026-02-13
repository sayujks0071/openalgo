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

---

## Snapshot @ 2026-02-04 14:37:42 IST

### Strategy Processes (PID / Uptime)
- Unavailable: process listing blocked (ps/pgrep not permitted in this environment).

### Logs (Last 5 Lines)

`live_ai_hybrid.log`
```
Status: RSI=1.4 | Price=130.19 | BB=[129.67, 133.03] | Vol=53548
Insufficient data for sector strength check (0 rows). Defaulting to allow trades.
Status: RSI=1.4 | Price=130.19 | BB=[129.67, 133.03] | Vol=53548
Insufficient data for sector strength check (0 rows). Defaulting to allow trades.
Status: RSI=1.4 | Price=130.19 | BB=[129.67, 133.03] | Vol=53548
```

`live_banknifty.log`
```
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
```

`live_nifty.log`
```
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
Signal: WAIT | Score: 1.14 | VWAP Dev: -1.14% | ADX: nan
```

`log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log`
```
2026-02-04 14:26:19,496 | INFO | 📊 Cycle 416 | Pos: 1 | Orders: 1/10 | Open: 16 | Filled: 0
2026-02-04 14:28:49,682 | INFO | 📊 Cycle 421 | Pos: 1 | Orders: 1/10 | Open: 16 | Filled: 0
2026-02-04 14:31:19,849 | INFO | 📊 Cycle 426 | Pos: 1 | Orders: 1/10 | Open: 16 | Filled: 0
2026-02-04 14:33:49,991 | INFO | 📊 Cycle 431 | Pos: 1 | Orders: 1/10 | Open: 16 | Filled: 0
2026-02-04 14:36:20,132 | INFO | 📊 Cycle 436 | Pos: 1 | Orders: 1/10 | Open: 16 | Filled: 0
```

---

Timestamp (IST): 2026-02-04 15:37:48 IST

Strategy processes (PID / uptime):
- Unable to read process list (ps not permitted in this environment).

Logs (last 5 lines):
- live_ai_hybrid.log:
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- live_banknifty.log:
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- live_nifty.log:
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
  - 2026-02-04 15:18:55,022 | INFO | 📊 Cycle 521 | Pos: 0 | Orders: 2/10 | Open: 17 | Filled: 0
  - 2026-02-04 15:21:25,257 | INFO | 📊 Cycle 526 | Pos: 0 | Orders: 2/10 | Open: 17 | Filled: 0
  - 2026-02-04 15:23:55,520 | INFO | 📊 Cycle 531 | Pos: 0 | Orders: 2/10 | Open: 17 | Filled: 0
  - 2026-02-04 15:26:25,711 | INFO | 📊 Cycle 536 | Pos: 0 | Orders: 2/10 | Open: 17 | Filled: 0
  - 2026-02-04 15:28:55,876 | INFO | 📊 Cycle 541 | Pos: 0 | Orders: 2/10 | Open: 17 | Filled: 0

---
Timestamp (IST): 2026-02-04 16:37:52 IST

Processes (strategy scripts):
- Unable to read process list: `ps` returned "operation not permitted".

Log tails (last 5 lines):

`live_ai_hybrid.log`:
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...

`live_banknifty.log`:
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...

`live_nifty.log`:
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...

`log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log`:
- 2026-02-04 15:23:55,520 | INFO | 📊 Cycle 531 | Pos: 0 | Orders: 2/10 | Open: 17 | Filled: 0
- 2026-02-04 15:26:25,711 | INFO | 📊 Cycle 536 | Pos: 0 | Orders: 2/10 | Open: 17 | Filled: 0
- 2026-02-04 15:28:55,876 | INFO | 📊 Cycle 541 | Pos: 0 | Orders: 2/10 | Open: 17 | Filled: 0
- 2026-02-04 15:58:56,282 | INFO | ⏸️  Market closed. Waiting...
- 2026-02-04 16:28:56,689 | INFO | ⏸️  Market closed. Waiting...

---
Timestamp (IST): 2026-02-04 17:37:50 IST

Strategy processes (PID / uptime / command):
- MISSING: process list unavailable (ps: operation not permitted).

Log tails (last 5 lines):
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- /Users/mac/openalgo/openalgo/live_banknifty.log
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- /Users/mac/openalgo/openalgo/live_nifty.log
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
  - 2026-02-04 15:28:55,876 | INFO | 📊 Cycle 541 | Pos: 0 | Orders: 2/10 | Open: 17 | Filled: 0
  - 2026-02-04 15:58:56,282 | INFO | ⏸️  Market closed. Waiting...
  - 2026-02-04 16:28:56,689 | INFO | ⏸️  Market closed. Waiting...
  - 2026-02-04 16:58:57,144 | INFO | ⏸️  Market closed. Waiting...
  - 2026-02-04 17:28:57,614 | INFO | ⏸️  Market closed. Waiting...

---
Snapshot @ 2026-02-04 18:38:21 IST

Processes (strategy scripts)
- Unable to read process list (ps: operation not permitted).

Logs (last 5 lines)
- live_ai_hybrid.log:
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- live_banknifty.log:
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- live_nifty.log:
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
  - 2026-02-04 16:28:56,689 | INFO | ⏸️  Market closed. Waiting...
  - 2026-02-04 16:58:57,144 | INFO | ⏸️  Market closed. Waiting...
  - 2026-02-04 17:28:57,614 | INFO | ⏸️  Market closed. Waiting...
  - 2026-02-04 17:59:20,150 | INFO | ⏸️  Market closed. Waiting...
  - 2026-02-04 18:29:20,444 | INFO | ⏸️  Market closed. Waiting...

---
Snapshot @ 2026-02-04 19:51:54 IST

Processes (strategy scripts)
- Unable to read process list (ps: operation not permitted).

Logs (last 5 lines)
- live_ai_hybrid.log:
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- live_banknifty.log:
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- live_nifty.log:
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
  - 2026-02-04 16:58:57,144 | INFO | ⏸️  Market closed. Waiting...
  - 2026-02-04 17:28:57,614 | INFO | ⏸️  Market closed. Waiting...
  - 2026-02-04 17:59:20,150 | INFO | ⏸️  Market closed. Waiting...
  - 2026-02-04 18:29:20,444 | INFO | ⏸️  Market closed. Waiting...
  - 2026-02-04 18:59:20,806 | INFO | ⏸️  Market closed. Waiting...

---
Snapshot @ 2026-02-04 20:51:48 IST

Processes (strategy scripts)
- Unable to read process list (ps: operation not permitted).

Logs (last 5 lines)
- live_ai_hybrid.log:
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- live_banknifty.log:
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- live_nifty.log:
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
  - Market closed. Waiting...
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
  - 2026-02-04 20:48:08,338 | INFO | Max Orders/Day: 10
  - 2026-02-04 20:48:08,338 | INFO | Market Hours: Ignored
  - 2026-02-04 20:48:08,339 | INFO | ============================================================
  - 2026-02-04 20:48:08,671 | INFO | 📊 Cycle 1 | Pos: 0 | Orders: 0/10 | Open: 0 | Filled: 0
  - 2026-02-04 20:50:38,905 | INFO | 📊 Cycle 6 | Pos: 0 | Orders: 0/10 | Open: 0 | Filled: 0

---

Timestamp (IST): 2026-02-04 21:51:55 IST

Processes (PIDs + uptime):
- (unavailable) `ps` not permitted in this environment

Log tail (last 5 lines):

File: /Users/mac/openalgo/openalgo/live_ai_hybrid.log
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

File: /Users/mac/openalgo/openalgo/live_banknifty.log
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

File: /Users/mac/openalgo/openalgo/live_nifty.log
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

File: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
2026-02-04 21:49:05,198 | INFO | Max Orders/Day: 10
2026-02-04 21:49:05,199 | INFO | Market Hours: Ignored
2026-02-04 21:49:05,199 | INFO | ============================================================
2026-02-04 21:49:05,324 | INFO | 📊 Cycle 1 | Pos: 0 | Orders: 0/10 | Open: 0 | Filled: 0
2026-02-04 21:51:35,595 | INFO | 📊 Cycle 6 | Pos: 0 | Orders: 0/10 | Open: 0 | Filled: 0

---

Snapshot Time (IST): 2026-02-04 22:52:09 IST

Strategy Processes (PID | Uptime | Command):
- Unable to list processes: `ps` operation not permitted in this environment.

Log Tails (last 5 lines):

live_ai_hybrid.log:
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

live_banknifty.log:
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

live_nifty.log:
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
2026-02-04 22:48:22,229 | INFO | 📊 Cycle 6 | Pos: 0 | Orders: 0/10 | Open: 0 | Filled: 0
2026-02-04 22:50:52,683 | INFO | 📊 Cycle 11 | Pos: 0 | Orders: 0/10 | Open: 0 | Filled: 0
2026-02-04 22:50:52,695 | INFO | 🧪 SANDBOX: Forcing test BUY order after idle period
2026-02-04 22:50:53,645 | INFO | ✅ BUY 1 RELIANCE | OrderID: 26020448512856
2026-02-04 22:50:53,649 | INFO | 🧪 SANDBOX: Test order successful! Strategy validated.

---

Snapshot Time (IST): 2026-02-04 23:51:52 IST

Strategy Processes (PID | Uptime | Command):
- Unable to list processes: `ps` operation not permitted in this environment.

Log Tails (last 5 lines):

live_ai_hybrid.log:
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

live_banknifty.log:
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

live_nifty.log:
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
2026-02-04 23:39:45,209 | INFO | 📊 Cycle 36 | Pos: 1 | Orders: 1/10 | Open: 4 | Filled: 6
2026-02-04 23:42:15,313 | INFO | 📊 Cycle 41 | Pos: 1 | Orders: 1/10 | Open: 4 | Filled: 6
2026-02-04 23:44:45,380 | INFO | 📊 Cycle 46 | Pos: 1 | Orders: 1/10 | Open: 4 | Filled: 6
2026-02-04 23:47:15,449 | INFO | 📊 Cycle 51 | Pos: 1 | Orders: 1/10 | Open: 4 | Filled: 6
2026-02-04 23:49:45,509 | INFO | 📊 Cycle 56 | Pos: 1 | Orders: 1/10 | Open: 6 | Filled: 6
---
Timestamp (IST): 2026-02-05 00:52:13 IST

Processes (PID / uptime / command):
- Process list unavailable (ps blocked by OS permissions).

Logs (last 5 lines):

/Users/mac/openalgo/openalgo/live_ai_hybrid.log:
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...

/Users/mac/openalgo/openalgo/live_banknifty.log:
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...

/Users/mac/openalgo/openalgo/live_nifty.log:
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...

/Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
  2026-02-05 00:39:46,899 | INFO | 📊 Cycle 156 | Pos: 1 | Orders: 1/10 | Open: 12 | Filled: 6
  2026-02-05 00:42:16,989 | INFO | 📊 Cycle 161 | Pos: 1 | Orders: 1/10 | Open: 12 | Filled: 6
  2026-02-05 00:44:47,055 | INFO | 📊 Cycle 166 | Pos: 1 | Orders: 1/10 | Open: 12 | Filled: 6
  2026-02-05 00:47:17,106 | INFO | 📊 Cycle 171 | Pos: 1 | Orders: 1/10 | Open: 12 | Filled: 6
  2026-02-05 00:49:47,177 | INFO | 📊 Cycle 176 | Pos: 1 | Orders: 1/10 | Open: 12 | Filled: 6
---
Timestamp: 2026-02-05 01:52:02 IST

Strategy Processes (PID | Uptime | Command):
Process list unavailable (ps failed):
zsh:9: operation not permitted: ps

Log tail (last 5): /Users/mac/openalgo/openalgo/live_ai_hybrid.log
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

Log tail (last 5): /Users/mac/openalgo/openalgo/live_banknifty.log
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

Log tail (last 5): /Users/mac/openalgo/openalgo/live_nifty.log
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

Log tail (last 5): /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
2026-02-05 01:39:48,986 | INFO | 📊 Cycle 276 | Pos: 1 | Orders: 1/10 | Open: 15 | Filled: 6
2026-02-05 01:42:19,766 | INFO | 📊 Cycle 281 | Pos: 1 | Orders: 1/10 | Open: 15 | Filled: 6
2026-02-05 01:44:49,858 | INFO | 📊 Cycle 286 | Pos: 1 | Orders: 1/10 | Open: 18 | Filled: 6
2026-02-05 01:47:19,936 | INFO | 📊 Cycle 291 | Pos: 1 | Orders: 1/10 | Open: 18 | Filled: 6
2026-02-05 01:49:49,996 | INFO | 📊 Cycle 296 | Pos: 1 | Orders: 1/10 | Open: 18 | Filled: 6

\n---\nSnapshot @ 2026-02-05 02:52:06 IST
\nStrategy processes (pid, etimes seconds, command):
Process list unavailable: zsh:7: operation not permitted: ps

Last 5 lines (/Users/mac/openalgo/openalgo/live_ai_hybrid.log):
\n---\nSnapshot @ 2026-02-05 02:52:18 IST
\nStrategy processes (pid, etimes seconds, command):
Process list unavailable: zsh:7: no such file or directory: /usr/bin/ps

Last 5 lines (/Users/mac/openalgo/openalgo/live_ai_hybrid.log):
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

Last 5 lines (/Users/mac/openalgo/openalgo/live_banknifty.log):
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

Last 5 lines (/Users/mac/openalgo/openalgo/live_nifty.log):
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

Last 5 lines (/Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log):
2026-02-05 02:39:51,689 | INFO | 📊 Cycle 396 | Pos: 1 | Orders: 1/10 | Open: 21 | Filled: 6
2026-02-05 02:42:21,762 | INFO | 📊 Cycle 401 | Pos: 1 | Orders: 1/10 | Open: 21 | Filled: 6
2026-02-05 02:44:51,834 | INFO | 📊 Cycle 406 | Pos: 1 | Orders: 1/10 | Open: 21 | Filled: 6
2026-02-05 02:47:21,923 | INFO | 📊 Cycle 411 | Pos: 1 | Orders: 1/10 | Open: 24 | Filled: 6
2026-02-05 02:49:51,983 | INFO | 📊 Cycle 416 | Pos: 1 | Orders: 1/10 | Open: 24 | Filled: 6

---

Timestamp (IST): 2026-02-05 03:52:10 IST

Processes (strategy scripts):
- Process list unavailable (ps permission denied).

Log tail: live_ai_hybrid.log
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...

Log tail: live_banknifty.log
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...

Log tail: live_nifty.log
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...
  Market closed. Waiting...

Log tail: log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
  2026-02-05 03:39:53,276 | INFO | 📊 Cycle 516 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
  2026-02-05 03:42:23,345 | INFO | 📊 Cycle 521 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
  2026-02-05 03:44:53,418 | INFO | 📊 Cycle 526 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
  2026-02-05 03:47:23,494 | INFO | 📊 Cycle 531 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
  2026-02-05 03:49:53,548 | INFO | 📊 Cycle 536 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0

---

Timestamp (IST): 2026-02-05 04:51:51 IST

Processes (strategy scripts):
- Unable to list processes (ps: operation not permitted).

Logs (last 5 lines):

live_ai_hybrid.log:
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...

live_banknifty.log:
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...

live_nifty.log:
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...

log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
- 2026-02-05 04:39:54,819 | INFO | 📊 Cycle 636 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
- 2026-02-05 04:42:24,884 | INFO | 📊 Cycle 641 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
- 2026-02-05 04:44:54,946 | INFO | 📊 Cycle 646 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
- 2026-02-05 04:47:25,020 | INFO | 📊 Cycle 651 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
- 2026-02-05 04:49:55,103 | INFO | 📊 Cycle 656 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0

---

Timestamp (IST): 2026-02-05 05:51:49 IST

Processes (strategy scripts):
- Unable to list processes (ps: operation not permitted).

Logs (last 5 lines):

live_ai_hybrid.log:
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...

live_banknifty.log:
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...

live_nifty.log:
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...
- Market closed. Waiting...

log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
- 2026-02-05 05:39:56,488 | INFO | 📊 Cycle 756 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
- 2026-02-05 05:42:26,544 | INFO | 📊 Cycle 761 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
- 2026-02-05 05:44:56,602 | INFO | 📊 Cycle 766 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
- 2026-02-05 05:47:26,680 | INFO | 📊 Cycle 771 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
- 2026-02-05 05:49:56,751 | INFO | 📊 Cycle 776 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0

---

## Snapshot - 2026-02-05 06:51:51 IST

### Strategy Processes

Process list unavailable: `ps` permission restricted in this environment.

### Logs (last 5 lines)

**live_ai_hybrid.log**
```
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
```

**live_banknifty.log**
```
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
```

**live_nifty.log**
```
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
```

**log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log**
```
2026-02-05 06:39:58,059 | INFO | 📊 Cycle 876 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
2026-02-05 06:42:28,121 | INFO | 📊 Cycle 881 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
2026-02-05 06:44:58,186 | INFO | 📊 Cycle 886 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
2026-02-05 06:47:28,240 | INFO | 📊 Cycle 891 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
2026-02-05 06:49:58,314 | INFO | 📊 Cycle 896 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
```
\n---\n
Snapshot @ 2026-02-05 07:52:18 IST

Processes (strategy scripts):
- ps not permitted in this environment; unable to capture PID/uptime.

Log tail: live_ai_hybrid.log
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

Log tail: live_banknifty.log
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

Log tail: live_nifty.log
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...
Market closed. Waiting...

Log tail: log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
2026-02-05 07:39:59,624 | INFO | 📊 Cycle 996 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
2026-02-05 07:42:29,711 | INFO | 📊 Cycle 1001 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
2026-02-05 07:44:59,774 | INFO | 📊 Cycle 1006 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
2026-02-05 07:47:29,823 | INFO | 📊 Cycle 1011 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0
2026-02-05 07:49:59,861 | INFO | 📊 Cycle 1016 | Pos: 1 | Orders: 1/10 | Open: 0 | Filled: 0


---
Snapshot @ 2026-02-05 08:51:54 IST

Processes (strategy scripts):
- ps not permitted in this environment; unable to capture PID/uptime.

Log tail: live_ai_hybrid.log
Insufficient data for RELIANCE: 0 rows
Insufficient data for sector strength check (0 rows). Defaulting to allow trades.
Insufficient data for RELIANCE: 0 rows
Insufficient data for sector strength check (0 rows). Defaulting to allow trades.
Insufficient data for RELIANCE: 0 rows

Log tail: live_banknifty.log
Insufficient data for BANKNIFTY: 0 rows. Need at least 7.
Insufficient data for BANKNIFTY: 0 rows. Need at least 7.
Insufficient data for BANKNIFTY: 0 rows. Need at least 7.
Insufficient data for BANKNIFTY: 0 rows. Need at least 7.
Insufficient data for BANKNIFTY: 0 rows. Need at least 7.

Log tail: live_nifty.log
Insufficient data for NIFTY: 0 rows. Need at least 7.
Insufficient data for NIFTY: 0 rows. Need at least 7.
Insufficient data for NIFTY: 0 rows. Need at least 7.
Insufficient data for NIFTY: 0 rows. Need at least 7.
Insufficient data for NIFTY: 0 rows. Need at least 7.

Log tail: log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
[2026-02-05 08:51:25,272] WARNING in ai_hybrid_reliance_20260203095647: Skipping forced trade: no price available
2026-02-05 08:51:55,274 | INFO | 🧪 SANDBOX: Forcing test BUY order after idle period
[2026-02-05 08:51:55,274] INFO in ai_hybrid_reliance_20260203095647: 🧪 SANDBOX: Forcing test BUY order after idle period
2026-02-05 08:51:55,340 | WARNING | Skipping forced trade: no price available
[2026-02-05 08:51:55,340] WARNING in ai_hybrid_reliance_20260203095647: Skipping forced trade: no price available

---
Timestamp (IST): 2026-02-05 10:55:34 IST

Strategy processes (PID ETIME CMD):
ps unavailable: zsh:5: operation not permitted: ps

Log missing: /Users/mac/openalgo/openalgo/live_ai_hybrid.log

Log missing: /Users/mac/openalgo/openalgo/live_banknifty.log

Log missing: /Users/mac/openalgo/openalgo/live_nifty.log

Log missing: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log

---
Timestamp: 2026-02-05 11:55:56 IST

Processes (PID | Uptime | Command):
- MISSING: unable to read process list (ps: operation not permitted)

Log tails (last 5 lines):
- live_ai_hybrid.log: MISSING
- live_banknifty.log: MISSING
- live_nifty.log: MISSING
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: MISSING

\n---\nTimestamp (IST): 2026-02-05 12:55:49 IST

Strategy processes (PID ETIME CMD):
(process list unavailable: (eval):1: operation not permitted: ps)

Log tails (last 5 lines):
File: /Users/mac/openalgo/openalgo/live_ai_hybrid.log
(missing)

File: /Users/mac/openalgo/openalgo/live_banknifty.log
(missing)

File: /Users/mac/openalgo/openalgo/live_nifty.log
(missing)

File: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
(missing)

---
Timestamp (IST): 2026-02-05 13:55:54 IST

Strategy processes (PID | Uptime | Command):
(process list unavailable: zsh:8: operation not permitted: ps)

Log tails (last 5 lines):
File: /Users/mac/openalgo/openalgo/live_ai_hybrid.log
(missing)

File: /Users/mac/openalgo/openalgo/live_banknifty.log
(missing)

File: /Users/mac/openalgo/openalgo/live_nifty.log
(missing)

File: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
(missing)


---
Timestamp (IST): 2026-02-05 14:55:57 IST

Strategy processes (PID | Uptime | Command):
(process list unavailable: zsh:1: operation not permitted: ps)

Log tails (last 5 lines):
File: /Users/mac/openalgo/openalgo/live_ai_hybrid.log
(missing)

File: /Users/mac/openalgo/openalgo/live_banknifty.log
(missing)

File: /Users/mac/openalgo/openalgo/live_nifty.log
(missing)

File: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
(missing)
---
Snapshot Time (IST): 2026-02-05 15:56:51 IST

Processes (PID, Uptime, Command):
Unable to read process list: [Errno 1] Operation not permitted: 'ps'

Log Tails (last 5 lines):
Log: /Users/mac/openalgo/openalgo/live_ai_hybrid.log
Missing log file.

Log: /Users/mac/openalgo/openalgo/live_banknifty.log
Missing log file.

Log: /Users/mac/openalgo/openalgo/live_nifty.log
Missing log file.

Log: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
Missing log file.
\n---\n
Snapshot: 2026-02-05 16:56:24 IST

Processes (strategy scripts):
 - Unable to read process list (zsh:9: operation not permitted: ps).

Logs (last 5 lines):
 - /Users/mac/openalgo/openalgo/live_ai_hybrid.log
   (missing)
 - /Users/mac/openalgo/openalgo/live_banknifty.log
   (missing)
 - /Users/mac/openalgo/openalgo/live_nifty.log
   (missing)
 - /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
   (missing)
---
Timestamp (IST): 2026-02-05 17:56:51 IST

Process status (strategy scripts):
- Unable to read process list (ps permission restricted in sandbox).

Log tails (last 5 lines):
- live_ai_hybrid.log: missing
- live_banknifty.log: missing
- live_nifty.log: missing
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing

---
Snapshot: 2026-02-05 18:56:45 IST

Processes (strategy scripts):
- Unable to read process list (ps permission restricted in sandbox).

Log tails (last 5 lines):
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log: missing
- /Users/mac/openalgo/openalgo/live_banknifty.log: missing
- /Users/mac/openalgo/openalgo/live_nifty.log: missing
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing
-----
Snapshot: 2026-02-05 20:56:32 IST

Processes:
Missing: unable to read process list (zsh:5: operation not permitted: ps).

Log: /Users/mac/openalgo/openalgo/live_ai_hybrid.log
Missing: file not found.

Log: /Users/mac/openalgo/openalgo/live_banknifty.log
Missing: file not found.

Log: /Users/mac/openalgo/openalgo/live_nifty.log
Missing: file not found.

Log: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
Missing: file not found.

-----
Snapshot @ 2026-02-05 21:56:35 IST

Processes (PID | ELAPSED | COMMAND)
Process list unavailable (permission denied).

Logs
- live_ai_hybrid.log: MISSING (/Users/mac/openalgo/openalgo/live_ai_hybrid.log)
- live_banknifty.log: MISSING (/Users/mac/openalgo/openalgo/live_banknifty.log)
- live_nifty.log: MISSING (/Users/mac/openalgo/openalgo/live_nifty.log)
- AI_Hybrid_v1_RELIANCE_20260204.log: MISSING (/Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log)


---
Snapshot @ 2026-02-05 22:56:31 IST

Strategy processes (pid, elapsed seconds, command):
Process list unavailable: zsh:9: operation not permitted: ps

Log missing: /Users/mac/openalgo/openalgo/live_ai_hybrid.log

Log missing: /Users/mac/openalgo/openalgo/live_banknifty.log

Log missing: /Users/mac/openalgo/openalgo/live_nifty.log

Log missing: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log


-----
Snapshot @ 2026-02-05 23:56:34 IST

Strategy processes (pid, elapsed, command):
Process list unavailable: zsh:1: operation not permitted: ps

Logs (last 5 lines):
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log: missing
- /Users/mac/openalgo/openalgo/live_banknifty.log: missing
- /Users/mac/openalgo/openalgo/live_nifty.log: missing
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing

---

Timestamp (IST): 2026-02-06 00:56:36 IST

Strategy processes (PID / uptime / command):
- Unable to read process list (ps: operation not permitted).

Log tails (last 5 lines):

live_ai_hybrid.log:
- Missing log file at /Users/mac/openalgo/openalgo/live_ai_hybrid.log

live_banknifty.log:
- Missing log file at /Users/mac/openalgo/openalgo/live_banknifty.log

live_nifty.log:
- Missing log file at /Users/mac/openalgo/openalgo/live_nifty.log

log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
- Missing log file at /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log

---

Timestamp (IST): 2026-02-06 01:56:48 IST

Processes (PIDs + uptime):
- Unable to read process list (ps not permitted).

Logs (last 5 lines):
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log: missing
- /Users/mac/openalgo/openalgo/live_banknifty.log: missing
- /Users/mac/openalgo/openalgo/live_nifty.log: missing
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing
---
Timestamp (IST): 2026-02-06 09:47:36 IST

Processes (PIDs + uptime):
- Unable to read process list (ps not permitted).

Logs (last 5 lines):

live_ai_hybrid.log:
- Missing log file at /Users/mac/openalgo/openalgo/live_ai_hybrid.log

live_banknifty.log:
- Missing log file at /Users/mac/openalgo/openalgo/live_banknifty.log

live_nifty.log:
- Missing log file at /Users/mac/openalgo/openalgo/live_nifty.log

AI_Hybrid_v1_RELIANCE_20260204.log:
- Missing log file at /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
-----
Timestamp (IST): 2026-02-06 10:46:15 IST

Strategy processes (PID / uptime / command):
- Unable to read process list (ps not permitted).

Logs (last 5 lines):

live_ai_hybrid.log:
- Missing log file at /Users/mac/openalgo/openalgo/live_ai_hybrid.log

live_banknifty.log:
- Missing log file at /Users/mac/openalgo/openalgo/live_banknifty.log

live_nifty.log:
- Missing log file at /Users/mac/openalgo/openalgo/live_nifty.log

AI_Hybrid_v1_RELIANCE_20260204.log:
- Missing log file at /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log

---
Snapshot @ 2026-02-06 15:54:33 IST

Processes (strategy scripts):
- Unable to read process list (ps not permitted in this environment).

Logs (last 5 lines each):
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log (missing)
- /Users/mac/openalgo/openalgo/live_banknifty.log (missing)
- /Users/mac/openalgo/openalgo/live_nifty.log (missing)
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log (missing)

---

Snapshot @ 2026-02-06 16:54:22 IST

Processes (PID | uptime | command):
Process listing unavailable: zsh:7: operation not permitted: ps 

Log: live_ai_hybrid.log (/Users/mac/openalgo/openalgo/live_ai_hybrid.log)

Missing log file.

Log: live_banknifty.log (/Users/mac/openalgo/openalgo/live_banknifty.log)

Missing log file.

Log: live_nifty.log (/Users/mac/openalgo/openalgo/live_nifty.log)

Missing log file.

Log: AI_Hybrid_v1_RELIANCE_20260204.log (/Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log)

Missing log file.

---
Snapshot: 2026-02-06 17:54:35 IST

Processes (PIDs + uptime):
- Unable to list processes (ps permission restriction in sandbox).

Log tail: /Users/mac/openalgo/openalgo/live_ai_hybrid.log
- Missing

Log tail: /Users/mac/openalgo/openalgo/live_banknifty.log
- Missing

Log tail: /Users/mac/openalgo/openalgo/live_nifty.log
- Missing

Log tail: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
- Missing

---
Snapshot @ 2026-02-06 21:01:00 IST

Processes (PID | uptime | command):
- Unable to read process list (ps error: zsh:9: operation not permitted: ps)

Logs (last 5 lines):

live_ai_hybrid.log [/Users/mac/openalgo/openalgo/live_ai_hybrid.log]:
- Missing log file

live_banknifty.log [/Users/mac/openalgo/openalgo/live_banknifty.log]:
- Missing log file

live_nifty.log [/Users/mac/openalgo/openalgo/live_nifty.log]:
- Missing log file

AI_Hybrid_v1_RELIANCE_20260204.log [/Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log]:
- Missing log file


---

Snapshot: 2026-02-06 22:00:39 IST

Processes:
No matching strategy processes found (ps/rg returned none or restricted).

Log tails (last 5 lines):

/Users/mac/openalgo/openalgo/live_ai_hybrid.log:
Missing log file.

/Users/mac/openalgo/openalgo/live_banknifty.log:
Missing log file.

/Users/mac/openalgo/openalgo/live_nifty.log:
Missing log file.

/Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
Missing log file.

---

Snapshot: 2026-02-06 22:00:48 IST

Processes:
Process listing unavailable (ps error: zsh:12: operation not permitted: ps).

Log tails (last 5 lines):

/Users/mac/openalgo/openalgo/live_ai_hybrid.log:
Missing log file.

/Users/mac/openalgo/openalgo/live_banknifty.log:
Missing log file.

/Users/mac/openalgo/openalgo/live_nifty.log:
Missing log file.

/Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
Missing log file.

---

Snapshot: 2026-02-06 23:00:46 IST

Processes:
Process listing unavailable (ps error: zsh:1: operation not permitted: ps).

Log tails (last 5 lines):

/Users/mac/openalgo/openalgo/live_ai_hybrid.log:
Missing log file.

/Users/mac/openalgo/openalgo/live_banknifty.log:
Missing log file.

/Users/mac/openalgo/openalgo/live_nifty.log:
Missing log file.

/Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log:
Missing log file.

---

Timestamp (IST): 2026-02-07 00:00:35 IST

Strategy processes (PID, uptime, command):
- ps unavailable ("operation not permitted")

Logs (last 5 lines):
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log: MISSING
- /Users/mac/openalgo/openalgo/live_banknifty.log: MISSING
- /Users/mac/openalgo/openalgo/live_nifty.log: MISSING
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: MISSING

---

## Snapshot - 2026-02-07 01:00:39 IST

### Strategy Processes (PID, Uptime, Command)
Process list unavailable (ps error):
zsh:8: operation not permitted: ps

### Log Tails (last 5 lines)

#### /Users/mac/openalgo/openalgo/live_ai_hybrid.log
Missing log file.

#### /Users/mac/openalgo/openalgo/live_banknifty.log
Missing log file.

#### /Users/mac/openalgo/openalgo/live_nifty.log
Missing log file.

#### /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
Missing log file.
---
## Snapshot @ 2026-02-09 15:07:10 IST

### Strategy processes (PID / Uptime / Command)
ps error: zsh:7: operation not permitted: ps

### Log tails (last 5 lines)

#### /Users/mac/openalgo/openalgo/live_ai_hybrid.log
Missing log file.

#### /Users/mac/openalgo/openalgo/live_banknifty.log
Missing log file.

#### /Users/mac/openalgo/openalgo/live_nifty.log
Missing log file.

#### /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
Missing log file.

---
Timestamp (IST): 2026-02-09 16:07:11 IST

Processes (strategy scripts):
- Unavailable: unable to access process list in sandbox (ps/pgrep blocked).

Logs (last 5 lines):
- live_ai_hybrid.log: MISSING
- live_banknifty.log: MISSING
- live_nifty.log: MISSING
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: MISSING

---
Timestamp (IST): 2026-02-09 18:24:20 IST

Processes (strategy scripts):
- Unavailable: unable to access process list in sandbox (ps blocked).

Logs (last 5 lines):
- live_ai_hybrid.log: MISSING
- live_banknifty.log: MISSING
- live_nifty.log: MISSING
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: MISSING

---
Timestamp (IST): 2026-02-09 19:17:25 IST

Processes (strategy scripts):
- Unavailable: unable to access process list in sandbox (ps blocked).

Logs (last 5 lines):
- live_ai_hybrid.log: MISSING
- live_banknifty.log: MISSING
- live_nifty.log: MISSING
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: MISSING

---

## Snapshot - 2026-02-09 20:16:14 IST

### Strategy Processes (PID / Uptime)
- Unable to read process list (ps blocked by sandbox).

### Logs (last 5 lines)
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log: missing.
- /Users/mac/openalgo/openalgo/live_banknifty.log: missing.
- /Users/mac/openalgo/openalgo/live_nifty.log: missing.
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing.

---
Timestamp (IST): 2026-02-11 18:53:20 IST

Strategy processes (PID / uptime):
- Unable to read process list (ps not permitted in sandbox).

Logs (last 5 lines):
- live_ai_hybrid.log: missing
- live_banknifty.log: missing
- live_nifty.log: missing
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing

---

**Snapshot (IST):** 2026-02-11 19:52:56 IST

**Strategy processes (PID / uptime / command):**
- Unable to read process list (ps not permitted in sandbox).

**Logs (last 5 lines):**
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log: missing
- /Users/mac/openalgo/openalgo/live_banknifty.log: missing
- /Users/mac/openalgo/openalgo/live_nifty.log: missing
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing

---

## Snapshot - 2026-02-11 21:54:02 IST

Process status:
- Unable to read process list (ps not permitted in sandbox), so PIDs/uptimes unavailable.

Logs (last 5 lines each):
- live_ai_hybrid.log: missing
- live_banknifty.log: missing
- live_nifty.log: missing
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing

---

## Snapshot - 2026-02-12 09:03:37 IST

Process status:
- Unable to read process list (ps not permitted in sandbox), so PIDs/uptimes unavailable.

Logs (last 5 lines each):
- live_ai_hybrid.log: missing
- live_banknifty.log: missing
- live_nifty.log: missing
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing

---

## Snapshot - 2026-02-12 11:03:22 IST

**Processes (strategy scripts)**

- Process list unavailable in sandbox (ps not permitted).

**Logs (last 5 lines)**

- live_ai_hybrid.log: MISSING

- live_banknifty.log: MISSING

- live_nifty.log: MISSING

- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: MISSING


---

## Snapshot - 2026-02-12 12:03:47 IST

### Strategy Processes (PID / Uptime)
- Unable to read process list (ps not permitted in sandbox).

### Logs (last 5 lines)
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log: missing.
- /Users/mac/openalgo/openalgo/live_banknifty.log: missing.
- /Users/mac/openalgo/openalgo/live_nifty.log: missing.
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing.
---
Timestamp (IST): 2026-02-12 13:03:37 IST

Processes (strategy scripts):
- Unable to list processes (ps not permitted in sandbox).

Logs (last 5 lines):
- live_ai_hybrid.log: MISSING
- live_banknifty.log: MISSING
- live_nifty.log: MISSING
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: MISSING

---
Timestamp (IST): 2026-02-12 14:03:33 IST

Strategy processes (PID, uptime, command):
- Unavailable (ps not permitted in sandbox)

Logs (last 5 lines):
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log: missing
- /Users/mac/openalgo/openalgo/live_banknifty.log: missing
- /Users/mac/openalgo/openalgo/live_nifty.log: missing
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing

---
Timestamp (IST): 2026-02-12 15:03:24 IST

Strategy processes (PID, uptime, command):
- Unavailable (ps not permitted in sandbox)

Logs (last 5 lines):
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log: missing
- /Users/mac/openalgo/openalgo/live_banknifty.log: missing
- /Users/mac/openalgo/openalgo/live_nifty.log: missing
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing

---
Snapshot @ 2026-02-12 16:03:29 IST

Processes:
- Process list unavailable (ps not permitted in sandbox).

Logs:
- live_ai_hybrid.log: missing
- live_banknifty.log: missing
- live_nifty.log: missing
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing

---

Snapshot: 2026-02-12 17:03:37 IST

Processes (PID | Uptime | Command):
 - Missing: no matching strategy processes found

Logs (last 5 lines):
 - live_ai_hybrid.log: Missing (file not found: /Users/mac/openalgo/openalgo/live_ai_hybrid.log)
 - live_banknifty.log: Missing (file not found: /Users/mac/openalgo/openalgo/live_banknifty.log)
 - live_nifty.log: Missing (file not found: /Users/mac/openalgo/openalgo/live_nifty.log)
 - AI_Hybrid_v1_RELIANCE_20260204.log: Missing (file not found: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log)

---

Snapshot: 2026-02-12 17:03:50 IST

Processes (PID | Uptime | Command):
 - Unavailable: process listing blocked in sandbox (ps not permitted)

Logs (last 5 lines):
 - live_ai_hybrid.log: Missing (file not found: /Users/mac/openalgo/openalgo/live_ai_hybrid.log)
 - live_banknifty.log: Missing (file not found: /Users/mac/openalgo/openalgo/live_banknifty.log)
 - live_nifty.log: Missing (file not found: /Users/mac/openalgo/openalgo/live_nifty.log)
 - AI_Hybrid_v1_RELIANCE_20260204.log: Missing (file not found: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log)
---
Timestamp (IST): 2026-02-12 18:03:35 IST

Strategy processes (PID | Uptime | Command):
- UNAVAILABLE: process listing blocked by sandbox (ps)

Log tails (last 5 lines):
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log: MISSING
- /Users/mac/openalgo/openalgo/live_banknifty.log: MISSING
- /Users/mac/openalgo/openalgo/live_nifty.log: MISSING
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: MISSING
---
Timestamp (IST): 2026-02-12 19:03:48 IST

Strategy processes (PID | Uptime | Command):
- UNAVAILABLE: process listing blocked by sandbox (ps)

Log tails (last 5 lines):
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log: MISSING
- /Users/mac/openalgo/openalgo/live_banknifty.log: MISSING
- /Users/mac/openalgo/openalgo/live_nifty.log: MISSING
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: MISSING
Timestamp: 2026-02-12 20:04:00 IST

Processes (PID | uptime(s) | command):
(Process list unavailable: zsh:10: operation not permitted: ps)

Log: live_ai_hybrid.log
(Missing: /Users/mac/openalgo/openalgo/live_ai_hybrid.log)

Log: live_banknifty.log
(Missing: /Users/mac/openalgo/openalgo/live_banknifty.log)

Log: live_nifty.log
(Missing: /Users/mac/openalgo/openalgo/live_nifty.log)

Log: log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
(Missing: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log)

---

---
Timestamp (IST): 2026-02-12 21:03:49 IST

Strategy processes (PID, uptime, command):
- Unable to read process list (ps not permitted in this environment).

Logs:
- live_ai_hybrid.log: missing
- live_banknifty.log: missing
- live_nifty.log: missing
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing

---

## Snapshot 2026-02-12 22:03:35 IST

### Strategy Processes
- Process list unavailable (ps not permitted in this environment).

### Logs (last 5 lines)
- live_ai_hybrid.log: missing
- live_banknifty.log: missing
- live_nifty.log: missing
- log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: missing
---
Snapshot: 2026-02-12 23:45:15 IST

Processes (PID ETIME COMMAND):
(process listing failed: zsh:7: operation not permitted: ps)

--- /Users/mac/openalgo/openalgo/live_ai_hybrid.log (missing)
--- /Users/mac/openalgo/openalgo/live_banknifty.log (missing)
--- /Users/mac/openalgo/openalgo/live_nifty.log (missing)
--- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log (missing)


---
Timestamp (IST): 2026-02-13 00:45:57 IST

Strategy processes (PID / uptime):
- MISSING: process list unavailable (ps: operation not permitted).

Log tails (last 5 lines):
- /Users/mac/openalgo/openalgo/live_ai_hybrid.log: MISSING
- /Users/mac/openalgo/openalgo/live_banknifty.log: MISSING
- /Users/mac/openalgo/openalgo/live_nifty.log: MISSING
- /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log: MISSING

---

## Snapshot 2026-02-13 01:44:55 IST

### Strategy Processes (PID / Uptime / Command)
- Missing: unable to read process list (`ps` permission error).

### Logs (last 5 lines)
`live_ai_hybrid.log`
- Missing: /Users/mac/openalgo/openalgo/live_ai_hybrid.log

`live_banknifty.log`
- Missing: /Users/mac/openalgo/openalgo/live_banknifty.log

`live_nifty.log`
- Missing: /Users/mac/openalgo/openalgo/live_nifty.log

`log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log`
- Missing: /Users/mac/openalgo/openalgo/log/strategies/AI_Hybrid_v1_RELIANCE_20260204.log
