#!/bin/bash
# Quick strategy monitoring script (updated with time-filtered errors)

echo "=== Strategy Fleet Status ==="
echo "Time: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

echo "📊 Running Processes:"
ps aux | grep "strategies/scripts" | grep -v grep | wc -l
echo ""

echo "💾 Resource Usage:"
ps aux | grep "strategies/scripts" | grep -v grep | \
awk '{mem+=$6; cpu+=$3} END {printf "Memory: %.2f MB | CPU: %.2f%%\n", mem/1024, cpu}'
echo ""

echo "📈 Recent Trades (Last 10):"
grep -h "event=trade" live_*.log 2>/dev/null | tail -10
echo ""

echo "⚠️  Recent Errors (Last 30 min):"
find live_*.log -mmin -30 -exec grep -h "ERROR\|Exception" {} \; 2>/dev/null | grep -v "Input_Exception" | tail -5
if [ $? -ne 0 ]; then
    echo "No recent errors"
fi

echo ""
echo "🧩 Recent Broker Input Errors (tail):"
tail -n 300 live_session_app.log app_output_final.log 2>/dev/null | grep "Input_Exception" | tail -5
if [ $? -ne 0 ]; then
    echo "No recent Input_Exception"
fi
