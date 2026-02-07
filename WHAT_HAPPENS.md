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
                Get crypto, stock & commodity prices at any time


What is StockScan?
  StockScan lets you look up the exact price of any crypto, stock, or commodity
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
  • Commodities: Yahoo Finance (98+ commodity ETFs, NO API KEY NEEDED)
    - Supports: 1d (daily), 1wk (weekly), 1mo (monthly)
    - Works out of the box!
```

---

## Step 4: Choose Your Market

You'll see this question:

```
──────────────────────────────────────────────────────────────────────
Which market do you want to check?

  [1] Stocks       (AAPL, TSLA, RELIANCE.NS, HDFCBANK.BO, etc.)
  [2] Crypto       (BTCUSDT, ETHUSDT, etc.)
  [3] Commodities  (GLD, USO, CORN, etc.)
  [Q] Quit

Enter your choice (1/2/3/Q): _
```

**What to do:**
- Type `1` and press Enter → Go to Stocks
- Type `2` and press Enter → Go to Crypto
- Type `3` and press Enter → Go to Commodities
- Type `Q` and press Enter → Exit the program

---

## Path A: If You Chose Stocks (Pressed 1)

You'll see:

```
──────────────────────────────────────────────────────────────────────
STOCK PRICE LOOKUP

Syntax: <SYMBOL> <DATE>
Examples:
  AAPL 2026-01-15
  TSLA 2026-01-10
  TCS.NS 2024-12-20
  RELIANCE.NS 2024-12-20
  HDFCBANK.BO 2024-12-20

Date format: YYYY-MM-DD
Will ask for timeframe after you enter
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

──────────────────────────────────────────────────────────────────────
What would you like to do next?

  [1]  Check Live Price       - View current market price
  [2]  Compare with Current   - See price movement & P&L
  [3]  Continue               - Check another asset

Select option (1-3): _
```

### Step 3: More Options Menu

After seeing the price result, you now have 3 options:

**Option 1: Check Live Price**
- Shows the current market price
- Includes timestamp
- Shows delay warning (15 min for stocks, 1-2 min for crypto)

**Option 2: Compare with Current**
- Shows both historical and current prices
- Calculates P&L (Profit & Loss)
- Shows percentage change
- Color-coded: Green for profit, Red for loss
- Displays time period between the two prices

**Option 3: Continue**
- Skip to checking another stock

Let's choose **Option 2** to see the comparison:

```
──────────────────────────────────────────────────────────────────────
PRICE COMPARISON - STOCK
──────────────────────────────────────────────────────────────────────

CHECKED PRICE:
  Date/Time:  2026-01-15
  Price:      $258.21

CURRENT PRICE:
  Date/Time:  2026-02-07 14:30:45
  Price:      $265.50

ANALYSIS:
  P&L:        +$7.29
  Change:     +2.82%
  Movement:   PROFIT ↑
  
TIME PERIOD:  23 day(s), 14 hour(s), 30 minute(s)

⚠ Note: The current price may have a ~15 minute delay

──────────────────────────────────────────────────────────────────────

Press Enter to check another stock, or type 'back' to change market
```

---

**What to do next:**
- Press Enter → Check another stock
- Type `back` → Go back to market selection (choose crypto or quit)

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
- Type `back` → Go back to market selection (choose stocks, commodities, or quit)

---

## Path C: If You Chose Commodities (Pressed 3)

You'll see:

```
──────────────────────────────────────────────────────────────────────
COMMODITY PRICE LOOKUP

Syntax: <SYMBOL> <DATE>
Examples:
  GLD 2026-01-15   (Gold)
  USO 2024-12-20   (Crude Oil)
  CORN 2025-06-10  (Corn)

Date format: YYYY-MM-DD
Type 'list' to see all available commodities
Type 'back' to return to market selection

Enter commodity lookup: _
```

**Example: Let's check Gold commodity**

Type: `GLD 2026-01-15` and press Enter

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

**Let's choose `2` for weekly**

---

### Step 2: See the Result

You'll see:

```
──────────────────────────────────────────────────────────────────────
STOCKSCAN - COMMODITY PRICE LOOKUP
──────────────────────────────────────────────────────────────────────

ASSET:           GLD
COMMODITY:       SPDR Gold Trust
MARKET:          Commodities (Yahoo Finance)
REQUESTED DATE:  2024-01-15
TIMEFRAME:       Weekly

Candle Period:  2024-01-15 → 2024-01-21    👈 Full 7-day period
ℹ Note: This period has only 4 trading day(s) out of the full weekly timeframe.
   3 day(s) excluded due to weekends/holidays. Check dates beyond this period for continued data.

CANDLE DATA:
  Open:   $192.50
  High:   $195.80
  Low:    $191.20
  Close:  $194.75  ← Price at end of period    👈 THIS IS THE ANSWER!
  Volume: 8,234,500

PRICE MOVEMENT:
  Change:     +$2.25                       👈 Price went up
  Percentage: +1.17%                       👈 Gained 1.17%

Note: This uses OHLCV candle logic. The CLOSE price of the candle
      for your requested period is shown as the price.
      Price movement shows the change from Open to Close.

──────────────────────────────────────────────────────────────────────

Press Enter to check another commodity, or type 'back' to change market
```

---

### Example: Daily Timeframe

**Or choose `1` for daily:**

```
──────────────────────────────────────────────────────────────────────
STOCKSCAN - COMMODITY PRICE LOOKUP
──────────────────────────────────────────────────────────────────────

ASSET:           USO
COMMODITY:       United States Oil Fund
MARKET:          Commodities (Yahoo Finance)
REQUESTED DATE:  2026-01-15
TIMEFRAME:       Daily

Candle Date:    2026-01-15

CANDLE DATA:
  Open:   $72.45
  High:   $73.20
  Low:    $71.80
  Close:  $72.95  ← Price at that date    👈 THIS IS THE ANSWER!
  Volume: 5,678,900

PRICE MOVEMENT:
  Change:     +$0.50                       👈 Price went up
  Percentage: +0.69%                       👈 Gained 0.69%

Note: This uses OHLCV candle logic. The CLOSE price of the daily
      candle for your requested date is shown as the price.
      Price movement shows the change from Open to Close.

──────────────────────────────────────────────────────────────────────

Press Enter to check another commodity, or type 'back' to change market
```

---

### Viewing All Available Commodities

**Type `list` to see all 98+ commodity ETFs:**

```
──────────────────────────────────────────────────────────────────────
AVAILABLE COMMODITIES (98 total)

PRECIOUS METALS:
  GLD    - SPDR Gold Trust
  IAU    - iShares Gold Trust
  SLV    - iShares Silver Trust
  PPLT   - Aberdeen Standard Physical Platinum Shares ETF
  PALL   - Aberdeen Standard Physical Palladium Shares ETF

ENERGY:
  USO    - United States Oil Fund
  UNG    - United States Natural Gas Fund
  BNO    - United States Brent Oil Fund
  UGA    - United States Gasoline Fund
  UHN    - United States Heating Oil Fund

AGRICULTURE - GRAINS:
  CORN   - Teucrium Corn Fund
  WEAT   - Teucrium Wheat Fund
  SOYB   - Teucrium Soybean Fund
  ...and 85 more

Type a commodity symbol to check its price
──────────────────────────────────────────────────────────────────────
```

---

### Advanced Usage (Optional)

**For advanced users:** You can skip the interactive prompt by providing the timeframe directly:

```
GLD 2026-01-15 1wk
```

This will skip the timeframe selection and show the result directly.

---

**What to do next:**
- Press Enter → Check another commodity
- Type `back` → Go back to market selection (choose stocks, crypto, or quit)

---

## What If You Make a Mistake?

### Wrong Market Choice
If you type `5` instead of `1`, `2`, or `3`:

```
⚠ Invalid choice! Please enter 1 for Stocks, 2 for Crypto, 3 for Commodities, or Q to quit.
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

### Wrong Commodity Format
If you type just `GOLD`:

```
⚠ Invalid syntax! Use: <SYMBOL> <DATE>
Example: GLD 2026-01-15
```

Then it asks you again!

### Wrong or Unsupported Symbol
If you type a symbol that doesn't exist or isn't supported:

```
✗ Error: No data found for symbol WRONGSYMBOL.
The stock/commodity may not have existed at that time, or data is unavailable.

Note: StockScan doesn't cover very small-cap stocks and very newly listed IPOs.
Please verify the symbol is correct and the company has sufficient trading history.
```

**What's NOT supported:**
- Very small-cap/micro-cap stocks (extremely small companies)
- Very newly listed IPOs (companies that just went public)
- Unlisted/private companies (not traded on exchanges)

**What IS supported:**
- All major large-cap and mid-cap stocks
- All NIFTY 50 and BSE Sensex stocks
- All major US stocks (NYSE, NASDAQ)
- 1000+ crypto pairs on Binance
- 98+ commodity ETFs

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
5. Choose market: [1] Stocks  [2] Crypto  [3] Commodities  [Q] Quit
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
   ├─→ Press 3 → Commodity mode
   │   ↓
   │   Enter: GLD 2026-01-15 (or type 'list' to see all commodities)
   │   ↓
   │   Select timeframe: [1] 1d  [2] 1wk  [3] 1mo
   │   ↓
   │   See price: $194.75
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
3. Press `1`, `2`, or `3`
4. Type your lookup (just symbol and date)
5. Select timeframe from the menu
6. For crypto intraday: Enter custom start time (e.g., 14:39)
7. Get the price with EXACT timing!

**Key Features:**
- **3 Markets**: Stocks, Crypto, and Commodities (98+ commodity ETFs)
- **Custom Start Time**: For crypto intraday timeframes, you can start at ANY time (14:39, not just 14:00)
- **Midnight Crossing Detection**: Automatically shows time split across two dates
- **Full Period Display**: Weekly/monthly shows complete calendar periods with trading day notifications
- **Error Handling**: Clear messages for future dates, non-existent assets, and incomplete data
- **Interactive Prompts**: Tool guides you step-by-step
- **Advanced Usage**: Can still provide everything at once if you prefer

No complicated commands, no configuration files, no API keys. Just run and use! 🚀
