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
pip install requests
```

or

```bash
python -m pip install requests
```

That's it! Only one library needed.

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

**What happens:**
1. You'll see a big purple STOCKSCAN banner
2. It asks: "Which market do you want to check?"
   - Press `1` for Stocks
   - Press `2` for Crypto
   - Press `Q` to quit

3. After choosing, it shows you examples of how to enter data

4. You type your lookup (example: `AAPL 2026-01-15`)

5. It shows you the price!

6. Press Enter to check another price, or type `back` to change markets

---

### Option B: Command Line Mode (For Quick Lookups)

**For Stocks:**
```bash
python stockscan.py stock AAPL 2026-01-15
python stockscan.py stock TSLA 2024-12-20
python stockscan.py stock MSFT 2025-06-10
```

**For Crypto:**
```bash
python stockscan.py crypto BTCUSDT 2026-01-15 14:30 --timeframe 1h
python stockscan.py crypto ETHUSDT 2026-01-15 10:00 --timeframe 5m
python stockscan.py crypto BNBUSDT 2026-01-10 --timeframe 1d
```

**Timeframe options for crypto:**
- `1m` = 1 minute
- `5m` = 5 minutes
- `15m` = 15 minutes
- `1h` = 1 hour
- `1d` = 1 day

---

## Step 5: Understanding the Output

When you look up a price, you'll see:

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

**Example:**
- If a stock opened at $100 and closed at $105:
  - Change: +$5.00 (gained $5)
  - Percentage: +5.00% (gained 5%)

---

## Complete Example Walkthrough

### Example 1: Check Apple Stock Price

1. Open terminal
2. Run: `python stockscan.py`
3. Press `1` (for Stocks)
4. Type: `AAPL 2026-01-15`
5. Press Enter
6. See the price: $258.21

### Example 2: Check Bitcoin Price

1. Open terminal
2. Run: `python stockscan.py`
3. Press `2` (for Crypto)
4. Type: `BTCUSDT 2026-01-15 14:30 1h`
5. Press Enter
6. See the price: $97,040.75

---

## Common Questions

**Q: Do I need an API key?**
A: NO! Everything works out of the box. No registration, no API keys needed.

**Q: What stocks can I check?**
A: All US stocks (AAPL, TSLA, MSFT, GOOGL, AMZN, etc.)

**Q: What crypto can I check?**
A: All Binance spot pairs (BTCUSDT, ETHUSDT, BNBUSDT, etc.)

**Q: Can I check old prices?**
A: Yes! You can check any historical date when the asset existed.

**Q: Can I check future prices?**
A: No, it will show an error: "Future price data does not exist."

**Q: What if I make a mistake?**
A: The tool will show you a warning and ask you to try again with the correct format.

---

## Need Help?

Run this command to see all options:
```bash
python stockscan.py help
```

---

## That's It!

You're ready to use StockScan! 🎉

**Summary:**
1. Download `stockscan.py`
2. Install Python (if needed)
3. Run: `pip install requests`
4. Run: `python stockscan.py`
5. Follow the prompts!

No complicated setup, no API keys, just download and run! 🚀
