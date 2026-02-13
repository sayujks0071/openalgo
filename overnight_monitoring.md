# Overnight Monitoring Guide (24/7 Dhan Sandbox)

This guide shows how to monitor strategy health, logs, and common errors during overnight stress tests.

## Quick Check
Run the monitoring script:

```bash
cd /Users/mac/openalgo/openalgo
./monitor_strategies.sh
```

What it shows:
- Running process count
- Total CPU and memory use
- Last 10 trade events
- Recent error lines from live logs
- Tail of broker Input_Exception messages

## Log Locations
- Strategy live logs: `live_*.log`
- Backend log: `live_session_app.log`
- Legacy backend log: `app_output_final.log`
- Trade ledgers (CSV): `log/strategies/trades/*.csv`

## Common Issues and Fixes

### Input_Exception (DH-905)
Cause:
- Master contracts not ready or symbol mapping missing.

Fix:
1. Trigger master contract download (re-login or run the download task).
2. Reload the symbol cache.
3. Recheck `monitor_strategies.sh` for new errors.

### Marketfeed 404
Cause:
- Dhan sandbox quote endpoint may return 404 for some instruments.

Fix:
- Usually safe to ignore in sandbox. Data will fall back to charts API.

### Stale Data / Flat Price
Cause:
- Sandbox candles not updating.

Fix:
- Wait for new data or reduce strategy cadence.
- Ensure master contracts and cache are loaded.

## Process Control

Check running strategy PIDs:

```bash
ps aux | grep "strategies/scripts" | grep -v grep
```

Stop a specific strategy:

```bash
kill <PID>
```

Stop all strategies (use with care):

```bash
ps aux | grep "strategies/scripts" | awk '{print $2}' | xargs kill
```

## Daily Review

Recommended morning checks:
1. Review `log/strategies/trades/*.csv` for trade count and PnL.
2. Review `live_*.log` for errors or repeated skips.
3. Confirm backend errors are not accumulating.

## Notes
- Strategies are configured to avoid over-trading on stale data.
- SL/TP and time-stop exits are enabled across all strategies.
- Position reconciliation runs periodically to prevent drift.
