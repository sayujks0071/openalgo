# 31 - FastScalper NIFTY & BANKNIFTY Options – Intraday Scalping Playbook

## 1. Overview

FastScalper is a lightweight Rust-based desktop app that connects directly to your OpenAlgo instance and is designed for **manual, keyboard-driven scalping**.

This playbook shows **how to use FastScalper specifically for NIFTY & BANKNIFTY weekly options**, with:

- **Clear environment setup** (OpenAlgo + FastScalper)
- **Suggested layouts** for Windows, macOS and Linux
- **Risk framework** for intraday options
- **Concrete entry/exit rules** for NIFTY and BANKNIFTY
- **Practical use of L / LX / SE / SX and voice alerts**

> ⚠️ This is a **trading workflow guide**, not a recommendation or guarantee of profit. Always start in low quantity and Analyzer Mode where possible.

---

## 2. Environment Setup – OpenAlgo + FastScalper

### 2.1 Prerequisites

- A running **OpenAlgo** instance (local or on VPS)
- At least one **supported broker** with F&O enabled
- **API key** generated from OpenAlgo (`/apikey`)
- **FastScalper Desktop** installed for your OS (from the **Download** section in the React frontend)

### 2.2 OpenAlgo configuration

1. **Install & run OpenAlgo**
   - Follow the main [Installation Guide](../04-installation/README.md).
   - Confirm OpenAlgo is reachable at your chosen host (e.g. `http://127.0.0.1:5000`).
2. **Connect your broker**
   - Complete [Broker Connection](../06-broker-connection/README.md).
   - Log in to your broker and confirm you can place at least one small test order.
3. **Generate API key**
   - Go to the **API Key Management** page.
   - Create an API key and store it securely – you will use this in FastScalper.

### 2.3 FastScalper configuration

In FastScalper **Settings**:

- **API Key**: Paste the key generated in OpenAlgo.
- **Host URL**: Use your OpenAlgo URL, for example:
  - Local machine: `http://127.0.0.1:5000`
  - VPS / Cloud: `https://your-server-or-domain`
- **Exchange / Product defaults**:
  - Exchange: typically `NFO` for index options.
  - Product: **`MIS`** for **intraday-only** scalping.

Save settings and verify:

- Place a **very small test order** in a cheap option (or Analyzer Mode) using `L` and then close with `LX`.
- Confirm the order and position appear correctly in:
  - OpenAlgo **Dashboard / Orderbook / Positions**
  - Your **broker terminal** (web / mobile)

---

## 3. Layout & Workflow by Operating System

FastScalper is meant to be used **alongside your charting platform** (TradingView, GoCharting, etc.).

### 3.1 Windows – Recommended Multi-Instance Setup

- Run **two FastScalper instances**:
  - **Instance A – NIFTY Options**
  - **Instance B – BANKNIFTY Options**
- Place them side-by-side with your charts:
  - Left: NIFTY futures/index chart + FastScalper (NIFTY options)
  - Right: BANKNIFTY futures/index chart + FastScalper (BANKNIFTY options)
- Each instance is “locked” to **one underlying**:
  - Only change **strike / expiry / quantity** inside each instance.

**Benefits**:

- No symbol confusion (NIFTY vs BANKNIFTY).
- Both markets are always visible, with **one-key execution** (`L`, `LX`) per side.

### 3.2 macOS / Linux – Single-Instance Setup

macOS and Linux currently support **one FastScalper instance at a time**:

- Use a **single FastScalper window**.
- Keep **two charts** open in your charting tool:
  - NIFTY on left, BANKNIFTY on right.
- In FastScalper:
  - Switch between **NIFTY options** and **BANKNIFTY options** by changing the symbol/strike.

**Tip**: Focus on **one index at a time** until you are comfortable with the workflow.

---

## 4. NIFTY & BANKNIFTY Option Selection Rules

This playbook assumes you are trading **weekly index options**.

### 4.1 Strike selection

- Prefer **ATM or near-ATM** strikes:
  - NIFTY: within **±1 strike** of spot (e.g. 50-point steps).
  - BANKNIFTY: within **±1–2 strikes** of spot (e.g. 100-point steps).
- Choose strikes with:
  - Tight **bid–ask spread**
  - Consistent **volume / open interest**

### 4.2 Expiry selection

- Early in the week (Mon–Wed):
  - Trade the **current week** expiry.
- Last day of the week (expiry day) or when time decay is extreme:
  - Consider **next week** expiry for smoother pricing.

### 4.3 Symbol format reminder

OpenAlgo uses standard symbol format, e.g.:

```text
NFO:NIFTY30JAN2521500CE
NFO:BANKNIFTY30JAN2550100PE
```

For full details, see the [Symbol Format Guide](../symbol-format/README.md).

---

## 5. Risk Management & Position Sizing

### 5.1 Define per-trade risk

Start by deciding **how much you can lose per trade**:

- Suggested: **0.25–0.5% of account equity per trade**
- Example (₹5,00,000 account):
  - 0.5% per trade → **₹2,500 risk** per trade

### 5.2 Derive quantity from stop size

Estimate a **typical stop distance** on the option premium (in rupees). For example:

- NIFTY option: 10–15 points
- BANKNIFTY option: 20–30 points

Then compute:

```text
quantity = floor(per_trade_risk / option_stop_size)
```

Examples:

- NIFTY: ₹2,500 risk, 12-point stop → `floor(2500 / 12) ≈ 200` quantity
- BANKNIFTY: ₹2,500 risk, 25-point stop → `floor(2500 / 25) = 100` quantity

### 5.3 Daily loss cap

Set a **max daily loss** and strictly stop trading at that point:

- Suggested: **1–2% of account** per day
- Example: ₹5,00,000 account → max daily loss **₹5,000–10,000**

### 5.4 Scaling

At the beginning:

- Trade **single-unit size** (no scale-in) until you are comfortable.
- Later, you can scale:
  - Add with `L` again **only when the trade is in profit**.
  - Always stay within your daily loss cap.

---

## 6. NIFTY Options – Intraday Scalping Rules

These rules assume you are using **1–3 minute charts** for entries and **VWAP / short EMA** for trend context.

### 6.1 Time windows

- Avoid first **5–10 minutes** after open (too volatile, wide spreads).
- Focus on:
  - **09:25–11:30**
  - **13:30–15:00**

### 6.2 Long call (CE) scalps

**Conditions (charts, not FastScalper):**

- Price trades **above intraday VWAP**.
- Short-term trend is bullish:
  - Higher highs / higher lows on 1–3 minute chart, and/or
  - Close above a fast EMA (e.g. 9 EMA).

**Execution (FastScalper):**

1. Select a **NIFTY ATM or slightly ITM CE** for the current/next week.
2. Set quantity based on your risk formula.
3. When conditions align:
   - Press **`L`** to enter long.
4. Manage the trade:
   - Use a **fixed stop** on the option premium (e.g. 10–15 points).
   - Press **`LX`** to exit when:
     - Target is hit (e.g. 20–30% premium move), or
     - Price closes back below VWAP / key short-term support, or
     - A predefined **time stop** (e.g. 5–10 minutes without follow-through) is reached.

### 6.3 Long put (PE) scalps

Mirror the above logic for **downtrend**:

- Price trades **below VWAP**.
- Lower highs / lower lows on 1–3 minute chart.
- Select **NIFTY ATM/ITM PE**.
- Use `L` to enter long put and `LX` to exit.

### 6.4 Trend alignment filter

- Use a **15-minute chart** to define the larger trend.
- Prefer scalps **in the direction of the 15-minute trend**.
- Avoid aggressive counter-trend trades when the 15-minute trend is very strong.

---

## 7. BANKNIFTY Options – Intraday Scalping Rules

BANKNIFTY options are generally **more volatile** than NIFTY:

- Use **smaller quantity** or **wider stops** than you use for NIFTY.

### 7.1 Trend scalps

**Conditions:**

- Clean trend on **3–5 minute chart**:
  - Series of higher highs / higher lows (for longs), or
  - Series of lower highs / lower lows (for shorts).
- Price vs VWAP similar to NIFTY rules.

**Execution:**

1. In the BANKNIFTY FastScalper instance:
   - Select **BANKNIFTY ATM CE / PE** depending on direction.
2. Confirm spreads and liquidity.
3. Use **`L`** to enter and **`LX`** to exit according to:
   - Premium stop (e.g. 25–30 points).
   - Trend breaks (close beyond key levels).
   - Time-based exit if momentum stalls.

### 7.2 Optional: Mean-reversion micro-scalps (advanced)

Once you are consistent:

- Consider **small-size contrarian scalps** near strong intraday support/resistance.
- Rules should be stricter:
  - Only trade when strong levels from higher timeframes (e.g. daily/1-hour) align.
  - Use **tighter premium stops** and faster exits.

---

## 8. Using FastScalper Hotkeys & Voice Alerts Effectively

### 8.1 Hotkey mapping

- **`L`** – Place a **long order** in the selected instrument (e.g. NIFTY CE/PE, BANKNIFTY CE/PE).
- **`LX`** – **Close long positions** (partial or full, depending on your quantity setting).
- **`SE`** – Place a **short order** (for instruments that support it; optional for options).
- **`SX`** – **Close short positions**.

For the NIFTY/BANKNIFTY options playbook:

- Start with **`L` and `LX` only** for long calls and long puts.
- Introduce `SE`/`SX` later if you add other instruments or synthetic shorting.

### 8.2 Voice alerts

Voice alerts help you **keep eyes on the charts** while still getting confirmation:

- Enable voice alerts for:
  - **Order placement** (L / SE)
  - **Order exit** (LX / SX)
- Keep them **short and minimal** so they do not distract you during fast markets.

Examples:

- “NIFTY CE long executed”
- “BANKNIFTY PE exit filled”

If you mis-press `LX`/`SX` when no position exists, FastScalper will **safely ignore invalid closes**, reducing error risk.

---

## 9. Operating Checklists

### 9.1 Pre-market checklist

- OpenAlgo is **running** and reachable at your Host URL.
- Broker is **logged in** and shows correct margin.
- FastScalper:
  - Correct **API Key** and **Host URL** configured.
  - Default **exchange** (NFO) and **product** (MIS) set.
  - Test order (tiny quantity) verified at least once for the day.
- Charts:
  - NIFTY and BANKNIFTY charts open with VWAP + EMAs configured.

### 9.2 Per-trade checklist

- Right **underlying** (NIFTY vs BANKNIFTY).
- Right **strike & expiry**.
- **Quantity** matches your risk rules.
- **Bid–ask spread** within your acceptable limit.
- Trend and VWAP conditions satisfied on your entry timeframe.
- Hands on keyboard, ready to press `L` (entry) and `LX` (exit).

### 9.3 Post-session checklist

- Export or review **order / trade logs** from OpenAlgo.
- Tag trades:
  - NIFTY trend scalp, NIFTY mean reversion (if used), BANKNIFTY trend, etc.
- Check:
  - Were risk limits respected?
  - Did you stop at your **daily loss cap**?
  - Are your stop sizes and targets appropriate for current volatility?

---

## 10. Recommended Progression

1. **Phase 1 – 1-lot / minimum size**
   - Trade only **one instrument** (e.g. NIFTY) in minimal size.
   - Focus on **executing the plan** and honoring stops and daily loss caps.
2. **Phase 2 – Full normal size**
   - Scale quantity to your full risk-based size once execution is smooth.
3. **Phase 3 – Advanced variations**
   - Add BANKNIFTY trend scalps.
   - Add controlled scaling in/out with repeated `L` / `LX`.
   - Integrate OpenAlgo signals (e.g. trend filters) as confirmation, while keeping actual entries/ exits manual via FastScalper.

---

**Next steps**:

- Make sure you are fully comfortable with the [Order Types Explained](../11-order-types/README.md) module.
- Practice the workflow for several sessions in **small size** before increasing risk.

