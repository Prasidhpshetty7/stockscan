# 📈 StockScan

**Get the exact price of any crypto or stock at any point in time - instantly!**

No API keys. No registration. Just download and run.

---

## 🎯 What Does It Do?

StockScan answers one simple question: **"What was the price at this exact time?"**

- 📊 **Stocks**: Check any US stock (AAPL, TSLA, MSFT, etc.)
- 💰 **Crypto**: Check any Binance coin (BTC, ETH, BNB, etc.)
- 🕐 **Any Time**: Historical prices from any date/time
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
2. 📋 Choose: `[1] Stocks` or `[2] Crypto`
3. 📝 Enter your lookup (e.g., `AAPL 2026-01-15`)
4. 💵 Get the price instantly!

### Command Line Mode (Fastest)

Navigate to the stockscan folder first:
```bash
cd stockscan
```

**Stocks:**
```bash
python stockscan.py stock AAPL 2026-01-15 --timeframe 1d
python stockscan.py stock TSLA 2024-12-20 --timeframe 1wk
python stockscan.py stock RELIANCE.NS 2024-01-15 --timeframe 1mo
```

**Crypto:**
```bash
python stockscan.py crypto BTCUSDT 2026-01-15 14:30 --timeframe 1h
python stockscan.py crypto ETHUSDT 2026-01-15 10:00 --timeframe 5m
```

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

**Example**: If a stock opened at $100 and closed at $105:
- Change: +$5.00 (gained $5)
- Percentage: +5.00% (gained 5%)

---

## 🔧 Features

✅ **No API Keys Required** - Works immediately after download  
✅ **1000+ Cryptocurrencies** - All Binance spot pairs  
✅ **All US & Indian Stocks** - NYSE, NASDAQ, AMEX, NSE, BSE  
✅ **Multiple Timeframes** - Crypto: 16 timeframes (1s to 1M) | Stocks: 3 timeframes (1d, 1wk, 1mo)  
✅ **Historical Data** - Check any past date with full history  
✅ **Weekly/Monthly Periods** - Shows full calendar periods with trading day counts  
✅ **Price Movement Calculator** - Shows change and percentage gain/loss  
✅ **Smart Holiday Detection** - Warns about weekends and holidays in the period  
✅ **Beautiful UI** - Colorful terminal output with color-coded gains/losses  
✅ **Error Handling** - Clear warnings and helpful messages  
✅ **Interactive & CLI Modes** - Use whichever you prefer  

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

### Check Indian Stock (Monthly)
```bash
python stockscan.py stock RELIANCE.NS 2024-01-15 --timeframe 1mo
# Output: ₹1,426.62 (Close price)
# Change: +₹136.35 (+10.57%)
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
