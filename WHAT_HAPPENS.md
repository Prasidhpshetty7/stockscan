# 🎬 What Actually Happens When You Run StockScan

## Step 1: Download and Setup

1. Download `stockscan.py` to your computer
2. Open terminal/command prompt
3. Navigate to where you saved the file
4. Run: `pip install requests` (one-time setup)

---

## Step 2: Run StockScan

Type this command:
```bash
python stockscan.py
```

or

```bash
py stockscan.py
```

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
  • This is the same method used by CryptoFetch and other tools

Data Sources:
  • Crypto: Binance (1000+ coins, NO API KEY NEEDED)
    - Supports: 5m, 15m, 30m, 1h, 4h, 12h, 1d, 3d, 1w, 1M timeframes
  • Stocks: Yahoo Finance (all US stocks, NO API KEY NEEDED)
    - Supports: Daily data
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

**What to do next:**
- Press Enter → Check another stock
- Type `back` → Go back to market selection (choose crypto or quit)

---

## Path B: If You Chose Crypto (Pressed 2)

You'll see:

```
──────────────────────────────────────────────────────────────────────
CRYPTO PRICE LOOKUP

Syntax: <SYMBOL> <DATE> <TIME> <TIMEFRAME>
Examples:
  BTCUSDT 2026-01-15 14:30 1h  (Bitcoin, 1-hour candle)
  ETHUSDT 2026-01-15 10:00 5m  (Ethereum, 5-minute candle)
  BNBUSDT 2026-01-10 1d        (BNB, daily candle - time optional)

Date format: YYYY-MM-DD
Time format: HH:MM (optional for daily timeframe)
Timeframes: 5m, 15m, 30m, 1h, 4h, 12h, 1d, 3d, 1w, 1M
Type 'back' to return to market selection

Enter crypto lookup: _
```

**Example: Let's check Bitcoin price**

Type: `BTCUSDT 2026-01-15 14:30 1h` and press Enter

You'll see:

```
──────────────────────────────────────────────────────────────────────
STOCKSCAN - CRYPTO PRICE LOOKUP
──────────────────────────────────────────────────────────────────────

ASSET:           BTCUSDT
MARKET:          Crypto (Binance)
REQUESTED TIME:  2026-01-15 14:30 UTC
TIMEFRAME:       1h

Candle Period:  2026-01-15 14:00 UTC → 2026-01-15 14:59 UTC

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
⚠ Invalid syntax! Use: <SYMBOL> <DATE> [TIME] [TIMEFRAME]
Example: BTCUSDT 2026-01-15 14:30
```

Then it asks you again!

---

## Complete Flow Diagram

```
1. Run: python stockscan.py
   ↓
2. See STOCKSCAN banner + info
   ↓
3. Choose market: [1] Stocks  [2] Crypto  [Q] Quit
   ↓
   ├─→ Press 1 → Stock mode
   │   ↓
   │   Enter: AAPL 2026-01-15
   │   ↓
   │   See price: $258.21
   │   ↓
   │   Press Enter (check another) or type 'back'
   │
   ├─→ Press 2 → Crypto mode
   │   ↓
   │   Enter: BTCUSDT 2026-01-15 14:30 1h
   │   ↓
   │   See price: $97,040.75
   │   ↓
   │   Press Enter (check another) or type 'back'
   │
   └─→ Press Q → Exit program
```

---

## Summary

**That's literally it!**

1. Run: `python stockscan.py`
2. Press `1` or `2`
3. Type your lookup
4. Get the price!

No complicated commands, no configuration files, no API keys. Just run and use! 🚀
