from flask import Flask, request, render_template
import yfinance as yf
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_data = {}
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        try:
            stock = yf.Ticker(symbol)
            info = stock.info

            if 'shortName' not in info or 'regularMarketPrice' not in info:
                raise ValueError("Invalid symbol or data not available.")

            local_time = datetime.now(pytz.timezone("US/Pacific"))
            stock_data = {
                'time': local_time.strftime("%a %b %d %H:%M:%S %Z %Y"),
                'company': f"{info['shortName']} ({symbol.upper()})",
                'price': f"{info['regularMarketPrice']:.2f}",
                'change': f"{info.get('regularMarketChange', 0):+.2f}",
                'percent_change': f"{info.get('regularMarketChangePercent', 0):+.2f}%"
            }
        except Exception as e:
            stock_data = {'error': str(e)}
    return render_template('index.html', stock_data=stock_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
