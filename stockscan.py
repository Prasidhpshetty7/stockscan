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

# Commodity ETF Symbols (130+ commodity ETFs)
COMMODITY_ETFS = {
    # Precious Metals - Gold
    "GLD": "SPDR Gold Shares",
    "IAU": "iShares Gold Trust",
    "GLDM": "SPDR Gold MiniShares",
    "SGOL": "abrdn Physical Gold Shares",
    "BAR": "GraniteShares Gold Trust",
    "AAAU": "Goldman Sachs Physical Gold",
    "OUNZ": "VanEck Merk Gold Trust",
    "GLDL": "Goldman Sachs ActiveBeta Gold",
    "IAUM": "iShares Gold Trust Micro",
    "AAAU": "Perth Mint Physical Gold",
    
    # Precious Metals - Silver
    "SLV": "iShares Silver Trust",
    "SIVR": "abrdn Physical Silver Shares",
    "PSLV": "Sprott Physical Silver Trust",
    "SLVP": "iShares MSCI Global Silver Miners",
    
    # Precious Metals - Platinum & Palladium
    "PPLT": "abrdn Physical Platinum Shares",
    "PALL": "abrdn Physical Palladium Shares",
    
    # Precious Metals - Multi-Metal
    "GLTR": "abrdn Physical Precious Metals Basket",
    "DBP": "Invesco DB Precious Metals Fund",
    
    # Energy - Crude Oil
    "USO": "United States Oil Fund",
    "UCO": "ProShares Ultra Bloomberg Crude Oil",
    "DBO": "Invesco DB Oil Fund",
    "USL": "United States 12 Month Oil Fund",
    "SCO": "ProShares UltraShort Bloomberg Crude Oil",
    "BNO": "United States Brent Oil Fund",
    "DNO": "United States Short Oil Fund",
    "OILK": "ProShares K-1 Free Crude Oil Strategy",
    "OLEM": "iShares Commodities Select Strategy",
    "USO": "United States Oil Fund LP",
    
    # Energy - Natural Gas
    "UNG": "United States Natural Gas Fund",
    "BOIL": "ProShares Ultra Bloomberg Natural Gas",
    "KOLD": "ProShares UltraShort Bloomberg Natural Gas",
    "UNL": "United States 12 Month Natural Gas Fund",
    "GAZ": "iPath Series B Bloomberg Natural Gas",
    "GASL": "Direxion Daily Natural Gas Related Bull 3X",
    "GASX": "Direxion Daily Natural Gas Related Bear 3X",
    
    # Energy - Gasoline & Heating Oil
    "UGA": "United States Gasoline Fund",
    "UHN": "United States Heating Oil Fund",
    
    # Energy - Broad Energy
    "DBE": "Invesco DB Energy Fund",
    "IXC": "iShares Global Energy ETF",
    "XLE": "Energy Select Sector SPDR Fund",
    "VDE": "Vanguard Energy ETF",
    "IYE": "iShares U.S. Energy ETF",
    
    # Agriculture - Grains
    "CORN": "Teucrium Corn Fund",
    "WEAT": "Teucrium Wheat Fund",
    "SOYB": "Teucrium Soybean Fund",
    "OATS": "Teucrium Oat Fund",
    "RICE": "Teucrium Rice Fund",
    "WEAT": "Teucrium Wheat Fund",
    "CANE": "Teucrium Sugar Fund",
    
    # Agriculture - Soft Commodities
    "JO": "iPath Series B Bloomberg Coffee",
    "NIB": "iPath Bloomberg Cocoa",
    "SGG": "iPath Series B Bloomberg Sugar",
    "BAL": "iPath Bloomberg Cotton",
    "WOOD": "iShares Global Timber & Forestry ETF",
    "CUT": "Invesco MSCI Global Timber ETF",
    
    # Agriculture - Livestock
    "COW": "iPath Series B Bloomberg Livestock",
    
    # Agriculture - Broad Agriculture
    "DBA": "Invesco DB Agriculture Fund",
    "TAGS": "Teucrium Agricultural Fund",
    "RJA": "Elements Rogers International Commodity Agriculture",
    "MOO": "VanEck Agribusiness ETF",
    "VEGI": "iShares MSCI Global Agriculture Producers",
    "PAGG": "Invesco Global Agriculture ETF",
    "FTAG": "First Trust Indxx Global Agriculture ETF",
    
    # Industrial Metals - Copper
    "CPER": "United States Copper Index Fund",
    "JJC": "iPath Series B Bloomberg Copper",
    "COPX": "Global X Copper Miners ETF",
    
    # Industrial Metals - Aluminum
    "JJU": "iPath Series B Bloomberg Aluminum",
    
    # Industrial Metals - Nickel
    "JJN": "iPath Series B Bloomberg Nickel",
    
    # Industrial Metals - Broad Base Metals
    "DBB": "Invesco DB Base Metals Fund",
    "PICK": "iShares MSCI Global Metals & Mining Producers",
    "XME": "SPDR S&P Metals & Mining ETF",
    
    # Broad Commodity Baskets
    "DBC": "Invesco DB Commodity Index Tracking Fund",
    "PDBC": "Invesco Optimum Yield Diversified Commodity",
    "GSG": "iShares S&P GSCI Commodity-Indexed Trust",
    "USCI": "United States Commodity Index Fund",
    "GCC": "WisdomTree Continuous Commodity Index Fund",
    "RJI": "Elements Rogers International Commodity Index",
    "COMT": "iShares Commodities Select Strategy ETF",
    "CMDY": "iShares Bloomberg Roll Select Commodity Strategy",
    "BCI": "abrdn Bloomberg All Commodity Strategy K-1 Free",
    "FTGC": "First Trust Global Tactical Commodity Strategy",
    "COMB": "GraniteShares Bloomberg Commodity Broad Strategy",
    
    # Uranium & Nuclear
    "URA": "Global X Uranium ETF",
    "URNM": "Sprott Uranium Miners ETF",
    "NLR": "VanEck Uranium+Nuclear Energy ETF",
    "HURA": "Horizons Global Uranium Index ETF",
    
    # Carbon Credits
    "KRBN": "KraneShares Global Carbon Strategy ETF",
    "KEUA": "KraneShares European Carbon Allowance Strategy",
    
    # Leveraged & Inverse Commodity ETFs
    "UGL": "ProShares Ultra Gold",
    "GLL": "ProShares UltraShort Gold",
    "AGQ": "ProShares Ultra Silver",
    "ZSL": "ProShares UltraShort Silver",
    "UGLD": "VelocityShares 3x Long Gold ETN",
    "DGLD": "VelocityShares 3x Inverse Gold ETN",
    "USLV": "VelocityShares 3x Long Silver ETN",
    "DSLV": "VelocityShares 3x Inverse Silver ETN",
    "BOIL": "ProShares Ultra Bloomberg Natural Gas",
    "KOLD": "ProShares UltraShort Bloomberg Natural Gas",
    "UCO": "ProShares Ultra Bloomberg Crude Oil",
    "SCO": "ProShares UltraShort Bloomberg Crude Oil",
    "WTIU": "ProShares Ultra Bloomberg WTI Crude Oil",
    "WTID": "ProShares UltraShort Bloomberg WTI Crude Oil",
    
    # Specialty Commodities
    "PLTM": "GraniteShares Platinum Trust",
    "PALL": "abrdn Physical Palladium Shares ETF",
    "WITE": "ETRACS Bloomberg Commodity Index Total Return ETN",
    "DJCI": "ETRACS Bloomberg Commodity Index Total Return ETN",
}


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
  StockScan lets you look up the exact price of any crypto, stock, or commodity
  at a specific date and time using OHLCV candle logic.

{CYAN}How it works:{RESET}
  • Fetches OHLCV (Open, High, Low, Close, Volume) candle data
  • Finds the candle that CONTAINS your requested time
  • Returns the CLOSE price as the price at that time
  • Compare with current price to see profit/loss
  • This is the standard method used by professional trading tools

{CYAN}Data Sources:{RESET}
  • Crypto: Binance (1000+ coins, NO API KEY NEEDED)
    - Supports: 1s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
  • Stocks: Yahoo Finance (all US & Indian stocks, NO API KEY NEEDED)
    - Supports: 1d (daily), 1wk (weekly), 1mo (monthly)
  • Commodities: Yahoo Finance (130+ commodity ETFs, NO API KEY NEEDED)
    - Supports: 1d (daily), 1wk (weekly), 1mo (monthly)
    - Gold, Silver, Oil, Natural Gas, Agriculture, Metals & more!
    - Works out of the box!

{CYAN}Coverage:{RESET}
  • All NASDAQ, NYSE, AMEX stocks (5000+ US stocks)
  • All NSE stocks (1000+ Indian stocks)
  • All BSE stocks (1000+ Indian stocks)
  • 1000+ crypto pairs on Binance
  • 130+ commodity ETFs
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
  python stockscan.py stock AAPL 2026-01-15 --timeframe 1d
  python stockscan.py stock TSLA 2025-06-10 --timeframe 1wk
  python stockscan.py stock TCS.NS 2024-12-20 --timeframe 1mo
  python stockscan.py stock INFY.NS 2023-08-05 --timeframe 1d
  python stockscan.py stock HDFCBANK.BO 2024-03-18 --timeframe 1wk

  {GREEN}# Get commodity price with timeframe{RESET}
  python stockscan.py commodity GLD 2024-01-15 --timeframe 1d
  python stockscan.py commodity USO 2024-01-10 --timeframe 1wk
  python stockscan.py commodity CORN 2024-01-15 --timeframe 1mo

  {GREEN}# List all available symbols{RESET}
  python stockscan.py list crypto
  python stockscan.py list stocks
  python stockscan.py list commodities

  {GREEN}# Show help{RESET}
  python stockscan.py help

{CYAN}Supported Timeframes:{RESET}
  {BOLD}Crypto:{RESET} 1s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
  {BOLD}Stocks:{RESET} 1d (daily), 1wk (weekly), 1mo (monthly)
  {BOLD}Commodities:{RESET} 1d (daily), 1wk (weekly), 1mo (monthly)

{CYAN}Interactive Mode Features:{RESET}
  • After viewing historical price, you get 3 options:
    {GREEN}[1]{RESET} Check Live Price - View current market price
    {GREEN}[2]{RESET} Compare with Current - See P&L and percentage change
    {GREEN}[3]{RESET} Continue - Check another asset

{CYAN}How it works:{RESET}
  • Uses OHLCV candle logic (industry-standard method)
  • Finds the candle that CONTAINS your requested time
  • Returns the CLOSE price of that candle
  • Compare with current price to see profit/loss
  • This is the standard method for historical price lookups

{GREEN}✅ NO API KEYS NEEDED!{RESET}
  Crypto (Binance), Stocks (Yahoo Finance), and Commodities (Yahoo Finance)
  all work out of the box. Just download and run!

{YELLOW}⚠ Coverage Note:{RESET}
  StockScan covers all major large-cap and mid-cap stocks.
  Very small-cap stocks and very newly listed IPOs are not supported.

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
            return {"error": "Future price data does not exist.\nThe requested date is in the future. Please choose a date in the past."}
        
        # For weekly/monthly timeframes, check if the period has completed
        if timeframe in ["1w", "1M"]:
            if timeframe == "1w":
                end_dt = dt + timedelta(days=7)
                period_name = "week"
            else:  # 1M
                end_dt = dt + timedelta(days=30)
                period_name = "month"
            
            if end_dt > datetime.now():
                return {"error": f"The {period_name} period starting from {date_str} has not completed yet.\nEnd date would be {end_dt.strftime('%Y-%m-%d')}, which is in the future.\nPlease choose an earlier date or use a shorter timeframe."}
        
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
        
        # For intraday timeframes (under 1d), fetch 1-minute candles and aggregate
        # This allows starting from ANY arbitrary time
        intraday_timeframes = ['1s', '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h']
        
        if interval in intraday_timeframes:
            # Fetch 1-minute candles to aggregate into custom period
            start_time = target_timestamp_ms
            end_time = target_timestamp_ms + window
            
            url = f"{BINANCE_BASE}/klines"
            params = {
                "symbol": symbol,
                "interval": "1m",  # Fetch 1-minute candles
                "startTime": start_time,
                "endTime": end_time,
                "limit": 1500  # Max limit
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                return {"error": "No data available for this time.\nThe crypto asset may not have existed yet, or data is unavailable."}
            
            # Aggregate the 1-minute candles into one
            opens = [float(candle[1]) for candle in data]
            highs = [float(candle[2]) for candle in data]
            lows = [float(candle[3]) for candle in data]
            closes = [float(candle[4]) for candle in data]
            volumes = [float(candle[5]) for candle in data]
            
            # Create aggregated candle
            target_candle = [
                data[0][0],  # Open time (first candle)
                opens[0],  # First open
                max(highs),  # Highest high
                min(lows),  # Lowest low
                closes[-1],  # Last close
                sum(volumes),  # Total volume
                data[-1][6]  # Close time (last candle)
            ]
            
            candle_open_time = dt
            candle_close_time = datetime.fromtimestamp(end_time / 1000)
            
        elif interval in ["1w", "1M"]:
            # For weekly/monthly timeframes, start from exact date and go forward
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
                return {"error": "No data available for this time.\nThe crypto asset may not have existed yet, or data is unavailable."}
            
            target_candle = data[0]
            
            # Calculate actual period
            candle_open_time = dt  # Start from requested date
            candle_close_time = dt + timedelta(milliseconds=window)
        else:
            # For daily and above (3d), use standard Binance candles
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
                return {"error": "No data available for this time.\nThe crypto asset may not have existed yet, or data is unavailable."}
            
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
        
        # Check if candle crosses midnight (spans two different dates)
        crosses_midnight = candle_open_time.date() != candle_close_time.date()
        midnight_note = None
        
        if crosses_midnight:
            # Calculate time in each day
            start_date = candle_open_time.date()
            end_date = candle_close_time.date()
            
            # Time until midnight from start
            midnight_of_start = datetime.combine(start_date, datetime.max.time()).replace(microsecond=0) + timedelta(seconds=1)
            time_in_first_day = (midnight_of_start - candle_open_time).total_seconds()
            
            # Time from midnight in next day
            time_in_second_day = (candle_close_time - midnight_of_start).total_seconds()
            
            # Convert to readable format with hours and minutes
            def seconds_to_readable(seconds):
                if seconds < 60:
                    return f"{int(seconds)} second(s)"
                elif seconds < 3600:
                    minutes = int(seconds / 60)
                    return f"{minutes} minute(s)"
                else:
                    hours = int(seconds / 3600)
                    remaining_seconds = seconds % 3600
                    minutes = int(remaining_seconds / 60)
                    
                    if minutes > 0:
                        return f"{hours} hour(s) {minutes} minute(s)"
                    else:
                        return f"{hours} hour(s)"
            
            midnight_note = f"{seconds_to_readable(time_in_first_day)} from {start_date.strftime('%Y-%m-%d')}, {seconds_to_readable(time_in_second_day)} from {end_date.strftime('%Y-%m-%d')}"
        
        result = {
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
            "volume": float(target_candle[5]),
            "crosses_midnight": crosses_midnight,
            "midnight_note": midnight_note
        }
        
        return result
    
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
    
    # Pass through specific error messages
    error_msg = result["error"]
    if any(phrase in error_msg for phrase in [
        "has not completed yet",
        "may not have existed",
        "No data found",
        "No trading data",
        "Incomplete data",
        "No price data",
        "Future price data"
    ]):
        return result
    
    # If Yahoo Finance failed for other reasons, return the original error with context
    return {
        "error": result["error"] + "\n\nPlease check the symbol and date, or try a different timeframe."
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
            return {"error": "Future price data does not exist.\nThe requested date is in the future. Please choose a date in the past."}
        
        # For weekly/monthly timeframes, check if the period has completed
        if timeframe in ["1wk", "1mo"]:
            if timeframe == "1wk":
                end_dt = dt + timedelta(days=7)
                period_name = "week"
            else:  # 1mo
                end_dt = dt + timedelta(days=30)
                period_name = "month"
            
            if end_dt > datetime.now():
                return {"error": f"The {period_name} period starting from {date_str} has not completed yet.\nEnd date would be {end_dt.strftime('%Y-%m-%d')}, which is in the future.\nPlease choose an earlier date or use a shorter timeframe."}
        
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
            # Add buffer days before to handle holidays/weekends at start
            start_dt = dt - timedelta(days=5)  # Go back 5 days to catch the requested date
            
            # Calculate end date based on timeframe
            # Add extra days to account for weekends and holidays
            if timeframe == "1wk":
                end_dt = dt + timedelta(days=14)  # Fetch 2 weeks to ensure we get 7 calendar days of data
            else:  # 1mo
                end_dt = dt + timedelta(days=40)  # Fetch 40 days to ensure we get 30 calendar days of data
            
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
            return {"error": f"No data found for symbol {symbol}.\nThe stock/commodity may not have existed at that time, or data is unavailable.\n\nNote: StockScan doesn't cover very small-cap stocks and very newly listed IPOs.\nPlease verify the symbol is correct and the company has sufficient trading history."}
        
        quote = result[0]
        
        if "timestamp" not in quote or "indicators" not in quote:
            return {"error": "Invalid data format from Yahoo Finance.\nThe stock/commodity may not have existed at that time, or data is unavailable.\n\nNote: StockScan doesn't cover very small-cap stocks and very newly listed IPOs.\nPlease verify the symbol is correct and the company has sufficient trading history."}
        
        timestamps = quote["timestamp"]
        indicators = quote["indicators"]["quote"][0]
        
        if not timestamps or not indicators:
            return {"error": "No price data available.\nThe stock/commodity may not have existed at that time, or data is unavailable.\n\nNote: StockScan doesn't cover very small-cap stocks and very newly listed IPOs.\nPlease verify the symbol is correct and the company has sufficient trading history."}
        
        # Find the data for our target period
        if timeframe in ["1wk", "1mo"]:
            # For weekly/monthly, aggregate daily data into one candle
            if not timestamps or len(timestamps) == 0:
                return {"error": "No price data available for this period"}
            
            # Calculate the end date for the period (inclusive)
            if timeframe == "1wk":
                period_end_date = (dt + timedelta(days=6)).date()  # 7 days total (day 0 to day 6)
            else:  # 1mo
                period_end_date = (dt + timedelta(days=29)).date()  # 30 days total (day 0 to day 29)
            
            # Filter timestamps to only include dates within the requested period
            filtered_indices = []
            
            for i, ts in enumerate(timestamps):
                ts_date = datetime.fromtimestamp(ts).date()
                # Include if date is >= requested date AND <= period end date (inclusive)
                if dt.date() <= ts_date <= period_end_date:
                    filtered_indices.append(i)
            
            if not filtered_indices:
                return {"error": "No trading data available for the requested period.\nThe stock/commodity may not have existed at that time, or data is unavailable."}
            
            # Aggregate only the filtered daily candles
            opens = [indicators["open"][i] for i in filtered_indices if indicators["open"][i] is not None]
            highs = [indicators["high"][i] for i in filtered_indices if indicators["high"][i] is not None]
            lows = [indicators["low"][i] for i in filtered_indices if indicators["low"][i] is not None]
            closes = [indicators["close"][i] for i in filtered_indices if indicators["close"][i] is not None]
            volumes = [indicators["volume"][i] for i in filtered_indices if indicators["volume"][i] is not None]
            
            if not opens or not closes:
                return {"error": "Incomplete data for this period.\nThe stock/commodity may not have existed at that time, or data is unavailable."}
            
            # Create aggregated candle
            open_price = opens[0]  # First open
            high_price = max(highs)  # Highest high
            low_price = min(lows)  # Lowest low
            close_price = closes[-1]  # Last close
            volume = sum(volumes)  # Total volume
            
            # Show the FULL requested period (not just trading days)
            # This shows the complete 7-day or 30-day period
            candle_start_date = dt.strftime("%Y-%m-%d")
            if timeframe == "1wk":
                candle_end_date = (dt + timedelta(days=6)).strftime("%Y-%m-%d")
                expected_period_days = 7
            else:  # 1mo
                candle_end_date = (dt + timedelta(days=29)).strftime("%Y-%m-%d")
                expected_period_days = 30
            
            # Calculate missing days (holidays/weekends)
            trading_days = len(filtered_indices)
            missing_days = expected_period_days - trading_days
            
            # Store missing days info for display
            if missing_days > 0:
                result_missing_days = missing_days
            else:
                result_missing_days = None
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
            result_missing_days = None  # Not used for daily
            
            open_price = indicators["open"][closest_idx]
            high_price = indicators["high"][closest_idx]
            low_price = indicators["low"][closest_idx]
            close_price = indicators["close"][closest_idx]
            volume = indicators["volume"][closest_idx]
        
        # Check for None values
        if None in [open_price, high_price, low_price, close_price, volume]:
            return {"error": f"Incomplete data for {date_str}.\nMarket may have been closed, or the stock/commodity may not have existed at that time."}
        
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
            "volume": float(volume),
            "missing_days": result_missing_days
        }
        
        # Add note if date was adjusted (only for daily)
        if timeframe == "1d" and candle_start_date != date_str:
            result["note"] = f"Market was closed on {date_str}. Showing closest trading day."
        
        return result
    
    except requests.exceptions.RequestException as e:
        error_str = str(e)
        if "400" in error_str or "Bad Request" in error_str:
            return {"error": f"No data available for {symbol} on {date_str}.\nThe stock/commodity may not have existed at that time, or data is unavailable for this date range.\n\nNote: StockScan doesn't cover very small-cap stocks and very newly listed IPOs.\nPlease verify the symbol is correct and the company has sufficient trading history."}
        return {"error": f"Failed to fetch from Yahoo Finance: {str(e)}"}
    except (KeyError, IndexError, TypeError) as e:
        return {"error": f"Error parsing Yahoo Finance data.\nThe stock/commodity may not have existed at that time, or data format is unexpected.\n\nNote: StockScan doesn't cover very small-cap stocks and very newly listed IPOs.\nPlease verify the symbol is correct and the company has sufficient trading history."}
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
            return {"error": "Future price data does not exist.\nThe requested date is in the future. Please choose a date in the past."}
        
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
            return {"error": "Future price data does not exist.\nThe requested date is in the future. Please choose a date in the past."}
        
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


def get_live_crypto_price(symbol: str) -> Dict[str, Any]:
    """Get current live price for crypto from Binance"""
    try:
        url = f"{BINANCE_BASE}/ticker/price"
        params = {"symbol": symbol}
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        return {
            "symbol": symbol,
            "price": float(data['price']),
            "timestamp": datetime.now(),
            "source": "Binance",
            "delay_note": "The current price may have a 1-2 minute delay"
        }
    except Exception as e:
        return {"error": f"Failed to fetch live price: {str(e)}"}


def get_live_stock_price(symbol: str) -> Dict[str, Any]:
    """Get current live price for stock from Yahoo Finance"""
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        params = {"interval": "1m", "range": "1d"}
        headers = {"User-Agent": "Mozilla/5.0"}
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if "chart" not in data or "result" not in data["chart"]:
            return {"error": "Invalid response from Yahoo Finance"}
        
        result = data["chart"]["result"]
        if not result or len(result) == 0:
            return {"error": f"No data found for symbol {symbol}"}
        
        quote = result[0]
        meta = quote.get("meta", {})
        
        current_price = meta.get("regularMarketPrice") or meta.get("previousClose")
        
        if current_price is None:
            return {"error": "Could not retrieve current price"}
        
        return {
            "symbol": symbol,
            "price": float(current_price),
            "timestamp": datetime.now(),
            "source": "Yahoo Finance",
            "delay_note": "The current price may have a ~15 minute delay"
        }
    except Exception as e:
        return {"error": f"Failed to fetch live price: {str(e)}"}


def print_live_price(live_data: Dict[str, Any], market_type: str):
    """Print live price in a formatted way"""
    if "error" in live_data:
        print(f"\n{RED}✗ Error: {live_data['error']}{RESET}\n")
        return
    
    # Format price based on market type
    if market_type == 'CRYPTO':
        formatted_price = f"${live_data['price']:,.8f}"
    else:
        formatted_price = f"${live_data['price']:,.2f}"
    
    output = f"""
{PURPLE}{'─' * 70}{RESET}
{BOLD}{BRIGHT_PURPLE}LIVE {market_type.upper()} PRICE{RESET}
{PURPLE}{'─' * 70}{RESET}

{CYAN}ASSET:{RESET}           {live_data['symbol']}
{CYAN}SOURCE:{RESET}          {live_data['source']}
{CYAN}TIMESTAMP:{RESET}       {live_data['timestamp'].strftime("%Y-%m-%d %H:%M:%S")}

{GREEN}{BOLD}CURRENT PRICE:  {formatted_price}{RESET}

{YELLOW}⚠ Note: {live_data['delay_note']}{RESET}

{PURPLE}{'─' * 70}{RESET}
"""
    print(output)


def print_price_comparison(checked_result: Dict[str, Any], live_data: Dict[str, Any], market_type: str):
    """Print comparison between checked price and current price"""
    if "error" in live_data:
        print(f"\n{RED}✗ Error fetching current price: {live_data['error']}{RESET}\n")
        return
    
    # Extract prices
    checked_price = checked_result['close']
    current_price = live_data['price']
    
    # Calculate P&L
    pnl = current_price - checked_price
    pnl_percent = (pnl / checked_price) * 100 if checked_price != 0 else 0
    
    # Determine profit/loss
    if pnl > 0:
        pnl_color = GREEN
        movement = "PROFIT ↑"
        pnl_sign = "+"
    elif pnl < 0:
        pnl_color = RED
        movement = "LOSS ↓"
        pnl_sign = ""
    else:
        pnl_color = YELLOW
        movement = "NO CHANGE →"
        pnl_sign = ""
    
    # Calculate time difference
    if market_type == "CRYPTO":
        checked_time = datetime.strptime(checked_result['requested_time'], "%Y-%m-%d %H:%M UTC")
    else:
        checked_time = datetime.strptime(checked_result['requested_date'], "%Y-%m-%d")
    
    current_time = live_data['timestamp']
    time_diff = current_time - checked_time
    
    # Format time difference
    days = time_diff.days
    hours = time_diff.seconds // 3600
    minutes = (time_diff.seconds % 3600) // 60
    
    if days > 0:
        time_period = f"{days} day(s), {hours} hour(s), {minutes} minute(s)"
    elif hours > 0:
        time_period = f"{hours} hour(s), {minutes} minute(s)"
    else:
        time_period = f"{minutes} minute(s)"
    
    # Format prices
    if market_type == "CRYPTO":
        price_format = ",.8f"
        currency = "$"
    else:
        price_format = ",.2f"
        # Detect currency
        symbol = checked_result['symbol']
        if '.NS' in symbol or '.BO' in symbol:
            currency = '₹'
        else:
            currency = '$'
    
    output = f"""
{PURPLE}{'─' * 70}{RESET}
{BOLD}{BRIGHT_PURPLE}PRICE COMPARISON - {market_type}{RESET}
{PURPLE}{'─' * 70}{RESET}

{CYAN}CHECKED PRICE:{RESET}
  Date/Time:  {checked_result.get('requested_time') or checked_result.get('requested_date')}
  Price:      {currency}{checked_price:{price_format}}

{CYAN}CURRENT PRICE:{RESET}
  Date/Time:  {current_time.strftime("%Y-%m-%d %H:%M:%S")}
  Price:      {currency}{current_price:{price_format}}

{CYAN}ANALYSIS:{RESET}
  {pnl_color}{BOLD}P&L:        {pnl_sign}{currency}{abs(pnl):{price_format}}{RESET}
  {pnl_color}{BOLD}Change:     {pnl_sign}{pnl_percent:.2f}%{RESET}
  {pnl_color}{BOLD}Movement:   {movement}{RESET}
  
{CYAN}TIME PERIOD:{RESET}  {time_period}

{YELLOW}⚠ Note: {live_data['delay_note']}{RESET}

{PURPLE}{'─' * 70}{RESET}
"""
    print(output)


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
    
    # Midnight crossing note
    midnight_crossing_note = ""
    if result.get('crosses_midnight') and result.get('midnight_note'):
        midnight_crossing_note = f"\n{YELLOW}ℹ Note: Timeframe spans across two dates.{RESET}\n{DIM}   Period includes: {result['midnight_note']}{RESET}\n"
    
    output = f"""
{PURPLE}{'─' * 70}{RESET}
{BOLD}{BRIGHT_PURPLE}STOCKSCAN - CRYPTO PRICE LOOKUP{RESET}
{PURPLE}{'─' * 70}{RESET}

{CYAN}ASSET:{RESET}           {result['symbol']}
{CYAN}MARKET:{RESET}          {result['market']}
{CYAN}REQUESTED TIME:{RESET}  {result['requested_time']}
{CYAN}TIMEFRAME:{RESET}       {result['timeframe']}

{DIM}Candle Period:  {result['candle_start']} → {result['candle_end']}{RESET}
{midnight_crossing_note}
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
    
    # Detect if this is a commodity
    is_commodity = 'commodity_name' in result
    
    # Detect currency based on symbol
    symbol = result['symbol']
    if '.NS' in symbol or '.BO' in symbol:
        # Indian stocks (NSE or BSE)
        currency = '₹'
        market_name = 'Indian Stock Market'
        market_type = 'stock market'
    else:
        # US and other stocks/commodities
        currency = '$'
        if is_commodity:
            market_name = f"Commodities (Yahoo Finance)"
            market_type = 'commodity market'
        else:
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
        
        # Add holiday/weekend notification if there are missing days
        if result.get('missing_days') and result['missing_days'] > 0:
            missing_days = result['missing_days']
            timeframe_name = result['timeframe'].lower()  # "weekly" or "monthly"
            trading_days = 7 - missing_days if result['timeframe'] == 'Weekly' else 30 - missing_days
            
            candle_date_display += f"\n{YELLOW}ℹ Note: This period has only {trading_days} trading day(s) out of the full {timeframe_name} timeframe.{RESET}\n{DIM}   {missing_days} day(s) excluded due to weekends/holidays. Check dates beyond this period for continued data.{RESET}"
    else:
        # Daily - show single date
        candle_date_display = f"{DIM}Candle Date:    {result['candle_start_date']}{RESET}"
    
    # Determine header title
    if is_commodity:
        header_title = "STOCKSCAN - COMMODITY PRICE LOOKUP"
        # Add commodity name if available
        if 'commodity_name' in result:
            commodity_info = f"{CYAN}COMMODITY:{RESET}      {result['commodity_name']}\n"
        else:
            commodity_info = ""
    else:
        header_title = "STOCKSCAN - STOCK PRICE LOOKUP"
        commodity_info = ""
    
    output = f"""
{PURPLE}{'─' * 70}{RESET}
{BOLD}{BRIGHT_PURPLE}{header_title}{RESET}
{PURPLE}{'─' * 70}{RESET}

{CYAN}ASSET:{RESET}           {result['symbol']}
{commodity_info}{CYAN}MARKET:{RESET}          {market_name}
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


def show_more_options_menu(result: Dict[str, Any], symbol: str, market_type: str) -> str:
    """Show more options menu after displaying price data
    
    Args:
        result: The price result dictionary
        symbol: The asset symbol
        market_type: 'CRYPTO', 'STOCK', or 'COMMODITY'
    
    Returns:
        User's choice ('1', '2', '3')
    """
    print(f"\n{CYAN}{'─' * 70}{RESET}")
    print(f"{BOLD}{BRIGHT_PURPLE}What would you like to do next?{RESET}\n")
    print(f"  {GREEN}[1]{RESET}  Check Live Price       - View current market price")
    print(f"  {GREEN}[2]{RESET}  Compare with Current   - See price movement & P&L")
    print(f"  {GREEN}[3]{RESET}  Continue               - Check another asset\n")
    
    while True:
        choice = input(f"{CYAN}Select option (1-3):{RESET} ").strip()
        
        if choice in ['1', '2', '3']:
            return choice
        else:
            print(f"{RED}⚠ Invalid choice! Please enter 1, 2, or 3{RESET}")


def interactive_mode():
    """Interactive mode - guides user through price lookup"""
    print_banner()
    print_description()
    
    while True:
        # Ask which market
        print(f"\n{CYAN}{'─' * 70}{RESET}")
        print(f"{BOLD}{BRIGHT_PURPLE}Which market do you want to check?{RESET}\n")
        print(f"  {GREEN}[1]{RESET} Stocks       (AAPL, TSLA, INFY.NS, HDFCBANK.BO, etc.)")
        print(f"  {GREEN}[2]{RESET} Crypto       (BTCUSDT, ETHUSDT, etc.)")
        print(f"  {GREEN}[3]{RESET} Commodities  (GLD, USO, CORN, etc.)")
        print(f"  {YELLOW}[Q]{RESET} Quit\n")
        
        choice = input(f"{CYAN}Enter your choice (1/2/3/Q):{RESET} ").strip().upper()
        
        if choice == 'Q':
            print(f"\n{PURPLE}Thanks for using StockScan! Goodbye! 👋{RESET}\n")
            break
        
        if choice not in ['1', '2', '3']:
            print(f"\n{RED}⚠ Invalid choice! Please enter 1 for Stocks, 2 for Crypto, 3 for Commodities, or Q to quit.{RESET}")
            continue
        
        # Show syntax based on choice
        if choice == '1':
            # Stock mode
            print(f"\n{CYAN}{'─' * 70}{RESET}")
            print(f"{BOLD}{BRIGHT_PURPLE}STOCK PRICE LOOKUP{RESET}\n")
            print(f"{CYAN}Syntax:{RESET} {GREEN}<SYMBOL> <DATE>{RESET}")
            print(f"{CYAN}Examples:{RESET}")
            print(f"  AAPL 2026-01-15")
            print(f"  TSLA 2025-06-10")
            print(f"  TCS.NS 2024-12-20")
            print(f"  INFY.NS 2023-08-05")
            print(f"  HDFCBANK.BO 2024-03-18\n")
            print(f"{DIM}Date format: YYYY-MM-DD{RESET}")
            print(f"{DIM}Will ask for timeframe after you enter{RESET}")
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
                
                # Show more options menu if result is valid
                if "error" not in result:
                    choice = show_more_options_menu(result, symbol.upper(), "STOCK")
                    
                    if choice == '1':
                        # Check live price
                        live_data = get_live_stock_price(symbol.upper())
                        print_live_price(live_data, "STOCK")
                    elif choice == '2':
                        # Compare with current price
                        live_data = get_live_stock_price(symbol.upper())
                        print_price_comparison(result, live_data, "STOCK")
                
                # Ask if they want to check another
                print(f"\n{DIM}Press Enter to check another stock, or type 'back' to change market{RESET}")
                continue_choice = input().strip().lower()
                if continue_choice == 'back':
                    break
        
        elif choice == '2':
            # Crypto mode
            print(f"\n{CYAN}{'─' * 70}{RESET}")
            print(f"{BOLD}{BRIGHT_PURPLE}CRYPTO PRICE LOOKUP{RESET}\n")
            print(f"{CYAN}Syntax:{RESET} {GREEN}<SYMBOL> <DATE>{RESET}")
            print(f"{CYAN}Examples:{RESET}")
            print(f"  BTCUSDT 2026-01-15")
            print(f"  ETHUSDT 2026-01-15")
            print(f"  BNBUSDT 2026-01-10\n")
            print(f"{DIM}Date format: YYYY-MM-DD{RESET}")
            print(f"{DIM}Will ask for timeframe after you enter{RESET}")
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
                    print(f"{RED}⚠ Invalid syntax! Use: <SYMBOL> <DATE>{RESET}")
                    print(f"{YELLOW}Example: BTCUSDT 2026-01-15{RESET}")
                    continue
                
                symbol = parts[0]
                date = parts[1]
                time = None  # Will be asked later if needed
                
                # Check if timeframe was provided (optional - for advanced users)
                timeframe = None
                valid_timeframes = ['1s', '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
                
                # Check if user provided time and/or timeframe (advanced usage)
                if len(parts) > 2:
                    # Could be: BTCUSDT 2026-01-15 14:30 or BTCUSDT 2026-01-15 1h
                    if ':' in parts[2]:
                        time = parts[2]
                        # Check if timeframe is also provided
                        if len(parts) > 3 and parts[3] in valid_timeframes:
                            timeframe = parts[3]
                    elif parts[2] in valid_timeframes:
                        timeframe = parts[2]
                
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
                
                # For timeframes under 1d, ask for start time if not provided
                intraday_timeframes = ['1s', '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h']
                if timeframe in intraday_timeframes and not time:
                    print(f"\n{CYAN}{'─' * 50}{RESET}")
                    print(f"{BOLD}{BRIGHT_PURPLE}ENTER START TIME{RESET}\n")
                    print(f"{CYAN}What time should the {timeframe} timeframe start?{RESET}\n")
                    print(f"{DIM}Format: HH:MM (24-hour format){RESET}")
                    print(f"{DIM}Range:  00:00 to 23:59{RESET}")
                    print(f"{DIM}Example: 14:30, 09:15, 23:59{RESET}\n")
                    
                    while True:
                        time_input = input(f"{CYAN}Enter start time (HH:MM):{RESET} ").strip()
                        
                        # Validate time format
                        if not time_input:
                            print(f"{RED}⚠ Please enter a time!{RESET}")
                            continue
                        
                        if ':' not in time_input:
                            print(f"{RED}⚠ Invalid format! Use HH:MM (e.g., 14:30){RESET}")
                            continue
                        
                        try:
                            time_parts = time_input.split(':')
                            if len(time_parts) != 2:
                                print(f"{RED}⚠ Invalid format! Use HH:MM (e.g., 14:30){RESET}")
                                continue
                            
                            hours = int(time_parts[0])
                            minutes = int(time_parts[1])
                            
                            if hours < 0 or hours > 23:
                                print(f"{RED}⚠ Hours must be between 00 and 23!{RESET}")
                                continue
                            
                            if minutes < 0 or minutes > 59:
                                print(f"{RED}⚠ Minutes must be between 00 and 59!{RESET}")
                                continue
                            
                            # Format time properly (ensure 2 digits)
                            time = f"{hours:02d}:{minutes:02d}"
                            break
                        
                        except ValueError:
                            print(f"{RED}⚠ Invalid time! Use numbers only (e.g., 14:30){RESET}")
                            continue
                
                result = get_crypto_price(symbol.upper(), date, time, timeframe)
                print_crypto_result(result)
                
                # Show more options menu if result is valid
                if "error" not in result:
                    choice = show_more_options_menu(result, symbol.upper(), "CRYPTO")
                    
                    if choice == '1':
                        # Check live price
                        live_data = get_live_crypto_price(symbol.upper())
                        print_live_price(live_data, "CRYPTO")
                    elif choice == '2':
                        # Compare with current price
                        live_data = get_live_crypto_price(symbol.upper())
                        print_price_comparison(result, live_data, "CRYPTO")
                
                # Ask if they want to check another
                print(f"\n{DIM}Press Enter to check another crypto, or type 'back' to change market{RESET}")
                continue_choice = input().strip().lower()
                if continue_choice == 'back':
                    break
        
        elif choice == '3':
            # Commodity mode
            print(f"\n{CYAN}{'─' * 70}{RESET}")
            print(f"{BOLD}{BRIGHT_PURPLE}COMMODITY PRICE LOOKUP{RESET}\n")
            print(f"{CYAN}Syntax:{RESET} {GREEN}<SYMBOL> <DATE>{RESET}")
            print(f"{CYAN}Examples:{RESET}")
            print(f"  GLD 2026-01-15")
            print(f"  USO 2026-01-15")
            print(f"  CORN 2024-12-20\n")
            print(f"{DIM}Date format: YYYY-MM-DD{RESET}")
            print(f"{DIM}Will ask for timeframe after you enter{RESET}")
            print(f"{DIM}Type 'list' to see all available commodities{RESET}")
            print(f"{DIM}Type 'back' to return to market selection{RESET}\n")
            
            while True:
                user_input = input(f"{CYAN}Enter commodity lookup:{RESET} ").strip()
                
                if user_input.lower() == 'back':
                    break
                
                if user_input.lower() == 'list':
                    # Show list of available commodities
                    print(f"\n{CYAN}{'─' * 70}{RESET}")
                    print(f"{BOLD}{BRIGHT_PURPLE}AVAILABLE COMMODITY ETFs ({len(COMMODITY_ETFS)} total){RESET}\n")
                    
                    # Group by category
                    categories = {
                        "Precious Metals - Gold": ["GLD", "IAU", "GLDM", "SGOL", "BAR", "AAAU", "OUNZ", "GLDL", "IAUM"],
                        "Precious Metals - Silver": ["SLV", "SIVR", "PSLV", "SLVP"],
                        "Precious Metals - Platinum & Palladium": ["PPLT", "PALL", "PLTM"],
                        "Energy - Crude Oil": ["USO", "UCO", "DBO", "USL", "BNO", "OILK", "OLEM"],
                        "Energy - Natural Gas": ["UNG", "BOIL", "KOLD", "UNL", "GAZ", "GASL", "GASX"],
                        "Energy - Gasoline & Heating Oil": ["UGA", "UHN"],
                        "Agriculture - Grains": ["CORN", "WEAT", "SOYB", "OATS", "RICE"],
                        "Agriculture - Soft Commodities": ["JO", "NIB", "SGG", "BAL", "CANE"],
                        "Agriculture - Livestock": ["COW"],
                        "Industrial Metals - Copper": ["CPER", "JJC", "COPX"],
                        "Industrial Metals - Aluminum": ["JJU"],
                        "Broad Commodity Baskets": ["DBC", "PDBC", "GSG", "USCI", "GCC", "RJI", "COMT", "CMDY"],
                        "Uranium & Nuclear": ["URA", "URNM", "NLR", "HURA"],
                    }
                    
                    for category, symbols in categories.items():
                        print(f"{YELLOW}{category}:{RESET}")
                        for sym in symbols:
                            if sym in COMMODITY_ETFS:
                                print(f"  {GREEN}{sym:6}{RESET} - {COMMODITY_ETFS[sym]}")
                        print()
                    
                    print(f"{DIM}Press Enter to continue...{RESET}")
                    input()
                    continue
                
                if not user_input:
                    print(f"{RED}⚠ Please enter something!{RESET}")
                    continue
                
                parts = user_input.split()
                
                if len(parts) < 2:
                    print(f"{RED}⚠ Invalid syntax! Use: <SYMBOL> <DATE> [TIMEFRAME]{RESET}")
                    print(f"{YELLOW}Example: GLD 2026-01-15{RESET}")
                    continue
                
                symbol = parts[0].upper()
                date = parts[1]
                
                # Validate if symbol is a known commodity ETF
                if symbol not in COMMODITY_ETFS:
                    print(f"{YELLOW}⚠ Warning: '{symbol}' is not in our commodity ETF list.{RESET}")
                    print(f"{DIM}Type 'list' to see all available commodities, or continue anyway.{RESET}")
                    confirm = input(f"{CYAN}Continue with {symbol}? (y/n):{RESET} ").strip().lower()
                    if confirm != 'y':
                        continue
                
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
                
                # Use stock price function (commodities are ETFs traded as stocks)
                result = get_stock_price(symbol, date, None, timeframe)
                
                # Add commodity name to result if available
                if symbol in COMMODITY_ETFS:
                    result['commodity_name'] = COMMODITY_ETFS[symbol]
                
                print_stock_result(result)
                
                # Show more options menu if result is valid
                if "error" not in result:
                    choice = show_more_options_menu(result, symbol, "COMMODITY")
                    
                    if choice == '1':
                        # Check live price
                        live_data = get_live_stock_price(symbol)
                        print_live_price(live_data, "COMMODITY")
                    elif choice == '2':
                        # Compare with current price
                        live_data = get_live_stock_price(symbol)
                        print_price_comparison(result, live_data, "COMMODITY")
                
                # Ask if they want to check another
                print(f"\n{DIM}Press Enter to check another commodity, or type 'back' to change market{RESET}")
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
    
    # Commodity command
    commodity_parser = subparsers.add_parser('commodity', help='Get commodity price')
    commodity_parser.add_argument('symbol', help='Commodity ETF symbol (e.g., GLD, USO)')
    commodity_parser.add_argument('date', help='Date (YYYY-MM-DD)')
    commodity_parser.add_argument('--timeframe', '-t',
                              choices=['1d', '1wk', '1mo'],
                              default='1d',
                              help='Candle timeframe (default: 1d)')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List symbols')
    list_parser.add_argument('market', choices=['crypto', 'stocks', 'commodities'], help='Market to list')
    
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
        
        elif args.command == 'commodity':
            timeframe = getattr(args, 'timeframe', '1d')
            result = get_stock_price(args.symbol, args.date, None, timeframe)
            # Add commodity name if available
            if args.symbol.upper() in COMMODITY_ETFS:
                result['commodity_name'] = COMMODITY_ETFS[args.symbol.upper()]
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
            
            elif args.market == 'commodities':
                print(f"\n{CYAN}Available Commodity ETFs ({len(COMMODITY_ETFS)} total):{RESET}\n")
                # Group by category
                categories = {
                    "Precious Metals - Gold": ["GLD", "IAU", "GLDM", "SGOL", "BAR", "AAAU", "OUNZ", "GLDL", "IAUM"],
                    "Precious Metals - Silver": ["SLV", "SIVR", "PSLV", "SLVP"],
                    "Precious Metals - Platinum & Palladium": ["PPLT", "PALL", "PLTM"],
                    "Energy - Crude Oil": ["USO", "UCO", "DBO", "USL", "BNO", "OILK", "OLEM"],
                    "Energy - Natural Gas": ["UNG", "BOIL", "KOLD", "UNL", "GAZ", "GASL", "GASX"],
                    "Energy - Gasoline & Heating Oil": ["UGA", "UHN"],
                    "Agriculture - Grains": ["CORN", "WEAT", "SOYB", "OATS", "RICE"],
                    "Agriculture - Soft Commodities": ["JO", "NIB", "SGG", "BAL", "CANE"],
                    "Agriculture - Livestock": ["COW"],
                    "Industrial Metals - Copper": ["CPER", "JJC", "COPX"],
                    "Industrial Metals - Aluminum": ["JJU"],
                    "Broad Commodity Baskets": ["DBC", "PDBC", "GSG", "USCI", "GCC", "RJI", "COMT", "CMDY"],
                    "Uranium & Nuclear": ["URA", "URNM", "NLR", "HURA"],
                }
                
                for category, symbols in categories.items():
                    print(f"{YELLOW}{category}:{RESET}")
                    for sym in symbols:
                        if sym in COMMODITY_ETFS:
                            print(f"  {GREEN}{sym:6}{RESET} - {COMMODITY_ETFS[sym]}")
                    print()
                print(f"{DIM}Total: {len(COMMODITY_ETFS)} commodity ETFs available{RESET}\n")
    
    except SystemExit:
        # argparse calls sys.exit on error, catch it
        print(f"\n{YELLOW}Tip: Run 'python stockscan.py help' for usage instructions{RESET}\n")
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Cancelled by user{RESET}\n")
    except Exception as e:
        print(f"\n{RED}Unexpected error: {e}{RESET}\n")


if __name__ == "__main__":
    main()
