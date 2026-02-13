## 2026-02-04 21:10:25 IST
- Running processes: 0 (monitor noted /bin/ps permission denied)
- CPU/Memory: 0.00% / 0.00 MB
- Recent trades (last 10): none
- Recent errors (last 30 min): none reported by monitor
- DH-905 counts: app_output_final.log=12, live_session_app.log=129
- Latest DH-905 context:
  - live_session_app.log @ 2026-02-04 15:29:41: /v2/charts/intraday request returned 400 Input_Exception (payload for securityId 1333, NSE_EQ, interval 1, 2026-02-02..2026-02-04, oi=true). Quotes request after that succeeded.
  - app_output_final.log @ 2026-02-04 09:47:36: order_api place_smart_order failed 400 Input_Exception; nearby logs show rate limit exceeded and repeated order attempts.
- Diagnosis: likely invalid/missing request fields or unsupported parameter combo for intraday history and order placement; verify required params/payload schema and rate-limit/backoff behavior.

## 2026-02-04 22:10:21 IST
- Running processes: 0
- Resource usage: Memory 0.00 MB | CPU 0.00%
- Recent trades (last 10): none
- Recent errors (last 30 min): none
- Script warnings: /bin/ps Operation not permitted (2 occurrences)
- Input_Exception/DH-905 count: app_output_final.log=12, live_session_app.log=257
- Latest DH-905 context (live_session_app.log @ 2026-02-04 15:29:41): intraday history request to /v2/charts/intraday returned 400 for NSE_EQ securityId 1333 (fromDate 2026-02-02 toDate 2026-02-04), followed by quote fetch.
- Latest DH-905 context (app_output_final.log @ 2026-02-04 09:47:36): order_api place_smart_order 400 Input_Exception DH-905, near rate-limit notices.

## 2026-02-04 23:10:15 IST
- Running processes: 0
- Resource usage: 0.00 MB | 0.00% CPU
- Recent trades: none
- Recent errors (30m): none
- Script warnings: /bin/ps Operation not permitted
- DH-905 counts: app_output_final.log=12, live_session_app.log=257
- Latest DH-905 context (app_output_final.log 09:47:36): order_api place_smart_order 400 after position_size/open position logs.
- Latest DH-905 context (live_session_app.log 15:29:41): /v2/charts/intraday request 400 for securityId 1333, NSE_EQ, interval 1, fromDate 2026-02-02, toDate 2026-02-04.
- Diagnosis: DH-905 indicates missing/invalid parameters in order placement and intraday history payloads; check required fields and date/securityId validity.

## 2026-02-04 23:10:51 IST
- Running processes: 0
- CPU: 0.00% | Memory: 0.00 MB
- Recent trades (last 10): none
- Recent errors (last 30 min): none
- Broker Input_Exception/DH-905 counts: app_output_final.log=12, live_session_app.log=129
- monitor_strategies.sh warnings: /bin/ps Operation not permitted (lines 9, 13)
- DH-905 latest context (live_session_app.log @ 15:29:41): intraday history request to /v2/charts/intraday returned 400 Input_Exception DH-905 for NSE_EQ securityId 1333 (date range 2026-02-02..2026-02-04)
- DH-905 latest context (app_output_final.log @ 09:47:36): order_api place_smart_order 400 Input_Exception DH-905 after symbol token 2885 lookup warnings

## 2026-02-04 23:11:22 IST
- Running processes: 0
- Resource usage: 0.00 MB | 0.00% CPU
- Recent trades (last 10): none
- Recent errors (last 30 min): none
- DH-905/Input_Exception counts: app_output_final.log=12, live_session_app.log=129
- Notes: monitor_strategies.sh reported /bin/ps Operation not permitted warnings
- Latest DH-905 context (app_output_final.log): 2026-02-04 09:47:36 order_api 400 after rate-limit log at 09:47:28
- Latest DH-905 context (live_session_app.log): 2026-02-04 15:29:41 intraday history request 400 (securityId 1333, interval 1, 2026-02-02..2026-02-04), followed by quotes fallback 200
