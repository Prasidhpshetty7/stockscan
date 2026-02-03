#!/usr/bin/env python3
"""
StockScan - Terminal-based Market Price Lookup Tool
Get crypto and stock prices at any point in time

Copyright (c) 2026 Prasidh P Shetty
GitHub: https://github.com/prasidhpshetty7
Portfolio: https://prasidhshetty.in

Licensed under the MIT License
"""

import sys
import os
import argparse
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List

# Try to import requests, provide helpful error if not available
try:
    import requests
except ImportError:
    print("\nError: 'requests' library not installed")
    print("Install it with: pip install requests")
    print("Or: python -m pip install requests\n")
    sys.exit(1)

# ANSI Color Codes (Purple Theme)
PURPLE = '\033[95m'
BRIGHT_PURPLE = '\033[1;35m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'
DIM = '\033[2m'

# API Configuration
BINANCE_BASE = "https://api.binance.com/api/v3"
FINNHUB_BASE = "https://finnhub.io/api/v1"
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY", "")
ALPHAVANTAGE_BASE = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", "demo")


def print_banner():
    """Print beautiful purple ASCII banner"""
    banner = f"""
{BRIGHT_PURPLE}╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║  ███████╗████████╗ ██████╗  ██████╗██╗  ██╗███████╗ ██████╗ █████╗ ███╗   ██╗ ║
║  ██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║ ║
║  ███████╗   ██║   ██║   ██║██║     █████╔╝ ███████╗██║     ███████║██╔██╗ ██║ ║
║  ╚════██║   ██║   ██║   ██║██║     ██╔═██╗ ╚════██║██║     ██╔══██║██║╚██╗██║ ║
║  ███████║   ██║   ╚██████╔╝╚██████╗██║  ██╗███████║╚██████╗██║  ██║██║ ╚████║ ║
║  ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝{RESET}

{PURPLE}                       Market Price Lookup Tool{RESET}
{DIM}                   Get crypto & stock prices at any time{RESET}
"""
    print(banner)


def print_description():
    """Print what StockScan does"""
    desc = f"""
{CYAN}What is StockScan?{RESET}
  StockScan lets you look up the exact price of any crypto or stock
  at a specific date and time using OHLCV candle logic.

{CYAN}How it works:{RESET}
  • Fetches OHLCV (Open, High, Low, Close, Volume) candle data
  • Finds the candle that CONTAINS your requested time
  • Returns the CLOSE price as the price at that time
  • This is the standard method used by professional trading tools

{CYAN}Data Sources:{RESET}
  • Crypto: Binance (1000+ coins, NO API KEY NEEDED)
    - Supports: 1s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
  • Stocks: Yahoo Finance (all US & Indian stocks, NO API KEY NEEDED)
    - Supports: 1d (daily), 1wk (weekly), 1mo (monthly)
    - Works out of the box!
"""
    print(desc)


def print_usage():
    """Print usage instructions"""
    usage = f"""
{CYAN}Usage Examples:{RESET}

  {GREEN}# Get crypto price at specific time{RESET}
  python stockscan.py crypto BTCUSDT 2024-01-15 14:30 --timeframe 1h
  python stockscan.py crypto ETHUSDT 2024-01-15 --timeframe 1d

  {GREEN}# Get stock price with timeframe{RESET}
  python stockscan.py stock AAPL 2024-01-15 --timeframe 1d
  python stockscan.py stock TSLA 2024-01-10 --timeframe 1wk
  python stockscan.py stock RELIANCE.NS 2024-01-15 --timeframe 1mo

  {GREEN}# List all available crypto symbols{RESET}
  python stockscan.py list crypto

  {GREEN}# List all available stock symbols{RESET}
  python stockscan.py list stocks

  {GREEN}# Show help{RESET}
  python stockscan.py help

{CYAN}Supported Timeframes:{RESET}
  {BOLD}Crypto:{RESET} 1s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
  {BOLD}Stocks:{RESET} 1d (daily), 1wk (weekly), 1mo (monthly)

{CYAN}How it works:{RESET}
  • Uses OHLCV candle logic (industry-standard method)
  • Finds the candle that CONTAINS your requested time
  • Returns the CLOSE price of that candle
  • This is the standard method for historical price lookups

{GREEN}✅ NO API KEYS NEEDED!{RESET}
  Both crypto (Binance) and stocks (Yahoo Finance) work out of the box.
  Just download and run!

{DIM}Optional: For additional stock data sources, you can set API keys:
  • Alpha Vantage: https://www.alphavantage.co/support/#api-key
    Set it: $env:ALPHAVANTAGE_API_KEY="your_key"
  • Finnhub: https://finnhub.io/register
    Set it: $env:FINNHUB_API_KEY="your_key"{RESET}
"""
    print(usage)


def get_crypto_price(symbol: str, date_str: str, time_str: Optional[str] = None, timeframe: str = "5m") -> Dict[str, Any]:
    """
    Get crypto price from Binance at specific time using OHLCV candle logic.
    Finds the candle that CONTAINS the requested time and returns its CLOSE price.
    
    Args:
        symbol: Trading pair (e.g., BTCUSDT)
        date_str: Date in YYYY-MM-DD format
        time_str: Optional time in HH:MM format (default: 00:00)
        timeframe: Candle interval - 1m, 5m, 15m, 1h, 1d (default: 1m)
    
    Returns:
        Dict with price data or error
    """
    try:
        # Parse datetime
        if time_str:
            dt_str = f"{date_str} {time_str}"
            dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
        else:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
        
        # Check if future
        if dt > datetime.now():
            return {"error": "Future price data does not exist."}
        
        # Convert to milliseconds for Binance
        target_timestamp_ms = int(dt.timestamp() * 1000)
        
        # Calculate time window based on timeframe
        timeframe_ms = {
            "1s": 1000,
            "1m": 60000,
            "3m": 180000,
            "5m": 300000,
            "15m": 900000,
            "30m": 1800000,
            "1h": 3600000,
            "2h": 7200000,
            "4h": 14400000,
            "6h": 21600000,
            "8h": 28800000,
            "12h": 43200000,
            "1d": 86400000,
            "3d": 259200000,
            "1w": 604800000,
            "1M": 2592000000
        }
        
        interval = timeframe if timeframe in timeframe_ms else "1m"
        window = timeframe_ms[interval]
        
        # For weekly/monthly timeframes, start from exact date and go forward
        if interval in ["1w", "1M"]:
            # Start from the exact requested date
            start_time = target_timestamp_ms
            end_time = target_timestamp_ms + window
            
            url = f"{BINANCE_BASE}/klines"
            params = {
                "symbol": symbol,
                "interval": interval,
                "startTime": start_time,
                "endTime": end_time,
                "limit": 1
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                return {"error": "No data available for this time. Asset may not have existed yet."}
            
            target_candle = data[0]
            
            # Calculate actual period
            candle_open_time = dt  # Start from requested date
            candle_close_time = dt + timedelta(milliseconds=window)
        else:
            # For other timeframes, use the old logic (find candle containing the time)
            url = f"{BINANCE_BASE}/klines"
            params = {
                "symbol": symbol,
                "interval": interval,
                "startTime": target_timestamp_ms - (window * 2),  # Fetch candles before
                "endTime": target_timestamp_ms + (window * 2),    # and after target time
                "limit": 10
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                return {"error": "No data available for this time. Asset may not have existed yet."}
            
            # Find the candle that CONTAINS the target time
            # Candle structure: [open_time, open, high, low, close, volume, close_time, ...]
            target_candle = None
            for candle in data:
                candle_open_time_ms = candle[0]
                candle_close_time_ms = candle[6]
                
                # Check if target time falls within this candle
                if candle_open_time_ms <= target_timestamp_ms < candle_close_time_ms:
                    target_candle = candle
                    break
            
            # If no exact match, use the closest candle
            if not target_candle:
                target_candle = min(data, key=lambda c: abs(c[0] - target_timestamp_ms))
            
            # Extract candle data
            candle_open_time = datetime.fromtimestamp(target_candle[0] / 1000)
            candle_close_time = datetime.fromtimestamp(target_candle[6] / 1000)
        
        return {
            "symbol": symbol,
            "market": "Crypto (Binance)",
            "requested_time": dt.strftime("%Y-%m-%d %H:%M UTC"),
            "timeframe": interval,
            "candle_start": candle_open_time.strftime("%Y-%m-%d %H:%M UTC"),
            "candle_end": candle_close_time.strftime("%Y-%m-%d %H:%M UTC"),
            "open": float(target_candle[1]),
            "high": float(target_candle[2]),
            "low": float(target_candle[3]),
            "close": float(target_candle[4]),  # This is the price at that time
            "volume": float(target_candle[5])
        }
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch data from Binance: {str(e)}"}
    except ValueError as e:
        return {"error": f"Invalid date/time format: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


def get_stock_price(symbol: str, date_str: str, time_str: Optional[str] = None, timeframe: str = "1d") -> Dict[str, Any]:
    """
    Get stock price at specific date using OHLCV candle logic.
    Supports multiple timeframes with full historical data.
    
    Args:
        symbol: Stock symbol (e.g., AAPL, RELIANCE.NS)
        date_str: Date in YYYY-MM-DD format
        time_str: Ignored for stocks (not used)
        timeframe: Candle interval - 1d, 1wk, 1mo (default: 1d)
    
    Returns:
        Dict with price data or error
    """
    # Try Yahoo Finance (supports all timeframes, no API key needed!)
    result = get_stock_price_yahoo(symbol, date_str, time_str, timeframe)
    if "error" not in result:
        return result
    
    # If Yahoo Finance failed, return error
    return {
        "error": "Unable to fetch stock data from Yahoo Finance.\n" +
                 "Please check the symbol and try again."
    }


def get_stock_price_yahoo(symbol: str, date_str: str, time_str: Optional[str] = None, timeframe: str = "1d") -> Dict[str, Any]:
    """
    Get stock price from Yahoo Finance (no API key needed!)
    Supports multiple timeframes: 1d (daily), 1wk (weekly), 1mo (monthly)
    """
    try:
        # Parse date
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        
        # Check if future
        if dt > datetime.now():
            return {"error": "Future price data does not exist."}
        
        # Map timeframe to Yahoo Finance interval
        interval_map = {
            "1d": "1d",
            "1wk": "1wk",
            "1mo": "1mo"
        }
        
        interval = interval_map.get(timeframe, "1d")
        
        # For weekly/monthly timeframes, fetch DAILY data and aggregate
        if timeframe in ["1wk", "1mo"]:
            # Fetch daily data for the period
            start_dt = dt
            
            # Calculate end date based on timeframe
            if timeframe == "1wk":
                end_dt = dt + timedelta(days=7)
            else:  # 1mo
                end_dt = dt + timedelta(days=30)
            
            period1 = int(start_dt.timestamp())
            period2 = int(end_dt.timestamp())
            
            # Fetch DAILY data (not weekly/monthly)
            fetch_interval = "1d"
        else:
            # Daily - use old logic
            days_before = 7
            days_after = 1
            
            start_dt = dt - timedelta(days=days_before)
            end_dt = dt + timedelta(days=days_after)
            
            period1 = int(start_dt.timestamp())
            period2 = int(end_dt.timestamp())
            fetch_interval = interval
        
        # Yahoo Finance API endpoint
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        params = {
            "period1": period1,
            "period2": period2,
            "interval": fetch_interval,
            "events": "history"
        }
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Check for errors
        if "chart" not in data or "result" not in data["chart"]:
            return {"error": "Invalid response from Yahoo Finance"}
        
        result = data["chart"]["result"]
        if not result or len(result) == 0:
            return {"error": f"No data found for symbol {symbol}"}
        
        quote = result[0]
        
        if "timestamp" not in quote or "indicators" not in quote:
            return {"error": "Invalid data format from Yahoo Finance"}
        
        timestamps = quote["timestamp"]
        indicators = quote["indicators"]["quote"][0]
        
        if not timestamps or not indicators:
            return {"error": "No price data available"}
        
        # Find the data for our target period
        if timeframe in ["1wk", "1mo"]:
            # For weekly/monthly, aggregate daily data into one candle
            if not timestamps or len(timestamps) == 0:
                return {"error": "No price data available for this period"}
            
            # Aggregate all daily candles into one
            opens = [indicators["open"][i] for i in range(len(timestamps)) if indicators["open"][i] is not None]
            highs = [indicators["high"][i] for i in range(len(timestamps)) if indicators["high"][i] is not None]
            lows = [indicators["low"][i] for i in range(len(timestamps)) if indicators["low"][i] is not None]
            closes = [indicators["close"][i] for i in range(len(timestamps)) if indicators["close"][i] is not None]
            volumes = [indicators["volume"][i] for i in range(len(timestamps)) if indicators["volume"][i] is not None]
            
            if not opens or not closes:
                return {"error": "Incomplete data for this period"}
            
            # Create aggregated candle
            open_price = opens[0]  # First open
            high_price = max(highs)  # Highest high
            low_price = min(lows)  # Lowest low
            close_price = closes[-1]  # Last close
            volume = sum(volumes)  # Total volume
            
            candle_start_date = datetime.fromtimestamp(timestamps[0]).strftime("%Y-%m-%d")
            candle_end_date = datetime.fromtimestamp(timestamps[-1]).strftime("%Y-%m-%d")
        else:
            # Daily - find the closest date to our target
            target_ts = int(dt.timestamp())
            closest_idx = 0
            min_diff = float('inf')
            
            for i, ts in enumerate(timestamps):
                # Convert timestamp to date and compare
                ts_date = datetime.fromtimestamp(ts).date()
                target_date = dt.date()
                
                # Daily - exact match preferred
                if ts_date == target_date:
                    closest_idx = i
                    break
                
                diff = abs(ts - target_ts)
                if diff < min_diff and ts <= target_ts + 86400:  # Within 1 day after
                    min_diff = diff
                    closest_idx = i
            
            candle_start_date = datetime.fromtimestamp(timestamps[closest_idx]).strftime("%Y-%m-%d")
            candle_end_date = None  # Not used for daily
            
            open_price = indicators["open"][closest_idx]
            high_price = indicators["high"][closest_idx]
            low_price = indicators["low"][closest_idx]
            close_price = indicators["close"][closest_idx]
            volume = indicators["volume"][closest_idx]
        
        # Check for None values
        if None in [open_price, high_price, low_price, close_price, volume]:
            return {"error": f"Incomplete data for {date_str}. Market may have been closed."}
        
        # Map timeframe to display name
        timeframe_display = {
            "1d": "Daily",
            "1wk": "Weekly",
            "1mo": "Monthly"
        }
        
        result = {
            "symbol": symbol,
            "market": "Stocks (Yahoo Finance)",
            "requested_date": date_str,
            "candle_start_date": candle_start_date,
            "candle_end_date": candle_end_date,
            "timeframe": timeframe_display.get(timeframe, "Daily"),
            "open": float(open_price),
            "high": float(high_price),
            "low": float(low_price),
            "close": float(close_price),
            "volume": float(volume)
        }
        
        # Add note if date was adjusted (only for daily)
        if timeframe == "1d" and candle_start_date != date_str:
            result["note"] = f"Market was closed on {date_str}. Showing closest trading day."
        
        return result
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch from Yahoo Finance: {str(e)}"}
    except (KeyError, IndexError, TypeError) as e:
        return {"error": f"Error parsing Yahoo Finance data: {str(e)}"}
    except ValueError as e:
        return {"error": f"Invalid date format: {str(e)}"}
    except Exception as e:
        return {"error": f"Yahoo Finance error: {str(e)}"}


def get_stock_price_alphavantage(symbol: str, date_str: str, time_str: Optional[str] = None) -> Dict[str, Any]:
    """Get stock price from Alpha Vantage API"""
    try:
        # Parse date
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        
        # Check if future
        if dt > datetime.now():
            return {"error": "Future price data does not exist."}
        
        # Fetch daily time series
        url = ALPHAVANTAGE_BASE
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": ALPHAVANTAGE_API_KEY,
            "outputsize": "compact"  # Last 100 days
        }
        
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        # Check for API errors
        if "Error Message" in data:
            return {"error": f"Invalid symbol or API error: {data['Error Message']}"}
        
        if "Note" in data:
            return {"error": "API rate limit reached. Please wait a minute or get a free API key."}
        
        if "Time Series (Daily)" not in data:
            return {"error": "No data available from Alpha Vantage."}
        
        time_series = data["Time Series (Daily)"]
        
        # Find the exact date or closest date
        if date_str in time_series:
            candle_data = time_series[date_str]
            candle_date = date_str
        else:
            # Find closest date (market might be closed on requested date)
            available_dates = sorted(time_series.keys(), reverse=True)
            closest_date = None
            for d in available_dates:
                if d <= date_str:
                    closest_date = d
                    break
            
            if not closest_date:
                return {"error": f"No data available for {date_str}. Market may not have been open."}
            
            candle_data = time_series[closest_date]
            candle_date = closest_date
        
        result = {
            "symbol": symbol,
            "market": "Stocks (Alpha Vantage)",
            "requested_date": date_str,
            "candle_date": candle_date,
            "timeframe": "Daily",
            "open": float(candle_data["1. open"]),
            "high": float(candle_data["2. high"]),
            "low": float(candle_data["3. low"]),
            "close": float(candle_data["4. close"]),
            "volume": float(candle_data["5. volume"])
        }
        
        # Add note if time was provided or date was adjusted
        if time_str:
            result["note"] = "Stocks use daily data on free tier. Time parameter ignored."
        elif candle_date != date_str:
            result["note"] = f"Market was closed on {date_str}. Showing closest trading day."
        
        return result
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch from Alpha Vantage: {str(e)}"}
    except ValueError as e:
        return {"error": f"Invalid date format: {str(e)}"}
    except Exception as e:
        return {"error": f"Alpha Vantage error: {str(e)}"}


def get_stock_price_finnhub(symbol: str, date_str: str, time_str: Optional[str] = None) -> Dict[str, Any]:
    """Get stock price from Finnhub API"""
    if not FINNHUB_API_KEY:
        return {"error": "FINNHUB_API_KEY not set."}
    
    try:
        # Parse date
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        
        # Check if future
        if dt > datetime.now():
            return {"error": "Future price data does not exist."}
        
        # Convert to unix timestamp (start of day)
        timestamp = int(dt.timestamp())
        
        # Fetch candle data (daily) - get a few days around target
        url = f"{FINNHUB_BASE}/stock/candle"
        params = {
            "symbol": symbol,
            "resolution": "D",
            "from": timestamp - (86400 * 3),  # 3 days before
            "to": timestamp + (86400 * 3),    # 3 days after
            "token": FINNHUB_API_KEY
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("s") != "ok" or not data.get("c"):
            return {"error": "No data available for this date. Stock may not have existed yet."}
        
        # Find the candle for the target date
        target_candle_idx = None
        target_ts = timestamp
        min_diff = float('inf')
        
        for i, candle_ts in enumerate(data["t"]):
            # Check if this candle is for the target date
            candle_date = datetime.fromtimestamp(candle_ts).date()
            target_date = dt.date()
            
            if candle_date == target_date:
                target_candle_idx = i
                break
            
            # Track closest if exact match not found
            diff = abs(candle_ts - target_ts)
            if diff < min_diff:
                min_diff = diff
                target_candle_idx = i
        
        if target_candle_idx is None:
            return {"error": "No data available for this date."}
        
        idx = target_candle_idx
        candle_date = datetime.fromtimestamp(data["t"][idx]).strftime("%Y-%m-%d")
        
        result = {
            "symbol": symbol,
            "market": "Stocks (Finnhub)",
            "requested_date": date_str,
            "candle_date": candle_date,
            "timeframe": "Daily",
            "open": float(data["o"][idx]),
            "high": float(data["h"][idx]),
            "low": float(data["l"][idx]),
            "close": float(data["c"][idx]),
            "volume": float(data["v"][idx])
        }
        
        # Add note if time was provided
        if time_str:
            result["note"] = "Stocks use daily data on free tier. Time parameter ignored."
        
        return result
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch from Finnhub: {str(e)}"}
    except ValueError as e:
        return {"error": f"Invalid date format: {str(e)}"}
    except Exception as e:
        return {"error": f"Finnhub error: {str(e)}"}


def list_crypto_symbols(limit: int = 50) -> List[str]:
    """List available crypto symbols from Binance"""
    try:
        url = f"{BINANCE_BASE}/exchangeInfo"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        symbols = []
        for symbol_info in data.get("symbols", []):
            if (symbol_info.get("quoteAsset") == "USDT" and 
                symbol_info.get("status") == "TRADING" and
                symbol_info.get("isSpotTradingAllowed")):
                symbols.append(symbol_info.get("symbol"))
        
        return sorted(symbols)[:limit]
    
    except Exception as e:
        print(f"{RED}Error fetching crypto symbols: {e}{RESET}")
        return []


def list_stock_symbols(limit: int = 50) -> List[str]:
    """List available stock symbols from Finnhub"""
    if not FINNHUB_API_KEY:
        print(f"{RED}FINNHUB_API_KEY not set. Get free key at: https://finnhub.io/register{RESET}")
        return []
    
    try:
        url = f"{FINNHUB_BASE}/stock/symbol"
        params = {
            "exchange": "US",
            "token": FINNHUB_API_KEY
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        symbols = [stock["symbol"] for stock in data if stock.get("symbol")]
        return sorted(symbols)[:limit]
    
    except Exception as e:
        print(f"{RED}Error fetching stock symbols: {e}{RESET}")
        return []


def print_crypto_result(result: Dict[str, Any]):
    """Print crypto price result in CryptoFetch style with price change calculations"""
    if "error" in result:
        print(f"\n{RED}✗ Error: {result['error']}{RESET}\n")
        return
    
    # Calculate price change and percentage
    open_price = result['open']
    close_price = result['close']
    high_price = result['high']
    low_price = result['low']
    price_change = close_price - open_price
    percentage_change = (price_change / open_price) * 100 if open_price != 0 else 0
    
    # Check if absolutely no movement (possible holiday/no trading)
    no_movement = (open_price == close_price == high_price == low_price)
    
    # Determine color based on positive/negative change
    if price_change > 0:
        change_color = GREEN
        change_sign = "+"
    elif price_change < 0:
        change_color = RED
        change_sign = ""
    else:
        change_color = YELLOW
        change_sign = ""
    
    # Holiday warning if no movement at all
    holiday_warning = ""
    if no_movement and result['volume'] == 0:
        holiday_warning = f"\n{YELLOW}⚠ WARNING: No price movement detected. This day might be a holiday for crypto markets.{RESET}\n{DIM}   Check market reports to verify if trading was active on this date.{RESET}\n"
    
    output = f"""
{PURPLE}{'─' * 70}{RESET}
{BOLD}{BRIGHT_PURPLE}STOCKSCAN - CRYPTO PRICE LOOKUP{RESET}
{PURPLE}{'─' * 70}{RESET}

{CYAN}ASSET:{RESET}           {result['symbol']}
{CYAN}MARKET:{RESET}          {result['market']}
{CYAN}REQUESTED TIME:{RESET}  {result['requested_time']}
{CYAN}TIMEFRAME:{RESET}       {result['timeframe']}

{DIM}Candle Period:  {result['candle_start']} → {result['candle_end']}{RESET}

{CYAN}CANDLE DATA:{RESET}
  Open:   ${result['open']:,.8f}
  High:   ${result['high']:,.8f}
  Low:    ${result['low']:,.8f}
  {GREEN}{BOLD}Close:  ${result['close']:,.8f}  ← Price at that time{RESET}
  Volume: {result['volume']:,.2f}

{CYAN}PRICE MOVEMENT:{RESET}
  {change_color}{BOLD}Change:     {change_sign}${abs(price_change):,.8f}{RESET}
  {change_color}{BOLD}Percentage: {change_sign}{percentage_change:.2f}%{RESET}
{holiday_warning}
{DIM}Note: This uses OHLCV candle logic. The CLOSE price of the candle
      containing your requested time is shown as the price.
      Price movement shows the change from Open to Close.{RESET}

{PURPLE}{'─' * 70}{RESET}
"""
    print(output)


def print_stock_result(result: Dict[str, Any]):
    """Print stock price result in CryptoFetch style with price change calculations"""
    if "error" in result:
        print(f"\n{RED}✗ Error: {result['error']}{RESET}\n")
        return
    
    note_text = ""
    has_existing_warning = False
    if "note" in result:
        note_text = f"\n{YELLOW}⚠ {result['note']}{RESET}\n"
        has_existing_warning = True
    
    # Detect currency based on symbol
    symbol = result['symbol']
    if '.NS' in symbol or '.BO' in symbol:
        # Indian stocks (NSE or BSE)
        currency = '₹'
        market_name = 'Indian Stock Market'
        market_type = 'stock market'
    else:
        # US and other stocks
        currency = '$'
        market_name = result['market']
        market_type = 'stock market'
    
    # Calculate price change and percentage
    open_price = result['open']
    close_price = result['close']
    high_price = result['high']
    low_price = result['low']
    price_change = close_price - open_price
    percentage_change = (price_change / open_price) * 100 if open_price != 0 else 0
    
    # Check if absolutely no movement (possible holiday/no trading)
    no_movement = (open_price == close_price == high_price == low_price)
    
    # Determine color based on positive/negative change
    if price_change > 0:
        change_color = GREEN
        change_sign = "+"
    elif price_change < 0:
        change_color = RED
        change_sign = ""
    else:
        change_color = YELLOW
        change_sign = ""
    
    # Holiday warning ONLY if no existing warning AND no movement at all
    holiday_warning = ""
    if no_movement and result['volume'] == 0 and not has_existing_warning:
        holiday_warning = f"\n{YELLOW}⚠ WARNING: No price movement detected. This day might be a holiday for {market_type}.{RESET}\n{DIM}   Check market reports to verify if trading was active on this date.{RESET}\n"
    
    # Format candle date display based on timeframe
    if result.get('candle_end_date'):
        # Weekly or monthly - show period
        candle_date_display = f"{DIM}Candle Period:  {result['candle_start_date']} → {result['candle_end_date']}{RESET}"
    else:
        # Daily - show single date
        candle_date_display = f"{DIM}Candle Date:    {result['candle_start_date']}{RESET}"
    
    output = f"""
{PURPLE}{'─' * 70}{RESET}
{BOLD}{BRIGHT_PURPLE}STOCKSCAN - STOCK PRICE LOOKUP{RESET}
{PURPLE}{'─' * 70}{RESET}

{CYAN}ASSET:{RESET}           {result['symbol']}
{CYAN}MARKET:{RESET}          {market_name}
{CYAN}REQUESTED DATE:{RESET}  {result['requested_date']}
{CYAN}TIMEFRAME:{RESET}       {result['timeframe']}

{candle_date_display}
{note_text}
{CYAN}CANDLE DATA:{RESET}
  Open:   {currency}{result['open']:,.2f}
  High:   {currency}{result['high']:,.2f}
  Low:    {currency}{result['low']:,.2f}
  {GREEN}{BOLD}Close:  {currency}{result['close']:,.2f}  ← Price at that date{RESET}
  Volume: {result['volume']:,.0f}

{CYAN}PRICE MOVEMENT:{RESET}
  {change_color}{BOLD}Change:     {change_sign}{currency}{abs(price_change):,.2f}{RESET}
  {change_color}{BOLD}Percentage: {change_sign}{percentage_change:.2f}%{RESET}
{holiday_warning}
{DIM}Note: This uses OHLCV candle logic. The CLOSE price of the candle
      for your requested period is shown as the price.
      Price movement shows the change from Open to Close.{RESET}

{PURPLE}{'─' * 70}{RESET}
"""
    print(output)


def interactive_mode():
    """Interactive mode - guides user through price lookup"""
    print_banner()
    print_description()
    
    while True:
        # Ask which market
        print(f"\n{CYAN}{'─' * 70}{RESET}")
        print(f"{BOLD}{BRIGHT_PURPLE}Which market do you want to check?{RESET}\n")
        print(f"  {GREEN}[1]{RESET} Stocks  (AAPL, TSLA, MSFT, etc.)")
        print(f"  {GREEN}[2]{RESET} Crypto  (BTCUSDT, ETHUSDT, etc.)")
        print(f"  {YELLOW}[Q]{RESET} Quit\n")
        
        choice = input(f"{CYAN}Enter your choice (1/2/Q):{RESET} ").strip().upper()
        
        if choice == 'Q':
            print(f"\n{PURPLE}Thanks for using StockScan! Goodbye! 👋{RESET}\n")
            break
        
        if choice not in ['1', '2']:
            print(f"\n{RED}⚠ Invalid choice! Please enter 1 for Stocks, 2 for Crypto, or Q to quit.{RESET}")
            continue
        
        # Show syntax based on choice
        if choice == '1':
            # Stock mode
            print(f"\n{CYAN}{'─' * 70}{RESET}")
            print(f"{BOLD}{BRIGHT_PURPLE}STOCK PRICE LOOKUP{RESET}\n")
            print(f"{CYAN}Syntax:{RESET} {GREEN}<SYMBOL> <DATE> [TIMEFRAME]{RESET}")
            print(f"{CYAN}Examples:{RESET}")
            print(f"  AAPL 2026-01-15     {DIM}(Will ask for timeframe){RESET}")
            print(f"  AAPL 2026-01-15 1d  {DIM}(Direct with timeframe){RESET}")
            print(f"  TSLA 2024-12-20 1wk {DIM}(Weekly candle){RESET}\n")
            print(f"{DIM}Date format: YYYY-MM-DD{RESET}")
            print(f"{DIM}Type 'back' to return to market selection{RESET}\n")
            
            while True:
                user_input = input(f"{CYAN}Enter stock lookup:{RESET} ").strip()
                
                if user_input.lower() == 'back':
                    break
                
                if not user_input:
                    print(f"{RED}⚠ Please enter something!{RESET}")
                    continue
                
                parts = user_input.split()
                
                if len(parts) < 2:
                    print(f"{RED}⚠ Invalid syntax! Use: <SYMBOL> <DATE> [TIMEFRAME]{RESET}")
                    print(f"{YELLOW}Example: AAPL 2026-01-15{RESET}")
                    continue
                
                symbol = parts[0]
                date = parts[1]
                
                # Check if timeframe was provided
                timeframe = None
                valid_timeframes = ['1d', '1wk', '1mo']
                if len(parts) > 2 and parts[2] in valid_timeframes:
                    timeframe = parts[2]
                
                # If no timeframe provided, ask user to select
                if timeframe is None:
                    print(f"\n{CYAN}{'─' * 50}{RESET}")
                    print(f"{BOLD}{BRIGHT_PURPLE}SELECT TIMEFRAME{RESET}\n")
                    print(f"{CYAN}Available timeframes:{RESET}")
                    print(f"  {GREEN}[1]{RESET}  1d   - Daily")
                    print(f"  {GREEN}[2]{RESET}  1wk  - Weekly")
                    print(f"  {GREEN}[3]{RESET}  1mo  - Monthly\n")
                    
                    timeframe_map = {
                        '1': '1d',
                        '2': '1wk',
                        '3': '1mo'
                    }
                    
                    while True:
                        tf_choice = input(f"{CYAN}Select timeframe (1-3):{RESET} ").strip()
                        
                        if tf_choice in timeframe_map:
                            timeframe = timeframe_map[tf_choice]
                            break
                        else:
                            print(f"{RED}⚠ Invalid choice! Please enter a number between 1 and 3{RESET}")
                
                result = get_stock_price(symbol.upper(), date, None, timeframe)
                print_stock_result(result)
                
                # Ask if they want to check another
                print(f"\n{DIM}Press Enter to check another stock, or type 'back' to change market{RESET}")
                continue_choice = input().strip().lower()
                if continue_choice == 'back':
                    break
        
        else:  # choice == '2'
            # Crypto mode
            print(f"\n{CYAN}{'─' * 70}{RESET}")
            print(f"{BOLD}{BRIGHT_PURPLE}CRYPTO PRICE LOOKUP{RESET}\n")
            print(f"{CYAN}Syntax:{RESET} {GREEN}<SYMBOL> <DATE> <TIME> [TIMEFRAME]{RESET}")
            print(f"{CYAN}Examples:{RESET}")
            print(f"  BTCUSDT 2026-01-15 14:30     {DIM}(Will ask for timeframe){RESET}")
            print(f"  BTCUSDT 2026-01-15 14:30 1h  {DIM}(Direct with timeframe){RESET}")
            print(f"  ETHUSDT 2026-01-15 10:00 5m  {DIM}(Direct with timeframe){RESET}\n")
            print(f"{DIM}Date format: YYYY-MM-DD{RESET}")
            print(f"{DIM}Time format: HH:MM (optional for daily timeframe){RESET}")
            print(f"{DIM}Type 'back' to return to market selection{RESET}\n")
            
            while True:
                user_input = input(f"{CYAN}Enter crypto lookup:{RESET} ").strip()
                
                if user_input.lower() == 'back':
                    break
                
                if not user_input:
                    print(f"{RED}⚠ Please enter something!{RESET}")
                    continue
                
                parts = user_input.split()
                
                if len(parts) < 2:
                    print(f"{RED}⚠ Invalid syntax! Use: <SYMBOL> <DATE> [TIME] [TIMEFRAME]{RESET}")
                    print(f"{YELLOW}Example: BTCUSDT 2026-01-15 14:30{RESET}")
                    continue
                
                symbol = parts[0]
                date = parts[1]
                time = parts[2] if len(parts) > 2 and ':' in parts[2] else None
                
                # Check if timeframe was provided
                timeframe = None
                valid_timeframes = ['1s', '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
                if len(parts) > 2:
                    # Last part might be timeframe
                    last_part = parts[-1]
                    if last_part in valid_timeframes:
                        timeframe = last_part
                    # If we have 4 parts: symbol date time timeframe
                    elif len(parts) == 4 and parts[3] in valid_timeframes:
                        timeframe = parts[3]
                
                # If no timeframe provided, ask user to select
                if timeframe is None:
                    print(f"\n{CYAN}{'─' * 50}{RESET}")
                    print(f"{BOLD}{BRIGHT_PURPLE}SELECT TIMEFRAME{RESET}\n")
                    print(f"{CYAN}Available timeframes:{RESET}")
                    print(f"  {GREEN}[1]{RESET}  1s   - 1 second")
                    print(f"  {GREEN}[2]{RESET}  1m   - 1 minute")
                    print(f"  {GREEN}[3]{RESET}  3m   - 3 minutes")
                    print(f"  {GREEN}[4]{RESET}  5m   - 5 minutes")
                    print(f"  {GREEN}[5]{RESET}  15m  - 15 minutes")
                    print(f"  {GREEN}[6]{RESET}  30m  - 30 minutes")
                    print(f"  {GREEN}[7]{RESET}  1h   - 1 hour")
                    print(f"  {GREEN}[8]{RESET}  2h   - 2 hours")
                    print(f"  {GREEN}[9]{RESET}  4h   - 4 hours")
                    print(f"  {GREEN}[10]{RESET} 6h   - 6 hours")
                    print(f"  {GREEN}[11]{RESET} 8h   - 8 hours")
                    print(f"  {GREEN}[12]{RESET} 12h  - 12 hours")
                    print(f"  {GREEN}[13]{RESET} 1d   - 1 day")
                    print(f"  {GREEN}[14]{RESET} 3d   - 3 days")
                    print(f"  {GREEN}[15]{RESET} 1w   - 1 week")
                    print(f"  {GREEN}[16]{RESET} 1M   - 1 month\n")
                    
                    timeframe_map = {
                        '1': '1s',
                        '2': '1m',
                        '3': '3m',
                        '4': '5m',
                        '5': '15m',
                        '6': '30m',
                        '7': '1h',
                        '8': '2h',
                        '9': '4h',
                        '10': '6h',
                        '11': '8h',
                        '12': '12h',
                        '13': '1d',
                        '14': '3d',
                        '15': '1w',
                        '16': '1M'
                    }
                    
                    while True:
                        tf_choice = input(f"{CYAN}Select timeframe (1-16):{RESET} ").strip()
                        
                        if tf_choice in timeframe_map:
                            timeframe = timeframe_map[tf_choice]
                            break
                        else:
                            print(f"{RED}⚠ Invalid choice! Please enter a number between 1 and 16{RESET}")
                
                result = get_crypto_price(symbol.upper(), date, time, timeframe)
                print_crypto_result(result)
                
                # Ask if they want to check another
                print(f"\n{DIM}Press Enter to check another crypto, or type 'back' to change market{RESET}")
                continue_choice = input().strip().lower()
                if continue_choice == 'back':
                    break
def main():
    """Main entry point"""
    # If no arguments, start interactive mode
    if len(sys.argv) == 1:
        interactive_mode()
        return
    
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="StockScan - Market Price Lookup Tool",
        add_help=False
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Crypto command
    crypto_parser = subparsers.add_parser('crypto', help='Get crypto price')
    crypto_parser.add_argument('symbol', help='Trading pair (e.g., BTCUSDT)')
    crypto_parser.add_argument('date', help='Date (YYYY-MM-DD)')
    crypto_parser.add_argument('time', nargs='?', help='Time (HH:MM, optional)')
    crypto_parser.add_argument('--timeframe', '-t', 
                              choices=['1s', '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M'],
                              default='5m',
                              help='Candle timeframe (default: 5m)')
    
    # Stock command
    stock_parser = subparsers.add_parser('stock', help='Get stock price')
    stock_parser.add_argument('symbol', help='Stock symbol (e.g., AAPL)')
    stock_parser.add_argument('date', help='Date (YYYY-MM-DD)')
    stock_parser.add_argument('--timeframe', '-t',
                              choices=['1d', '1wk', '1mo'],
                              default='1d',
                              help='Candle timeframe (default: 1d)')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List symbols')
    list_parser.add_argument('market', choices=['crypto', 'stocks'], help='Market to list')
    
    # Help command
    subparsers.add_parser('help', help='Show help')
    
    try:
        args = parser.parse_args()
        
        if args.command == 'help' or not args.command:
            print_banner()
            print_description()
            print_usage()
        
        elif args.command == 'crypto':
            timeframe = getattr(args, 'timeframe', '5m')
            result = get_crypto_price(args.symbol, args.date, args.time, timeframe)
            print_crypto_result(result)
        
        elif args.command == 'stock':
            timeframe = getattr(args, 'timeframe', '1d')
            result = get_stock_price(args.symbol, args.date, None, timeframe)
            print_stock_result(result)
        
        elif args.command == 'list':
            if args.market == 'crypto':
                print(f"\n{CYAN}Available Crypto Symbols (first 50):{RESET}\n")
                symbols = list_crypto_symbols()
                for i, symbol in enumerate(symbols, 1):
                    print(f"  {i:2d}. {symbol}")
                print(f"\n{DIM}Total: {len(symbols)} symbols shown{RESET}\n")
            
            elif args.market == 'stocks':
                print(f"\n{CYAN}Available Stock Symbols (first 50):{RESET}\n")
                symbols = list_stock_symbols()
                for i, symbol in enumerate(symbols, 1):
                    print(f"  {i:2d}. {symbol}")
                print(f"\n{DIM}Total: {len(symbols)} symbols shown{RESET}\n")
    
    except SystemExit:
        # argparse calls sys.exit on error, catch it
        print(f"\n{YELLOW}Tip: Run 'python stockscan.py help' for usage instructions{RESET}\n")
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Cancelled by user{RESET}\n")
    except Exception as e:
        print(f"\n{RED}Unexpected error: {e}{RESET}\n")


if __name__ == "__main__":
    main()
