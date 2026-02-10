#!/usr/bin/env python3
"""
StockScan Data Exporter - CSV Export & Backtesting Tool
Export historical price data to CSV for backtesting and analysis

This is a SEPARATE tool from StockScan - it doesn't modify the main program.

Copyright (c) 2026 Prasidh P Shetty
Licensed under the MIT License
"""

import sys
import csv
import os
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List

try:
    import requests
except ImportError:
    print("\nError: 'requests' library not installed")
    print("Install it with: pip install requests")
    sys.exit(1)

# ANSI Color Codes
PURPLE = '\033[95m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

# API Configuration
BINANCE_BASE = "https://api.binance.com/api/v3"


def print_banner():
    """Print banner"""
    banner = f"""
{PURPLE}╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║           STOCKSCAN DATA EXPORTER - CSV & BACKTESTING            ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝{RESET}

{CYAN}What does this tool do?{RESET}
  • Export historical price data to CSV files
  • Fetch bulk data for backtesting strategies
  • Download multiple timeframes at once
  • Perfect for algorithmic trading analysis

{CYAN}Supported Markets:{RESET}
  • Crypto: Binance (1000+ pairs, 16 timeframes)
  • Stocks: Yahoo Finance (coming soon)
  • Commodities: Yahoo Finance (coming soon)

{GREEN}✅ NO API KEYS NEEDED!{RESET}
"""
    print(banner)


def fetch_crypto_bulk_data(symbol: str, start_date: str, end_date: str, timeframe: str = "1d") -> List[Dict[str, Any]]:
    """
    Fetch bulk crypto data from Binance for a date range
    
    Args:
        symbol: Trading pair (e.g., BTCUSDT)
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        timeframe: Candle interval (1m, 5m, 15m, 1h, 1d, etc.)
    
    Returns:
        List of candle data dictionaries
    """
    try:
        # Parse dates
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Check if future
        if start_dt > datetime.now() or end_dt > datetime.now():
            return {"error": "Cannot fetch future data"}
        
        # Convert to milliseconds
        start_ms = int(start_dt.timestamp() * 1000)
        end_ms = int(end_dt.timestamp() * 1000)
        
        # Fetch data from Binance
        url = f"{BINANCE_BASE}/klines"
        params = {
            "symbol": symbol,
            "interval": timeframe,
            "startTime": start_ms,
            "endTime": end_ms,
            "limit": 1000  # Max limit per request
        }
        
        all_data = []
        
        print(f"{CYAN}Fetching data for {symbol} from {start_date} to {end_date}...{RESET}")
        
        while True:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                break
            
            # Process each candle
            for candle in data:
                candle_data = {
                    "timestamp": datetime.fromtimestamp(candle[0] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                    "open": float(candle[1]),
                    "high": float(candle[2]),
                    "low": float(candle[3]),
                    "close": float(candle[4]),
                    "volume": float(candle[5]),
                    "close_time": datetime.fromtimestamp(candle[6] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                }
                all_data.append(candle_data)
            
            # Check if we got all data
            if len(data) < 1000:
                break
            
            # Update start time for next batch
            params["startTime"] = data[-1][0] + 1
            
            print(f"{GREEN}Fetched {len(all_data)} candles...{RESET}")
        
        print(f"{GREEN}✓ Total: {len(all_data)} candles fetched{RESET}\n")
        return all_data
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch data: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


def export_to_csv(data: List[Dict[str, Any]], filename: str, symbol: str, timeframe: str):
    """
    Export data to CSV file
    
    Args:
        data: List of candle data
        filename: Output filename
        symbol: Trading symbol
        timeframe: Timeframe used
    """
    try:
        # Create exports directory if it doesn't exist
        os.makedirs("exports", exist_ok=True)
        
        filepath = os.path.join("exports", filename)
        
        with open(filepath, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data)
        
        print(f"{GREEN}✓ Data exported successfully!{RESET}")
        print(f"{CYAN}File:{RESET} {filepath}")
        print(f"{CYAN}Rows:{RESET} {len(data)}")
        print(f"{CYAN}Symbol:{RESET} {symbol}")
        print(f"{CYAN}Timeframe:{RESET} {timeframe}\n")
        
        return filepath
    
    except Exception as e:
        print(f"{RED}✗ Error exporting to CSV: {str(e)}{RESET}")
        return None


def interactive_mode():
    """Interactive mode for data export"""
    print_banner()
    
    while True:
        print(f"\n{CYAN}{'─' * 70}{RESET}")
        print(f"{BOLD}{PURPLE}EXPORT CRYPTO DATA TO CSV{RESET}\n")
        
        # Get symbol
        symbol = input(f"{CYAN}Enter symbol (e.g., BTCUSDT):{RESET} ").strip().upper()
        if not symbol:
            print(f"{RED}⚠ Symbol cannot be empty!{RESET}")
            continue
        
        # Get start date
        start_date = input(f"{CYAN}Enter start date (YYYY-MM-DD):{RESET} ").strip()
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            print(f"{RED}⚠ Invalid date format! Use YYYY-MM-DD{RESET}")
            continue
        
        # Get end date
        end_date = input(f"{CYAN}Enter end date (YYYY-MM-DD):{RESET} ").strip()
        try:
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            print(f"{RED}⚠ Invalid date format! Use YYYY-MM-DD{RESET}")
            continue
        
        # Get timeframe
        print(f"\n{CYAN}Available timeframes:{RESET}")
        print(f"  {GREEN}[1]{RESET}  1m   - 1 minute")
        print(f"  {GREEN}[2]{RESET}  5m   - 5 minutes")
        print(f"  {GREEN}[3]{RESET}  15m  - 15 minutes")
        print(f"  {GREEN}[4]{RESET}  1h   - 1 hour")
        print(f"  {GREEN}[5]{RESET}  4h   - 4 hours")
        print(f"  {GREEN}[6]{RESET}  1d   - 1 day")
        print(f"  {GREEN}[7]{RESET}  1w   - 1 week\n")
        
        timeframe_map = {
            '1': '1m',
            '2': '5m',
            '3': '15m',
            '4': '1h',
            '5': '4h',
            '6': '1d',
            '7': '1w'
        }
        
        tf_choice = input(f"{CYAN}Select timeframe (1-7):{RESET} ").strip()
        if tf_choice not in timeframe_map:
            print(f"{RED}⚠ Invalid choice!{RESET}")
            continue
        
        timeframe = timeframe_map[tf_choice]
        
        # Fetch data
        print(f"\n{CYAN}{'─' * 70}{RESET}\n")
        data = fetch_crypto_bulk_data(symbol, start_date, end_date, timeframe)
        
        if isinstance(data, dict) and "error" in data:
            print(f"{RED}✗ Error: {data['error']}{RESET}")
            continue
        
        if not data:
            print(f"{RED}✗ No data found{RESET}")
            continue
        
        # Generate filename
        filename = f"{symbol}_{timeframe}_{start_date}_to_{end_date}.csv"
        
        # Export to CSV
        export_to_csv(data, filename, symbol, timeframe)
        
        # Ask if user wants to export more
        print(f"{CYAN}{'─' * 70}{RESET}")
        choice = input(f"\n{CYAN}Export more data? (y/n):{RESET} ").strip().lower()
        if choice != 'y':
            print(f"\n{PURPLE}Thanks for using StockScan Data Exporter! 👋{RESET}\n")
            break


def main():
    """Main entry point"""
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        print(f"{YELLOW}Command-line mode coming soon!{RESET}")
        print(f"{CYAN}For now, run without arguments for interactive mode:{RESET}")
        print(f"  python stockscan_exporter.py\n")


if __name__ == "__main__":
    main()
