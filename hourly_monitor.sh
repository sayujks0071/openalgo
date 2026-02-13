#!/bin/bash
# Hourly strategy monitoring with timestamped reports

REPORT_DIR="/Users/mac/openalgo/openalgo/overnight_reports"
DATE=$(date '+%Y-%m-%d')
TIME=$(date '+%H:%M:%S')
REPORT_FILE="${REPORT_DIR}/overnight_status_${DATE}.md"

# Create report directory if it doesn't exist
mkdir -p "$REPORT_DIR"

# Initialize report if it's the first entry of the day
if [ ! -f "$REPORT_FILE" ]; then
    cat > "$REPORT_FILE" << 'HEADER'
# Overnight Strategy Monitoring Report

**Date**: $(date '+%Y-%m-%d')  
**Fleet**: 14 Strategies (5 NSE Stocks + 4 Originals + 5 Option Chain)

---

HEADER
fi

# Append hourly update
cat >> "$REPORT_FILE" << ENTRY

## Update: ${TIME}

**Processes**: $(ps aux | grep "strategies/scripts" | grep -v grep | wc -l | tr -d ' ')  
**Memory**: $(ps aux | grep "strategies/scripts" | grep -v grep | awk '{mem+=$6} END {printf "%.2f MB", mem/1024}')  
**CPU**: $(ps aux | grep "strategies/scripts" | grep -v grep | awk '{cpu+=$3} END {printf "%.2f%%", cpu}')

### Trades (Last Hour)
\`\`\`
$(grep -h "event=trade" live_*.log 2>/dev/null | tail -n 20 | head -10 || echo "No trades")
\`\`\`

### Recent Errors (Last 30 min)
\`\`\`
$(find live_*.log -mmin -30 -exec grep -h "ERROR\|Exception" {} \; 2>/dev/null | tail -5 || echo "No recent errors")
\`\`\`

ENTRY

echo "✅ Report updated: $REPORT_FILE"
