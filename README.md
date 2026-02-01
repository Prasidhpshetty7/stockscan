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
```bash
python stockscan.py
```

That's it! No API keys, no configuration, no hassle.

---

## 🎮 How to Use

### Interactive Mode (Easiest)

Just run without arguments:
```bash
python stockscan.py
```

You'll see:
1. ✨ Big purple STOCKSCAN banner
2. 📋 Choose: `[1] Stocks` or `[2] Crypto`
3. 📝 Enter your lookup (e.g., `AAPL 2026-01-15`)
4. 💵 Get the price instantly!

### Command Line Mode (Fastest)

**Stocks:**
```bash
python stockscan.py stock AAPL 2026-01-15
python stockscan.py stock TSLA 2024-12-20
```

**Crypto:**
```bash
python stockscan.py crypto BTCUSDT 2026-01-15 14:30 --timeframe 1h
python stockscan.py crypto ETHUSDT 2026-01-15 10:00 --timeframe 5m
```

---

## 📸 Example Output

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

Note: This uses OHLCV candle logic. The CLOSE price of the daily
      candle for your requested date is shown as the price.

──────────────────────────────────────────────────────────────────────
```

---

## 🔧 Features

✅ **No API Keys Required** - Works immediately after download  
✅ **1000+ Cryptocurrencies** - All Binance spot pairs  
✅ **All US Stocks** - NYSE, NASDAQ, AMEX  
✅ **Multiple Timeframes** - 1m, 5m, 15m, 1h, 1d for crypto  
✅ **Historical Data** - Check any past date  
✅ **Beautiful UI** - Colorful terminal output  
✅ **Error Handling** - Clear warnings and helpful messages  
✅ **Interactive & CLI Modes** - Use whichever you prefer  

---

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Step-by-step guide for beginners
- **[DEMO.md](DEMO.md)** - Detailed examples and screenshots
- Run `python stockscan.py help` - See all commands

---

## 🎓 How It Works

StockScan uses **OHLCV candle logic** (the same method as CryptoFetch):

1. You provide a symbol and date/time
2. StockScan fetches the candle data that CONTAINS that time
3. Returns the CLOSE price of that candle
4. This is the standard method for historical price lookups

**Data Sources:**
- **Crypto**: Binance Public API (no key needed)
- **Stocks**: Yahoo Finance API (no key needed)

---

## 💡 Examples

### Check Apple Stock
```bash
python stockscan.py stock AAPL 2026-01-15
# Output: $258.21
```

### Check Bitcoin Price
```bash
python stockscan.py crypto BTCUSDT 2026-01-15 14:30 --timeframe 1h
# Output: $97,040.75
```

### Check Tesla Stock
```bash
python stockscan.py stock TSLA 2024-12-20
# Output: $421.06
```

### Check Ethereum Price
```bash
python stockscan.py crypto ETHUSDT 2026-01-15 10:00 --timeframe 5m
# Output: $3,302.39
```

---

## 🎯 Supported Assets

### Stocks
All US stocks including:
- AAPL (Apple)
- TSLA (Tesla)
- MSFT (Microsoft)
- GOOGL (Google)
- AMZN (Amazon)
- And thousands more...

### Crypto
All Binance spot pairs including:
- BTCUSDT (Bitcoin)
- ETHUSDT (Ethereum)
- BNBUSDT (Binance Coin)
- ADAUSDT (Cardano)
- SOLUSDT (Solana)
- And 1000+ more...

---

## ⏱️ Timeframes (Crypto Only)

- `1m` - 1 minute candles
- `5m` - 5 minute candles
- `15m` - 15 minute candles
- `1h` - 1 hour candles
- `1d` - Daily candles

*Note: Stocks only support daily data (free tier limitation)*

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

## 📝 License

MIT License - Free to use and modify

---

## 🤝 Contributing

Found a bug? Have a suggestion? Feel free to open an issue or submit a pull request!

---

## ⭐ Show Your Support

If you find StockScan useful, give it a star! ⭐

---

## 📞 Support

Having issues? Check out:
1. [QUICKSTART.md](QUICKSTART.md) - Beginner's guide
2. [DEMO.md](DEMO.md) - Detailed examples
3. Run `python stockscan.py help` - See all commands

---

**Made with ❤️ for traders, investors, and crypto enthusiasts**

🚀 Download, run, and start checking prices in seconds!
