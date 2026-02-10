# 🚀 StockScan - Quick Start Guide

## Step 1: Download the File

Download `stockscan.py` from this repository to your computer.

---

## Step 2: Install Python (if you don't have it)

**Check if you have Python:**
```bash
python --version
```
or
```bash
py --version
```

If you don't have Python, download it from: https://www.python.org/downloads/

**Minimum version required:** Python 3.7 or higher

---

## Step 3: Install Required Library

Open your terminal/command prompt and run:

```bash
pip install requests yfinance
```

or

```bash
python -m pip install requests yfinance
```

**What are these libraries?**
- `requests` - Required for all features (price checking & crypto export)
- `yfinance` - Required only for stock/commodity data export (optional)

---

## Step 4: Run StockScan

### Option A: Interactive Mode (Recommended for Beginners)

Just run the file without any arguments:

```bash
python stockscan.py
```

or

```bash
py stockscan.py
```

## Step 5: Using StockScan

### Interactive Mode (Easiest)

Run without arguments:
```bash
python stockscan.py
```

**What happens:**

1. **You see the banner** - Big purple STOCKSCAN logo with description

2. **Choose what to do** - Main menu appears:
   - `[1]` Check Prices - Look up historical prices
   - `[2]` Export Data - Download bulk data to CSV
   - `[Q]` Quit

3. **If you choose Check Prices (Option 1):**
   - Choose market: `1` for Stocks, `2` for Crypto, `3` for Commodities
   - Enter your lookup (e.g., `AAPL 2026-01-15`)
   - Select timeframe from the menu
   - See the price with OHLCV data and price movement
   - Get 3 more options:
     - `[1]` Check Live Price - See current market price
     - `[2]` Compare with Current - See P&L and percentage change
     - `[3]` Continue - Check another asset

4. **If you choose Export Data (Option 2):**
   - Choose market: `1` for Crypto, `2` for Stocks, `3` for Commodities
   - Enter symbol (e.g., `BTCUSDT`, `AAPL`, `GLD`)
   - Enter start date (e.g., `2024-01-01`)
   - Enter end date (e.g., `2024-12-31`)
   - Select timeframe (16 options for crypto, 3 for stocks/commodities)
   - Data automatically downloads to `exports/` folder as CSV
   - Shows success message with file location and row count

**Example output:**
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
  Close:  $258.21  ← Price at that date
  Volume: 39,388,600

PRICE MOVEMENT:
  Change:     -$2.44
  Percentage: -0.94%
```

Then you can check live price or compare with current price to see profit/loss!

**Example CSV export:**
```
✓ Data exported successfully!
File: exports/BTCUSDT_1d_2024-01-01_to_2024-12-31.csv
Rows: 365
Symbol: BTCUSDT
Timeframe: 1d
```

The CSV file contains: timestamp, open, high, low, close, volume, close_time

---
1. You'll see a big purple STOCKSCAN banner
2. It asks: "Which market do you want to check?"
   - Press `1` for Stocks
   - Press `2` for Crypto
   - Press `3` for Commodities
   - Press `Q` to quit

3. After choosing, it shows you examples of how to enter data

4. You type your lookup (example: `AAPL 2026-01-15`)

5. Select timeframe from the menu

6. It shows you the price with OHLCV data and price movement!

7. You get 3 options:
   - Check live price
   - Compare with current price (see P&L)
   - Continue to check another

8. Press Enter to check another price, or type `back` to change markets

---

### Option B: Command Line Mode (For Quick Lookups)

Navigate to the stockscan folder first:
```bash
cd stockscan
```

**For Stocks:**
```bash
python stockscan.py stock AAPL 2026-01-15 --timeframe 1d
python stockscan.py stock TSLA 2025-06-10 --timeframe 1wk
python stockscan.py stock TCS.NS 2024-12-20 --timeframe 1mo
python stockscan.py stock INFY.NS 2023-08-05 --timeframe 1d
python stockscan.py stock HDFCBANK.BO 2024-03-18 --timeframe 1wk
```

**For Crypto:**
```bash
python stockscan.py crypto BTCUSDT 2026-01-15 14:30 --timeframe 1h
python stockscan.py crypto ETHUSDT 2026-01-15 10:00 --timeframe 5m
python stockscan.py crypto BNBUSDT 2026-01-10 --timeframe 1d
```

**For Commodities:**
```bash
python stockscan.py commodity GLD 2026-01-15 --timeframe 1d
python stockscan.py commodity USO 2024-12-20 --timeframe 1wk
python stockscan.py commodity CORN 2024-01-15 --timeframe 1mo
```

**Windows users:** Replace `python` with `py` if needed

**Timeframe options for crypto (16 total):**
- `1s` = 1 second
- `1m` = 1 minute
- `3m` = 3 minutes
- `5m` = 5 minutes
- `15m` = 15 minutes
- `30m` = 30 minutes
- `1h` = 1 hour
- `2h` = 2 hours
- `4h` = 4 hours
- `6h` = 6 hours
- `8h` = 8 hours
- `12h` = 12 hours
- `1d` = 1 day
- `3d` = 3 days
- `1w` = 1 week
- `1M` = 1 month

*All 16 Binance timeframes supported!*

**Timeframe options for stocks:**
- `1d` = Daily (full history)
- `1wk` = Weekly (full history)
- `1mo` = Monthly (full history)

**Timeframe options for commodities:**
- `1d` = Daily (full history)
- `1wk` = Weekly (full history)
- `1mo` = Monthly (full history)

*Commodities use the same timeframes as stocks - daily and above only*

---

## Step 5: Understanding the Output

### Daily Lookup Output

When you look up a daily price, you'll see:

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
  Close:  $258.21  ← Price at that date    👈 THIS IS THE PRICE!
  Volume: 39,388,600

PRICE MOVEMENT:
  Change:     -$2.44                       👈 Price went down by $2.44
  Percentage: -0.94%                       👈 Lost 0.94%
```

### Weekly/Monthly Lookup Output

When you look up a weekly or monthly period, you'll see:

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
  Change:     +$9.40                       👈 Price went up by $9.40
  Percentage: +5.16%                       👈 Gained 5.16%
```

### What Each Part Means:

**CANDLE DATA:**
- **Open** = Price when the day/period started
- **High** = Highest price during that day/period
- **Low** = Lowest price during that day/period
- **Close** = Price when the day/period ended ← **This is the main price!**
- **Volume** = How many shares/coins were traded

**PRICE MOVEMENT:**
- **Change** = How much the price moved (Close - Open)
  - Green with + = Price went up 📈
  - Red with - = Price went down 📉
  - Yellow = No change
- **Percentage** = Percentage change from Open to Close
  - Shows the gain or loss as a percentage

**WEEKLY/MONTHLY PERIODS:**
- **Candle Period** = Shows the full 7-day (weekly) or 30-day (monthly) calendar period
- **Trading Days Note** = Tells you how many days had actual market activity
- **Non-Trading Days** = Weekends and holidays don't have trading data
- **Example**: A week with 1 holiday + 2 weekend days = only 4 trading days

**CRYPTO CUSTOM START TIME (Intraday Timeframes):**
- **Any Start Time** = For timeframes under 1d, you can start from ANY time (14:39, 23:59, etc.)
- **Perfect Timing** = 14:39 with 1h = exactly 14:39:00 to 15:39:00
- **Midnight Crossing** = If period crosses midnight, shows time split across dates
- **Example**: 23:59 with 3m = "1 minute from 2026-01-02, 2 minutes from 2026-01-03"

**Example:**
- If a stock opened at $100 and closed at $105:
  - Change: +$5.00 (gained $5)
  - Percentage: +5.00% (gained 5%)

---

## Complete Example Walkthrough

### Example 1: Check Apple Stock Price (Daily)

1. Open terminal
2. Navigate to folder: `cd stockscan`
3. Run: `python stockscan.py` (or `py stockscan.py` on Windows)
4. Press `1` (for Stocks)
5. Type: `AAPL 2026-01-15`
6. Select timeframe: `1` (Daily)
7. See the price: $258.21

### Example 2: Check Apple Stock Price (Weekly)

1. Open terminal
2. Navigate to folder: `cd stockscan`
3. Run: `python stockscan.py` (or `py stockscan.py` on Windows)
4. Press `1` (for Stocks)
5. Type: `AAPL 2024-01-15`
6. Select timeframe: `2` (Weekly)
7. See the period: Jan 15 → Jan 21 with 4 trading days

### Example 3: Check Bitcoin Price with Custom Start Time

1. Open terminal
2. Navigate to folder: `cd stockscan`
3. Run: `python stockscan.py` (or `py stockscan.py` on Windows)
4. Press `2` (for Crypto)
5. Type: `BTCUSDT 2026-01-02`
6. Select timeframe: `7` (1 hour)
7. Enter start time: `14:39`
8. See the period: 14:39 → 15:39 with exact pricing

### Example 4: Check Bitcoin with Midnight Crossing

1. Open terminal
2. Navigate to folder: `cd stockscan`
3. Run: `python stockscan.py` (or `py stockscan.py` on Windows)
4. Press `2` (for Crypto)
5. Type: `BTCUSDT 2026-01-02`
6. Select timeframe: `3` (3 minutes)
7. Enter start time: `23:59`
8. See the split: 1 min from Jan 2, 2 mins from Jan 3

### Example 5: Check Gold Commodity Price (Weekly)

1. Open terminal
2. Navigate to folder: `cd stockscan`
3. Run: `python stockscan.py` (or `py stockscan.py` on Windows)
4. Press `3` (for Commodities)
5. Type: `GLD 2024-01-15`
6. Select timeframe: `2` (Weekly)
7. See the period: Jan 15 → Jan 21 with full commodity data

---

## 🔴 Live Price & Comparison Features (NEW!)

After checking a historical price, StockScan now offers additional options!

### What Happens After You Check a Price?

Instead of immediately asking "Press Enter to continue", you'll now see:

```
──────────────────────────────────────────────────────────────────────
What would you like to do next?

  [1]  Check Live Price       - View current market price
  [2]  Compare with Current   - See price movement & P&L
  [3]  Continue               - Check another asset

Select option (1-3): _
```

### Option 1: Check Live Price

Shows you the current market price right now:

```
──────────────────────────────────────────────────────────────────────
LIVE STOCK PRICE
──────────────────────────────────────────────────────────────────────

ASSET:           AAPL
SOURCE:          Yahoo Finance
TIMESTAMP:       2026-02-07 14:30:45

CURRENT PRICE:  $265.50

⚠ Note: The current price may have a ~15 minute delay

──────────────────────────────────────────────────────────────────────
```

**Delay Times:**
- Crypto: 1-2 minute delay (Binance)
- Stocks: ~15 minute delay (Yahoo Finance)
- Commodities: ~15 minute delay (Yahoo Finance)

### Option 2: Compare with Current Price

This is the BEST feature! It shows you:
- Your checked historical price
- The current market price
- How much profit/loss you would have made
- Percentage change
- Exact time period between the two prices

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
  P&L:        +$7.29                       👈 You would have gained $7.29!
  Change:     +2.82%                       👈 2.82% profit!
  Movement:   PROFIT ↑                     👈 Green color = profit!
  
TIME PERIOD:  23 day(s), 14 hour(s), 30 minute(s)

⚠ Note: The current price may have a ~15 minute delay

──────────────────────────────────────────────────────────────────────
```

**Color Coding:**
- 🟢 Green with "PROFIT ↑" = Price went up (you made money!)
- 🔴 Red with "LOSS ↓" = Price went down (you lost money)
- 🟡 Yellow with "NO CHANGE →" = Price stayed the same

**Works for ALL markets:**
- ✅ Stocks (US & Indian)
- ✅ Crypto
- ✅ Commodities

### Option 3: Continue

Just press 3 and it goes back to the normal flow - press Enter to check another asset.

---

## Common Questions

**Q: Do I need an API key?**
A: NO! Everything works out of the box. No registration, no API keys needed.

**Q: What stocks can I check?**
A: All US stocks (AAPL, TSLA, MSFT, GOOGL, AMZN, etc.) and Indian stocks (RELIANCE.NS, TCS.NS, etc.)

**Q: What crypto can I check?**
A: All Binance spot pairs (BTCUSDT, ETHUSDT, BNBUSDT, etc.)

**Q: What commodities can I check?**
A: 98+ commodity ETFs including Gold (GLD), Oil (USO), Silver (SLV), Natural Gas (UNG), Corn (CORN), Wheat (WEAT), and many more

**Q: Can I check old prices?**
A: Yes! You can check any historical date when the asset existed.

**Q: Can I check future prices?**
A: No, it will show an error: "Future price data does not exist. The requested date is in the future."

**Q: What if the asset didn't exist at that time?**
A: You'll see: "No data available for [SYMBOL] on [DATE]. The stock/commodity may not have existed at that time, or data is unavailable for this date range."

**Q: What if I make a mistake?**
A: The tool will show you a warning and ask you to try again with the correct format.

**Q: Can I check the current live price?**
A: Yes! After viewing historical data, choose option [1] to see the current market price.

**Q: Can I compare historical price with current price?**
A: Yes! After viewing historical data, choose option [2] to see a detailed comparison with P&L, percentage change, and time period.

**Q: How accurate is the live price?**
A: Very accurate! Crypto has 1-2 minute delay (Binance), Stocks/Commodities have ~15 minute delay (Yahoo Finance).

**Q: Does the comparison feature work for all markets?**
A: Yes! It works for crypto, stocks (US & Indian), and commodities.

**Q: What if I enter a wrong stock symbol?**
A: StockScan will show an error message. Note that StockScan doesn't cover very small-cap stocks and very newly listed IPOs. Please verify the symbol is correct and the company has sufficient trading history.

**Q: What stocks are NOT supported?**
A: StockScan doesn't cover:
   - Very small-cap/micro-cap stocks (extremely small companies)
   - Very newly listed IPOs (companies that just went public)
   - Unlisted/private companies (not traded on exchanges)
   All major large-cap and mid-cap stocks are fully supported!

---

## 📊 Data Export Feature

Want to export bulk historical data to CSV files? Just choose option `[2] Export Data` from the main menu!

**What it does:**
- Export thousands of candles at once
- Save to CSV files for analysis
- Perfect for backtesting strategies
- Works with Python, Excel, R, etc.

**How to use:**
1. Run: `python stockscan.py`
2. Choose: `[2] Export Data`
3. Select market (Crypto/Stocks/Commodities)
4. Enter symbol, start date, end date, timeframe
5. Data automatically downloads to `exports/` folder

**CSV format:**
- timestamp, open, high, low, close, volume, close_time
- Ready for backtesting and analysis
- Compatible with all data analysis tools

**Supported timeframes:**
- Crypto: 16 timeframes (1s to 1M)
- Stocks/Commodities: 3 timeframes (1d, 1wk, 1mo)

---

## Need Help?

Run this command (from inside the stockscan folder):
```bash
cd stockscan
python stockscan.py help
```

Or on Windows:
```bash
cd stockscan
py stockscan.py help
```

---

## That's It!

You're ready to use StockScan! 🎉

**Summary:**
1. Download `stockscan.py`
2. Install Python (if needed)
3. Run: `pip install requests yfinance`
4. Navigate: `cd stockscan`
5. Run: `python stockscan.py` (or `py stockscan.py`)
6. Follow the prompts!

No complicated setup, no API keys, just download and run! 🚀
