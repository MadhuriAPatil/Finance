import yfinance as yf
from datetime import datetime
import pytz

def get_stock_info(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        if 'shortName' not in info or 'regularMarketPrice' not in info:
            raise ValueError("Invalid symbol or data not available.")

        # Get local current time
        local_time = datetime.now(pytz.timezone("US/Pacific"))
        print("\n" + local_time.strftime("%a %b %d %H:%M:%S %Z %Y") + "\n")

        company_name = f"{info['shortName']} ({symbol.upper()})"
        price = info['regularMarketPrice']
        change = info.get('regularMarketChange', 0)
        percent_change = info.get('regularMarketChangePercent', 0)

        change_sign = "+" if change >= 0 else "-"
        percent_sign = "+" if percent_change >= 0 else "-"

        print(company_name)
        print(f"{price:.2f} {change_sign}{abs(change):.2f} ({percent_sign}{abs(percent_change):.2f}%)\n")

    except Exception as e:
        print(f"Error: {str(e)}")
        print("Please check your internet connection or enter a valid stock symbol.\n")

def main():
    while True:
        symbol = input("Please enter a symbol (or type 'exit' to quit):\n").strip()
        if symbol.lower() == "exit":
            break
        get_stock_info(symbol)

if __name__ == "__main__":
    main()
