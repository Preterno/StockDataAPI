from flask import Flask, request, jsonify
from flask_cors import CORS
import yfinance as yf
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv('API_KEY')

def require_api_key(func):
    def wrapper(*args, **kwargs):
        if request.headers.get('Authorization') != f'Bearer {API_KEY}':
            return jsonify({'message': 'Forbidden, invalid API key'}), 403
        return func(*args, **kwargs)
    return wrapper

@app.route('/historical_data', methods=['GET'])
@require_api_key
def get_historical_data():
    stock_symbols = request.args.get('stocks', '')

    if not stock_symbols:
        return jsonify({"error": "Please provide a list of stock symbols."}), 400

    stocks = stock_symbols.split(',')
    historical_data = {}

    for stock in stocks:
        try:
            ticker = yf.Ticker(stock.strip())
            data = ticker.history(period='3mo')

            historical_data[stock.strip()] = {
                date.strftime('%Y-%m-%d'): value
                for date, value in data['Close'].items()
            }
        except Exception as e:
            historical_data[stock.strip()] = {"error": str(e)}
        
    return jsonify(historical_data)

if __name__ == '__main__':
    app.run(debug=False)
