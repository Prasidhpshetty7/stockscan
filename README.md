# 📈 StockScan

**Get the exact price of any crypto, stock, or commodity at any point in time - instantly!**

No API keys. No registration. Just download and run.

---

## 🎯 What Does It Do?

StockScan answers one simple question: **"What was the price at this exact time?"**

Plus, it now lets you **compare with current prices** and see your potential profit/loss!

- 📊 **Stocks**: Check any US or Indian stock (AAPL, TSLA, RELIANCE.NS, etc.)
- 💰 **Crypto**: Check any Binance coin (BTC, ETH, BNB, etc.)
- 🏆 **Commodities**: Check 98+ commodity ETFs (Gold, Oil, Corn, etc.)
- 🕐 **Any Time**: Historical prices from any date/time
- 🔴 **Live Prices**: Check current market price after viewing historical data
- 📈 **Price Comparison**: See P&L, percentage change, and profit/loss between historical and current prices
- 🎨 **Beautiful Output**: Clean, colorful terminal display

---

## ⚡ Quick Start (3 Steps)

### 1. Download
Download `stockscan.py` from this repository

### 2. Install Requirements
```bash
pip install requests
```

### 3. Run It!

**Option A - Navigate to the folder first (Recommended):**
```bash
cd stockscan
python stockscan.py
```

**Option B - Run from parent folder:**
```bash
# Windows
python stockscan\stockscan.py

# Mac/Linux
python stockscan/stockscan.py
```

**Note for Windows users:** If `python` doesn't work, try `py` instead:
```bash
cd stockscan
py stockscan.py
```

That's it! No API keys, no configuration, no hassle.

---

## 🎮 How to Use

### Interactive Mode (Easiest)

First, navigate to the stockscan folder:
```bash
cd stockscan
```

Then run without arguments:
```bash
python stockscan.py
```
Or on Windows, you can use:
```bash
py stockscan.py
```

You'll see:
1. ✨ Big purple STOCKSCAN banner
2. 📋 Choose: `[1] Stocks` or `[2] Crypto` or `[3] Commodities`
3. 📝 Enter your lookup (e.g., `AAPL 2026-01-15` or `BTCUSDT 2026-01-15` or `GLD 2026-01-15`)
4. 🕐 Select timeframe (interactive prompt)
5. ⏰ For crypto intraday: Enter custom start time (e.g., 14:39)
6. 💵 Get the price instantly!

### Command Line Mode (Fastest)

Navigate to the stockscan folder first:
```bash
cd stockscan
```

**Stocks:**
```bash
python stockscan.py stock AAPL 2026-01-15 --timeframe 1d
python stockscan.py stock TSLA 2025-06-10 --timeframe 1wk
python stockscan.py stock TCS.NS 2024-12-20 --timeframe 1mo
python stockscan.py stock INFY.NS 2023-08-05 --timeframe 1d
python stockscan.py stock HDFCBANK.BO 2024-03-18 --timeframe 1wk
```

**Crypto:**
```bash
python stockscan.py crypto BTCUSDT 2026-01-15 14:30 --timeframe 1h
python stockscan.py crypto ETHUSDT 2026-01-15 10:00 --timeframe 5m
python stockscan.py crypto BTCUSDT 2026-01-15 23:59 --timeframe 3m
```

**Commodities:**
```bash
python stockscan.py commodity GLD 2026-01-15 --timeframe 1d
python stockscan.py commodity USO 2024-12-20 --timeframe 1wk
python stockscan.py commodity CORN 2024-01-15 --timeframe 1mo
```

**Note:** For crypto intraday timeframes (under 1d), you can specify ANY start time (HH:MM format). The tool will create a custom period starting from that exact time!

**Windows users:** Replace `python` with `py` if needed

---

## 📸 Example Output

### Stock Weekly Lookup
```
──────────────────────────────────────────────────────────────────────
STOCKSCAN - STOCK PRICE LOOKUP
──────────────────────────────────────────────────────────────────────

ASSET:           AAPL
MARKET:          Stocks (Yahoo Finance)
REQUESTED DATE:  2024-01-15
TIMEFRAME:       Weekly

Candle Period:  2024-01-15 → 2024-01-21
ℹ Note: This period has only 4 trading day(s) out of the full weekly timeframe.
   3 day(s) excluded due to weekends/holidays. Check dates beyond this period for continued data.

CANDLE DATA:
  Open:   $182.16
  High:   $191.95
  Low:    $180.30
  Close:  $191.56  ← Price at that date
  Volume: 259,829,200

PRICE MOVEMENT:
  Change:     +$9.40
  Percentage: +5.16%

Note: This uses OHLCV candle logic. The CLOSE price of the candle
      for your requested period is shown as the price.
      Price movement shows the change from Open to Close.

──────────────────────────────────────────────────────────────────────
```

### Stock Daily Lookup
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

Note: This uses OHLCV candle logic. The CLOSE price of the daily
      candle for your requested date is shown as the price.
      Price movement shows the change from Open to Close.

──────────────────────────────────────────────────────────────────────
```

### Commodity Weekly Lookup
```
──────────────────────────────────────────────────────────────────────
STOCKSCAN - COMMODITY PRICE LOOKUP
──────────────────────────────────────────────────────────────────────

ASSET:           GLD
COMMODITY:      SPDR Gold Shares
MARKET:          Commodities (Yahoo Finance)
REQUESTED DATE:  2024-01-15
TIMEFRAME:       Weekly

Candle Period:  2024-01-15 → 2024-01-21
ℹ Note: This period has only 4 trading day(s) out of the full weekly timeframe.
   3 day(s) excluded due to weekends/holidays. Check dates beyond this period for continued data.

CANDLE DATA:
  Open:   $189.15
  High:   $189.26
  Low:    $185.45
  Close:  $187.93  ← Price at that date
  Volume: 25,596,200

PRICE MOVEMENT:
  Change:     $1.22
  Percentage: -0.64%

Note: This uses OHLCV candle logic. The CLOSE price of the candle
      for your requested period is shown as the price.
      Price movement shows the change from Open to Close.

──────────────────────────────────────────────────────────────────────
```

### Crypto Intraday with Custom Start Time
```
──────────────────────────────────────────────────────────────────────
STOCKSCAN - CRYPTO PRICE LOOKUP
──────────────────────────────────────────────────────────────────────

ASSET:           BTCUSDT
MARKET:          Crypto (Binance)
REQUESTED TIME:  2026-01-02 14:39 UTC
TIMEFRAME:       1h

Candle Period:  2026-01-02 14:39 UTC → 2026-01-02 15:39 UTC

CANDLE DATA:
  Open:   $89,133.80000000
  High:   $89,800.00000000
  Low:    $89,106.34000000
  Close:  $89,715.36000000  ← Price at that time
  Volume: 1,253.49

PRICE MOVEMENT:
  Change:     +$581.56000000
  Percentage: +0.65%

Note: This uses OHLCV candle logic. The CLOSE price of the candle
      containing your requested time is shown as the price.
      Price movement shows the change from Open to Close.

──────────────────────────────────────────────────────────────────────
```

### Crypto with Midnight Crossing
```
──────────────────────────────────────────────────────────────────────
STOCKSCAN - CRYPTO PRICE LOOKUP
──────────────────────────────────────────────────────────────────────

ASSET:           BTCUSDT
MARKET:          Crypto (Binance)
REQUESTED TIME:  2026-01-02 23:59 UTC
TIMEFRAME:       3m

Candle Period:  2026-01-02 23:59 UTC → 2026-01-03 00:02 UTC

ℹ Note: Timeframe spans across two dates.
   Period includes: 1 minute(s) from 2026-01-02, 2 minute(s) from 2026-01-03

CANDLE DATA:
  Open:   $90,305.99000000
  High:   $90,339.89000000
  Low:    $90,132.94000000
  Close:  $90,157.13000000  ← Price at that time
  Volume: 54.84

PRICE MOVEMENT:
  Change:     $148.86000000
  Percentage: -0.16%

Note: This uses OHLCV candle logic. The CLOSE price of the candle
      containing your requested time is shown as the price.
      Price movement shows the change from Open to Close.

──────────────────────────────────────────────────────────────────────
```

### 📊 Understanding the Output

**CANDLE DATA** - Shows the OHLCV (Open, High, Low, Close, Volume) for that time period:
- **Open**: Price when the period started
- **High**: Highest price during the period
- **Low**: Lowest price during the period
- **Close**: Price when the period ended (this is the main price shown)
- **Volume**: How much was traded during the period

**PRICE MOVEMENT** - Shows how the price changed during that period:
- **Change**: Absolute price difference from Open to Close (in $ or ₹)
  - Green with + sign = Price went up
  - Red with - sign = Price went down
  - Yellow = No change
- **Percentage**: Percentage change from Open to Close
  - Shows how much the price moved as a percentage

**WEEKLY/MONTHLY PERIODS** - For weekly (1wk) and monthly (1mo) timeframes:
- **Candle Period**: Shows the full 7-day or 30-day calendar period
- **Trading Days Note**: Indicates how many days had actual trading activity
- **Non-Trading Days**: Weekends and holidays are excluded from the data
- **Example**: A week starting Monday with a holiday shows "4 trading days out of 7"

**CRYPTO CUSTOM START TIME** - For crypto intraday timeframes (under 1d):
- **Any Start Time**: You can specify ANY time (e.g., 14:39, 23:59) and the period starts exactly from that time
- **Perfect Timing**: 14:39 with 1h timeframe = exactly 14:39:00 to 15:39:00
- **Midnight Crossing**: If the period crosses midnight, it shows the time split across dates
- **Example**: 23:59 with 3m = "1 minute(s) from 2026-01-02, 2 minute(s) from 2026-01-03"
- **Non-Trading Days**: Weekends and holidays are excluded from the data
- **Example**: A week starting Monday with a holiday shows "4 trading days out of 7"

**Example**: If a stock opened at $100 and closed at $105:
- Change: +$5.00 (gained $5)
- Percentage: +5.00% (gained 5%)

---

## 🔧 Features

✅ **No API Keys Required** - Works immediately after download  
✅ **1000+ Cryptocurrencies** - All Binance spot pairs  
✅ **All US & Indian Stocks** - NYSE, NASDAQ, AMEX, NSE, BSE  
✅ **98+ Commodity ETFs** - Gold, Silver, Oil, Natural Gas, Agriculture, Metals & more  
✅ **Multiple Timeframes** - Crypto: 16 timeframes (1s to 1M) | Stocks & Commodities: 3 timeframes (1d, 1wk, 1mo)  
✅ **Custom Start Time** - For crypto intraday: Start from ANY time (14:39, 23:59, etc.) with perfect precision  
✅ **Midnight Crossing Detection** - Automatically detects and shows time split across dates  
✅ **Historical Data** - Check any past date with full history  
✅ **Weekly/Monthly Periods** - Shows full calendar periods with trading day counts  
✅ **Live Price Checking** - Check current market price after viewing historical data  
✅ **Price Comparison** - Compare historical price with current price, see P&L and percentage change  
✅ **Price Movement Calculator** - Shows change and percentage gain/loss  
✅ **Smart Holiday Detection** - Warns about weekends and holidays in the period  
✅ **Smart Error Messages** - Clear warnings about unsupported symbols (very small-cap stocks, new IPOs)  
✅ **Beautiful UI** - Colorful terminal output with color-coded gains/losses  
✅ **Error Handling** - Clear warnings and helpful messages  
✅ **Interactive & CLI Modes** - Use whichever you prefer  

---

## 🔴 Live Price & Comparison Features

After checking a historical price, StockScan offers additional options:

### More Options Menu

After displaying historical price data, you'll see:

```
──────────────────────────────────────────────────────────────────────
What would you like to do next?

  [1]  Check Live Price       - View current market price
  [2]  Compare with Current   - See price movement & P&L
  [3]  Continue               - Check another asset

Select option (1-3): _
```

### Option 1: Check Live Price

Shows the current market price with timestamp:

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

**Data Sources:**
- **Crypto**: Binance API (1-2 minute delay)
- **Stocks**: Yahoo Finance (15 minute delay)
- **Commodities**: Yahoo Finance (15 minute delay)

### Option 2: Compare with Current Price

Shows detailed comparison between historical and current price:

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
```

**Features:**
- ✅ Shows both checked and current prices side-by-side
- ✅ Calculates P&L (Profit & Loss)
- ✅ Shows percentage change
- ✅ Color-coded: Green for profit, Red for loss
- ✅ Displays exact time period between prices
- ✅ Works for crypto, stocks, and commodities

### Option 3: Continue

Returns to the normal flow - press Enter to check another asset or type 'back' to change markets.

---

## 📋 Coverage & Limitations

### ✅ What IS Supported

**Stocks:**
- All major large-cap and mid-cap stocks
- All NIFTY 50 stocks (India NSE)
- All BSE Sensex stocks (India BSE)
- All major US stocks (NYSE, NASDAQ, AMEX)
- 1000+ NSE/BSE listed stocks
- Major international stocks

**Crypto:**
- 1000+ Binance spot trading pairs
- All major cryptocurrencies (BTC, ETH, BNB, etc.)
- Full historical data with 16 timeframes

**Commodities:**
- 98+ commodity ETFs
- Gold, Silver, Platinum, Palladium
- Oil, Natural Gas, Gasoline
- Agriculture (Corn, Wheat, Soy, etc.)
- Industrial Metals (Copper, Aluminum, etc.)

### ❌ What is NOT Supported

**Stocks:**
- Very small-cap/micro-cap stocks (extremely small companies with minimal liquidity)
- Very newly listed IPOs (companies that just went public with limited trading history)
- Unlisted/private companies (not traded on public exchanges)
- Recently delisted stocks

**Why?**
These stocks either don't have sufficient data available on Yahoo Finance or lack the trading history needed for reliable price lookups.

**Error Message:**
If you try to look up an unsupported stock, you'll see:
```
✗ Error: No data found for symbol [SYMBOL].

Note: StockScan doesn't cover very small-cap stocks and very newly listed IPOs.
Please verify the symbol is correct and the company has sufficient trading history.
```

---

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Step-by-step guide for beginners
- **[WHAT_HAPPENS.md](WHAT_HAPPENS.md)** - Visual walkthrough
- Run `python stockscan.py help` - See all commands

---

## 🎓 How It Works

StockScan uses **OHLCV candle logic** (the industry-standard method):

1. You provide a symbol and date/time
2. StockScan fetches the candle data that CONTAINS that time
3. Returns the CLOSE price of that candle
4. This is the same method used by professional trading platforms

**Data Sources:**
- **Crypto**: Binance Public API (no key needed) - 16 timeframes available
- **Stocks**: Yahoo Finance API (no key needed) - 3 timeframes available
- **Commodities**: Yahoo Finance API (no key needed) - 3 timeframes available

---

## 💡 Examples

Navigate to the stockscan folder first:
```bash
cd stockscan
```

### Check Apple Stock (Daily)
```bash
python stockscan.py stock AAPL 2026-01-15 --timeframe 1d
# Output: $258.21 (Close price)
# Change: -$2.44 (-0.94%)
```

### Check Apple Stock (Weekly)
```bash
python stockscan.py stock AAPL 2024-01-15 --timeframe 1wk
# Output: $191.56 (Close price)
# Change: +$9.40 (+5.16%)
```

### Check Indian Stock NSE (Monthly)
```bash
python stockscan.py stock TCS.NS 2024-12-20 --timeframe 1mo
# Output: ₹3,712.45 (Close price)
# Change: +₹245.30 (+7.08%)
```

### Check Indian Stock NSE (Daily)
```bash
python stockscan.py stock INFY.NS 2023-08-05 --timeframe 1d
# Output: ₹1,542.30 (Close price)
# Change: +₹18.75 (+1.23%)
```

### Check Indian Stock BSE (Weekly)
```bash
python stockscan.py stock HDFCBANK.BO 2024-03-18 --timeframe 1wk
# Output: ₹1,598.25 (Close price)
# Change: +₹45.60 (+2.94%)
```

### Check Bitcoin Price
```bash
python stockscan.py crypto BTCUSDT 2026-01-15 14:30 --timeframe 1h
# Output: $97,040.75 (Close price)
# Change: +$397.74 (+0.41%)
```

### Check Ethereum Price
```bash
python stockscan.py crypto ETHUSDT 2026-01-15 10:00 --timeframe 5m
# Output: $3,302.39 (Close price)
# Change: +$2.23 (+0.07%)
```

### Check Gold Price (Commodity)
```bash
python stockscan.py commodity GLD 2024-01-15 --timeframe 1d
# Output: $189.71 (Close price)
# Change: -$0.96 (-0.50%)
```

### Check Oil Price (Commodity - Weekly)
```bash
python stockscan.py commodity USO 2024-01-01 --timeframe 1wk
# Output: $72.81 (Close price)
# Change: +$5.25 (+7.77%)
```

### Check Corn Price (Commodity - Monthly)
```bash
python stockscan.py commodity CORN 2024-01-01 --timeframe 1mo
# Output: $20.61 (Close price)
# Change: -$0.44 (-2.09%)
```

**Windows users:** Replace `python` with `py` if the above doesn't work

---

## 🎯 Supported Assets & How to Find Symbols

### 📊 Stocks

**US Stocks:**
- Format: Just the ticker symbol (e.g., `AAPL`, `TSLA`, `MSFT`)
- Find symbols: [Yahoo Finance](https://finance.yahoo.com/) - Search for any company

**Indian Stocks:**
- Format: Symbol + `.NS` (NSE) or `.BO` (BSE)
- Examples: `RELIANCE.NS`, `TCS.NS`, `INFY.BO`
- Find symbols: [NSE India](https://www.nseindia.com/) or [BSE India](https://www.bseindia.com/)
- Prices shown in ₹ (Rupees)

**Other International Stocks:**
- Most international stocks work with Yahoo Finance format
- Find symbols: Search on [Yahoo Finance](https://finance.yahoo.com/)

**Popular US Stocks:**
- AAPL (Apple)
- TSLA (Tesla)
- MSFT (Microsoft)
- GOOGL (Google)
- AMZN (Amazon)
- META (Meta/Facebook)
- NVDA (NVIDIA)

**Popular Indian Stocks:**
- RELIANCE.NS (Reliance Industries)
- TCS.NS (Tata Consultancy Services)
- INFY.NS (Infosys)
- HDFCBANK.NS (HDFC Bank)
- ICICIBANK.NS (ICICI Bank)
- SBIN.NS (State Bank of India)
- ITC.NS (ITC Limited)

### 💰 Crypto

**Format:** Trading pair on Binance (e.g., `BTCUSDT`, `ETHUSDT`)
- Most crypto symbols end with `USDT` (Tether)
- Find all symbols: [Binance Markets](https://www.binance.com/en/markets)

**Popular Crypto Pairs:**
- BTCUSDT (Bitcoin)
- ETHUSDT (Ethereum)
- BNBUSDT (Binance Coin)
- ADAUSDT (Cardano)
- SOLUSDT (Solana)
- XRPUSDT (Ripple)
- DOGEUSDT (Dogecoin)
- MATICUSDT (Polygon)

**How to find crypto symbols:**
1. Go to [Binance Spot Markets](https://www.binance.com/en/markets)
2. Search for your coin
3. Use the trading pair (usually ends with USDT)
4. Example: Bitcoin → BTC/USDT → Use `BTCUSDT`

### 🏆 Commodities

**Format:** Commodity ETF symbol (e.g., `GLD`, `USO`, `CORN`)
- 98+ commodity ETFs available
- Track prices of Gold, Silver, Oil, Natural Gas, Agriculture, Metals & more
- Find all symbols: Run `python stockscan.py list commodities`

**Popular Commodity ETFs:**

**Precious Metals:**
- GLD (SPDR Gold Shares)
- IAU (iShares Gold Trust)
- SLV (iShares Silver Trust)
- PPLT (abrdn Physical Platinum Shares)
- PALL (abrdn Physical Palladium Shares)

**Energy:**
- USO (United States Oil Fund)
- UNG (United States Natural Gas Fund)
- UCO (ProShares Ultra Bloomberg Crude Oil)
- UGA (United States Gasoline Fund)

**Agriculture:**
- CORN (Teucrium Corn Fund)
- WEAT (Teucrium Wheat Fund)
- SOYB (Teucrium Soybean Fund)
- DBA (Invesco DB Agriculture Fund)

**Industrial Metals:**
- CPER (United States Copper Index Fund)
- JJU (iPath Series B Bloomberg Aluminum)

**Broad Baskets:**
- DBC (Invesco DB Commodity Index Tracking Fund)
- PDBC (Invesco Optimum Yield Diversified Commodity)
- GSG (iShares S&P GSCI Commodity-Indexed Trust)

**How to find commodity symbols:**
1. Run: `python stockscan.py list commodities`
2. Browse 98+ commodity ETFs organized by category
3. Use the symbol shown (e.g., GLD, USO, CORN)

**Note:** Commodities use the same timeframes as stocks (1d, 1wk, 1mo) with full historical data.

---

## 🔍 Symbol Lookup Resources

**Need help finding the right symbol?**

### 📥 Complete Downloadable Lists (ALL Symbols)

| Market | Complete List | Format | Link |
|--------|--------------|--------|------|
| **US Stocks (ALL)** | NASDAQ FTP Server | CSV/TXT | ftp://ftp.nasdaqtrader.com/symboldirectory/ |
| **US Stocks (ALL)** | Symbol List IO | JSON/CSV | https://symbol-list.io/ |
| **US Stocks (ALL)** | Stock Screener | Web/Export | https://stock-screener.org/stock-list.aspx |
| **Indian Stocks (NSE)** | NSE Bhavcopy | CSV | https://www.nseindia.com/all-reports |
| **Indian Stocks (NSE)** | NSE Market Cap List | Excel/CSV | https://www.nseindia.com/regulations/listing-compliance/nse-market-capitalisation-all-companies |
| **Indian Stocks (BSE)** | BSE Listed Companies | Excel | https://www.bseindia.com/corporates/List_Scrips.aspx |
| **Crypto (Binance ALL)** | Binance API | JSON | https://api.binance.com/api/v3/exchangeInfo |
| **Crypto (ALL)** | CoinMarketCap | Web/API | https://coinmarketcap.com/ |

### 🎯 How to Download Complete Lists

**US Stocks (NASDAQ + NYSE + AMEX):**
1. **Option 1 - NASDAQ FTP (Most Complete):**
   - Go to: ftp://ftp.nasdaqtrader.com/symboldirectory/
   - Download: `nasdaqlisted.txt` (NASDAQ stocks)
   - Download: `otherlisted.txt` (NYSE, AMEX stocks)
   - Format: Pipe-delimited text file with ALL symbols

2. **Option 2 - Symbol List IO:**
   - Visit: https://symbol-list.io/
   - Download JSON or CSV with all US stocks
   - Updated daily

**Indian Stocks (NSE):**
1. Visit: https://www.nseindia.com/all-reports
2. Scroll to "Equity Bhavcopy"
3. Select date and download CSV
4. Contains ALL NSE stocks with symbols
5. Add `.NS` to symbol for StockScan (e.g., `RELIANCE` → `RELIANCE.NS`)

**Indian Stocks (BSE):**
1. Visit: https://www.bseindia.com/corporates/List_Scrips.aspx
2. Download Excel file with all BSE companies
3. Add `.BO` to symbol for StockScan (e.g., `RELIANCE` → `RELIANCE.BO`)

**Crypto (Binance - ALL 1000+ Pairs):**
1. **Option 1 - Direct API (Easiest):**
   - Open: https://api.binance.com/api/v3/exchangeInfo
   - This JSON file contains ALL Binance trading pairs
   - Look for `"symbol"` field in each entry
   - Use symbols ending with `USDT` (e.g., `BTCUSDT`, `ETHUSDT`)

2. **Option 2 - Binance Website:**
   - Visit: https://www.binance.com/en/markets
   - Browse all pairs
   - Use the symbol shown (e.g., BTC/USDT → `BTCUSDT`)

### 🔎 Quick Search Tools (No Download Needed)

**For ANY Stock:**
- Yahoo Finance Lookup: https://finance.yahoo.com/lookup
- Just search company name, copy the symbol

**For Crypto:**
- Binance Markets: https://www.binance.com/en/markets
- Search your coin, use the USDT pair

### 💡 Pro Tips

1. **US Stocks**: Use the symbol exactly as shown (e.g., `AAPL`, `TSLA`)
2. **Indian Stocks**: Add `.NS` for NSE or `.BO` for BSE (e.g., `RELIANCE.NS`)
3. **Crypto**: Use Binance spot pairs ending with USDT (e.g., `BTCUSDT`)
4. **When in doubt**: Search on Yahoo Finance first - that symbol works in StockScan!

---

## ⏱️ Timeframes

### Crypto (Binance) - 16 Timeframes
- `1s` - 1 second candles
- `1m` - 1 minute candles
- `3m` - 3 minute candles
- `5m` - 5 minute candles
- `15m` - 15 minute candles
- `30m` - 30 minute candles
- `1h` - 1 hour candles
- `2h` - 2 hour candles
- `4h` - 4 hour candles
- `6h` - 6 hour candles
- `8h` - 8 hour candles
- `12h` - 12 hour candles
- `1d` - Daily candles
- `3d` - 3 day candles
- `1w` - Weekly candles
- `1M` - Monthly candles

*All 16 Binance timeframes supported with full historical data!*

### Stocks (Yahoo Finance) - 3 Timeframes
- `1d` - Daily candles (full history)
- `1wk` - Weekly candles (full history)
- `1mo` - Monthly candles (full history)

*All timeframes support full historical data - no limitations!*

### Commodities (Yahoo Finance) - 3 Timeframes
- `1d` - Daily candles (full history)
- `1wk` - Weekly candles (full history)
- `1mo` - Monthly candles (full history)

*Same as stocks - full historical data with no limitations!*

---

## ❓ FAQ

**Q: Do I need to register or get API keys?**  
A: No! Everything works out of the box.

**Q: Is it free?**  
A: Yes, completely free. No hidden costs.

**Q: What if I enter a wrong date format?**  
A: StockScan will show you a warning and ask you to try again.

**Q: Can I check future prices?**  
A: No, it will show: "Future price data does not exist."

**Q: What if the market was closed on my date?**  
A: For stocks, it will show the closest trading day.

**Q: Can I check the current live price?**  
A: Yes! After viewing historical data, choose option [1] to see the current market price.

**Q: Can I compare historical price with current price?**  
A: Yes! After viewing historical data, choose option [2] to see a detailed comparison with P&L, percentage change, and time period.

**Q: How accurate is the live price?**  
A: Very accurate! Crypto has 1-2 minute delay (Binance), Stocks/Commodities have ~15 minute delay (Yahoo Finance).

**Q: What if I enter a wrong stock symbol?**  
A: StockScan will show an error message. Note that StockScan doesn't cover very small-cap stocks and very newly listed IPOs. Please verify the symbol is correct and the company has sufficient trading history.

**Q: What stocks are NOT supported?**  
A: StockScan doesn't cover:
   - Very small-cap/micro-cap stocks (extremely small companies)
   - Very newly listed IPOs (companies that just went public)
   - Unlisted/private companies (not traded on exchanges)
   
   All major large-cap and mid-cap stocks are fully supported!

**Q: How accurate is the data?**  
A: Very accurate! Data comes directly from Binance and Yahoo Finance.

---

## 🛠️ Requirements

- Python 3.7 or higher
- `requests` library (install with `pip install requests`)

That's it!

---

## 📝 License & Copyright

**MIT License**

Copyright © 2026 **Prasidh P Shetty**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

**For full license details, see the [LICENSE](LICENSE) file.**

---

## 👨‍💻 Author

**Prasidh P Shetty**

- 🌐 Portfolio: [prasidhshetty.in](https://prasidhshetty.in)
- 💻 GitHub: [@prasidhpshetty7](https://github.com/prasidhpshetty7)
- 📧 For queries and support, visit my portfolio

---

## 🤝 Contributing

Found a bug? Have a suggestion? Feel free to open an issue or submit a pull request!

Contributions are welcome! Please feel free to submit a Pull Request.

---

## ⭐ Show Your Support

If you find StockScan useful, give it a star! ⭐

---

## 📞 Support

Having issues? Check out:
1. [QUICKSTART.md](QUICKSTART.md) - Beginner's guide
2. [WHAT_HAPPENS.md](WHAT_HAPPENS.md) - Visual walkthrough
3. Open an issue on GitHub

---

**Made with ❤️ by [Prasidh P Shetty](https://prasidhshetty.in)**

🚀 Download, run, and start checking prices in seconds!
