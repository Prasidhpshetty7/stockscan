# 🎬 What Actually Happens When You Run StockScan

## Step 1: Download and Setup

1. Download `stockscan.py` to your computer
2. Open terminal/command prompt
3. Navigate to where you saved the file
4. Run: `pip install requests` (one-time setup)

---

## Step 2: Run StockScan

**Option A - Navigate to folder first (Recommended):**
```bash
cd stockscan
python stockscan.py
```

**Option B - Run from parent folder:**

Windows:
```bash
python stockscan\stockscan.py
```

Mac/Linux:
```bash
python stockscan/stockscan.py
```

**Note:** If `python` doesn't work, try `py` instead (common on Windows)

---

## Step 3: You See This Beautiful Banner

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║  ███████╗████████╗ ██████╗  ██████╗██╗  ██╗███████╗ ██████╗ █████╗ ███╗   ██╗ ║
║  ██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║ ║
║  ███████╗   ██║   ██║   ██║██║     █████╔╝ ███████╗██║     ███████║██╔██╗ ██║ ║
║  ╚════██║   ██║   ██║   ██║██║     ██╔═██╗ ╚════██║██║     ██╔══██║██║╚██╗██║ ║
║  ███████║   ██║   ╚██████╔╝╚██████╗██║  ██╗███████║╚██████╗██║  ██║██║ ╚████║ ║
║  ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

                       Market Price Lookup Tool
                   Get crypto & stock prices at any time


What is StockScan?
  StockScan lets you look up the exact price of any crypto or stock
  at a specific date and time using OHLCV candle logic.

How it works:
  • Fetches OHLCV (Open, High, Low, Close, Volume) candle data
  • Finds the candle that CONTAINS your requested time
  • Returns the CLOSE price as the price at that time
  • This is the standard method used by professional trading tools

Data Sources:
  • Crypto: Binance (1000+ coins, NO API KEY NEEDED)
    - Supports: 16 timeframes from 1s to 1M
  • Stocks: Yahoo Finance (all US & Indian stocks, NO API KEY NEEDED)
    - Supports: 1d (daily), 1wk (weekly), 1mo (monthly)
    - Works out of the box!
```

---

## Step 4: Choose Your Market

You'll see this question:

```
──────────────────────────────────────────────────────────────────────
Which market do you want to check?

  [1] Stocks  (AAPL, TSLA, MSFT, etc.)
  [2] Crypto  (BTCUSDT, ETHUSDT, etc.)
  [Q] Quit

Enter your choice (1/2/Q): _
```

**What to do:**
- Type `1` and press Enter → Go to Stocks
- Type `2` and press Enter → Go to Crypto  
- Type `Q` and press Enter → Exit the program

---

## Path A: If You Chose Stocks (Pressed 1)

You'll see:

```
──────────────────────────────────────────────────────────────────────
STOCK PRICE LOOKUP

Syntax: <SYMBOL> <DATE>
Examples:
  AAPL 2026-01-15  (Apple)
  TSLA 2024-12-20  (Tesla)
  MSFT 2025-06-10  (Microsoft)

Date format: YYYY-MM-DD
Type 'back' to return to market selection

Enter stock lookup: _
```

**Example: Let's check Apple stock**

Type: `AAPL 2026-01-15` and press Enter

---

### Step 1: Select Timeframe

You'll see a timeframe selector:

```
──────────────────────────────────────────────────
SELECT TIMEFRAME

Available timeframes:
  [1]  1d   - Daily
  [2]  1wk  - Weekly
  [3]  1mo  - Monthly

Select timeframe (1-3): _
```

**Let's choose `1` for daily**

---

### Step 2: See the Result

You'll see:

```
──────────────────────────────────────────────────────────────────────
STOCKSCAN - STOCK PRICE LOOKUP
──────────────────────────────────────────────────────────────────────

ASSET:           AAPL
MARKET:          Stocks (Yahoo Finance)
REQUESTED DATE:  2026-01-15
TIMEFRAME:       Daily

Candle Date:    2026-01-15

CANDLE DATA:
  Open:   $260.65
  High:   $261.04
  Low:    $257.05
  Close:  $258.21  ← Price at that date    👈 THIS IS THE ANSWER!
  Volume: 39,388,600

PRICE MOVEMENT:
  Change:     -$2.44                       👈 Price went down
  Percentage: -0.94%                       👈 Lost 0.94%

Note: This uses OHLCV candle logic. The CLOSE price of the daily
      candle for your requested date is shown as the price.
      Price movement shows the change from Open to Close.

──────────────────────────────────────────────────────────────────────

Press Enter to check another stock, or type 'back' to change market
```

---

### Example: Weekly Timeframe

**Or choose `2` for weekly:**

```
──────────────────────────────────────────────────────────────────────
STOCKSCAN - STOCK PRICE LOOKUP
──────────────────────────────────────────────────────────────────────

ASSET:           AAPL
MARKET:          Stocks (Yahoo Finance)
REQUESTED DATE:  2024-01-15
TIMEFRAME:       Weekly

Candle Period:  2024-01-15 → 2024-01-21    👈 Full 7-day period
ℹ Note: This period has only 4 trading day(s) out of the full weekly timeframe.
   3 day(s) excluded due to weekends/holidays. Check dates beyond this period for continued data.

CANDLE DATA:
  Open:   $182.16
  High:   $191.95
  Low:    $180.30
  Close:  $191.56  ← Price at end of period
  Volume: 259,829,200

PRICE MOVEMENT:
  Change:     +$9.40                       👈 Price went up
  Percentage: +5.16%                       👈 Gained 5.16%

Note: This uses OHLCV candle logic. The CLOSE price of the candle
      for your requested period is shown as the price.
      Price movement shows the change from Open to Close.

──────────────────────────────────────────────────────────────────────

Press Enter to check another stock, or type 'back' to change market
```

---

### Advanced Usage (Optional)

**For advanced users:** You can skip the interactive prompt by providing the timeframe directly:

```
AAPL 2026-01-15 1wk
```

This will skip the timeframe selection and show the result directly.

---

**What to do next:**
- Press Enter → Check another stock
- Type `back` → Go back to market selection (choose crypto or quit)

---

## Path B: If You Chose Crypto (Pressed 2)

You'll see:

```
──────────────────────────────────────────────────────────────────────
CRYPTO PRICE LOOKUP

Syntax: <SYMBOL> <DATE>
Examples:
  BTCUSDT 2026-01-15
  ETHUSDT 2026-01-15
  BNBUSDT 2026-01-10

Date format: YYYY-MM-DD
Type 'back' to return to market selection

Enter crypto lookup: _
```

**Example: Let's check Bitcoin price**

Type: `BTCUSDT 2026-01-15` and press Enter

---

### Step 1: Select Timeframe

You'll see a timeframe selector:

```
──────────────────────────────────────────────────
SELECT TIMEFRAME

Available timeframes:
  [1]  1s   - 1 second
  [2]  1m   - 1 minute
  [3]  3m   - 3 minutes
  [4]  5m   - 5 minutes
  [5]  15m  - 15 minutes
  [6]  30m  - 30 minutes
  [7]  1h   - 1 hour
  [8]  2h   - 2 hours
  [9]  4h   - 4 hours
  [10] 6h   - 6 hours
  [11] 8h   - 8 hours
  [12] 12h  - 12 hours
  [13] 1d   - 1 day
  [14] 3d   - 3 days
  [15] 1w   - 1 week
  [16] 1M   - 1 month

Select timeframe (1-16): _
```

**Let's choose `7` for 1-hour candle**

---

### Step 2: Enter Start Time (For Intraday Timeframes Only)

Since we chose an intraday timeframe (under 1 day), you'll see:

```
──────────────────────────────────────────────────
ENTER START TIME

What time should the 1h timeframe start?

Format: HH:MM (24-hour format)
Range:  00:00 to 23:59
Example: 14:30, 09:15, 23:59

Enter start time (HH:MM): _
```

**Type: `14:39` and press Enter**

This means: "Show me the 1-hour candle starting at EXACTLY 14:39:00"

---

### Step 3: See the Result

You'll see:

```
──────────────────────────────────────────────────────────────────────
STOCKSCAN - CRYPTO PRICE LOOKUP
──────────────────────────────────────────────────────────────────────

ASSET:           BTCUSDT
MARKET:          Crypto (Binance)
REQUESTED TIME:  2026-01-15 14:39 UTC
TIMEFRAME:       1h

Candle Period:  2026-01-15 14:39 UTC → 2026-01-15 15:39 UTC    👈 EXACT timing!

CANDLE DATA:
  Open:   $96,643.01000000
  High:   $97,193.34000000
  Low:    $96,559.19000000
  Close:  $97,040.75000000  ← Price at that time    👈 THIS IS THE ANSWER!
  Volume: 1,029.78

PRICE MOVEMENT:
  Change:     +$397.74000000               👈 Price went up
  Percentage: +0.41%                       👈 Gained 0.41%

Note: This uses OHLCV candle logic. The CLOSE price of the candle
      containing your requested time is shown as the price.
      Price movement shows the change from Open to Close.

──────────────────────────────────────────────────────────────────────

Press Enter to check another crypto, or type 'back' to change market
```

**Notice:** The candle period is EXACTLY 14:39 → 15:39, not rounded to 14:00 → 15:00!

---

### Example: Midnight Crossing

**What if the timeframe crosses midnight?**

Let's say you choose:
- Date: `2026-01-15`
- Timeframe: `2h` (2 hours)
- Start time: `23:30`

You'll see:

```
──────────────────────────────────────────────────────────────────────
STOCKSCAN - CRYPTO PRICE LOOKUP
──────────────────────────────────────────────────────────────────────

ASSET:           BTCUSDT
MARKET:          Crypto (Binance)
REQUESTED TIME:  2026-01-15 23:30 UTC
TIMEFRAME:       2h

Candle Period:  2026-01-15 23:30 UTC → 2026-01-16 01:30 UTC

ℹ Note: Timeframe spans across two dates.
   Period includes: 30 minute(s) from 2026-01-15, 1 hour(s) 30 minute(s) from 2026-01-16

CANDLE DATA:
  Open:   $96,500.00000000
  High:   $96,800.00000000
  Low:    $96,400.00000000
  Close:  $96,750.00000000  ← Price at that time
  Volume: 850.45

PRICE MOVEMENT:
  Change:     +$250.00000000
  Percentage: +0.26%

Note: This uses OHLCV candle logic. The CLOSE price of the candle
      containing your requested time is shown as the price.
      Price movement shows the change from Open to Close.

──────────────────────────────────────────────────────────────────────

Press Enter to check another crypto, or type 'back' to change market
```

**Notice:** The tool automatically detects midnight crossing and shows how much time is in each date!

---

### Example: Daily/Weekly/Monthly Timeframes

**For timeframes 1d and above, NO start time is needed!**

If you choose:
- Date: `2026-01-15`
- Timeframe: `13` (1 day)

It will skip the start time question and show the result directly:

```
──────────────────────────────────────────────────────────────────────
STOCKSCAN - CRYPTO PRICE LOOKUP
──────────────────────────────────────────────────────────────────────

ASSET:           BTCUSDT
MARKET:          Crypto (Binance)
REQUESTED TIME:  2026-01-15 00:00 UTC
TIMEFRAME:       1d

Candle Period:  2026-01-15 00:00 UTC → 2026-01-16 00:00 UTC

CANDLE DATA:
  Open:   $96,000.00000000
  High:   $97,500.00000000
  Low:    $95,800.00000000
  Close:  $97,200.00000000  ← Price at that time
  Volume: 15,234.56

PRICE MOVEMENT:
  Change:     +$1,200.00000000
  Percentage: +1.25%

Note: This uses OHLCV candle logic. The CLOSE price of the candle
      containing your requested time is shown as the price.
      Price movement shows the change from Open to Close.

──────────────────────────────────────────────────────────────────────

Press Enter to check another crypto, or type 'back' to change market
```

---

### Advanced Usage (Optional)

**For advanced users:** You can skip the interactive prompts by providing everything at once:

```
BTCUSDT 2026-01-15 14:39 1h
```

This will:
- Use symbol: BTCUSDT
- Use date: 2026-01-15
- Use start time: 14:39
- Use timeframe: 1h
- Skip all prompts and show result directly

---

**What to do next:**
- Press Enter → Check another crypto
- Type `back` → Go back to market selection (choose stocks or quit)

---

## What If You Make a Mistake?

### Wrong Market Choice
If you type `5` instead of `1` or `2`:

```
⚠ Invalid choice! Please enter 1 for Stocks, 2 for Crypto, or Q to quit.
```

Then it asks you again!

### Wrong Stock Format
If you type just `AAPL` without a date:

```
⚠ Invalid syntax! Use: <SYMBOL> <DATE>
Example: AAPL 2026-01-15
```

Then it asks you again!

### Wrong Crypto Format
If you type just `BTC`:

```
⚠ Invalid syntax! Use: <SYMBOL> <DATE>
Example: BTCUSDT 2026-01-15
```

Then it asks you again!

---

## Complete Flow Diagram

```
1. Open terminal
   ↓
2. Navigate: cd stockscan
   ↓
3. Run: python stockscan.py (or py stockscan.py on Windows)
   ↓
4. See STOCKSCAN banner + info
   ↓
5. Choose market: [1] Stocks  [2] Crypto  [Q] Quit
   ↓
   ├─→ Press 1 → Stock mode
   │   ↓
   │   Enter: AAPL 2026-01-15
   │   ↓
   │   Select timeframe: [1] 1d  [2] 1wk  [3] 1mo
   │   ↓
   │   See price: $258.21
   │   ↓
   │   Press Enter (check another) or type 'back'
   │
   ├─→ Press 2 → Crypto mode
   │   ↓
   │   Enter: BTCUSDT 2026-01-15
   │   ↓
   │   Select timeframe: [1-16] (1s to 1M)
   │   ↓
   │   If intraday (under 1d):
   │   │   ↓
   │   │   Enter start time: 14:39
   │   │   ↓
   │   │   See price with EXACT timing: 14:39 → 15:39
   │   │
   │   If daily or above (1d, 3d, 1w, 1M):
   │   │   ↓
   │   │   See price directly (no start time needed)
   │   ↓
   │   Press Enter (check another) or type 'back'
   │
   └─→ Press Q → Exit program
```

---

## Summary

**That's literally it!**

1. Navigate: `cd stockscan`
2. Run: `python stockscan.py` (or `py stockscan.py`)
3. Press `1` or `2`
4. Type your lookup (just symbol and date)
5. Select timeframe from the menu
6. For crypto intraday: Enter custom start time (e.g., 14:39)
7. Get the price with EXACT timing!

**Key Features:**
- **Custom Start Time**: For crypto intraday timeframes, you can start at ANY time (14:39, not just 14:00)
- **Midnight Crossing Detection**: Automatically shows time split across two dates
- **Interactive Prompts**: Tool guides you step-by-step
- **Advanced Usage**: Can still provide everything at once if you prefer

No complicated commands, no configuration files, no API keys. Just run and use! 🚀
