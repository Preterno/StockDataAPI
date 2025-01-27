# StockDataAPI

StockDataAPI is a Flask-based backend service that provides historical stock data for one or more stock symbols using the Yahoo Finance API. It allows fetching closing prices of stock symbols for the last 3 months.

## Technologies Used

- Flask: A lightweight WSGI web application framework
- yfinance: Library to fetch stock data from Yahoo Finance
- CORS: Enables Cross-Origin Resource Sharing to allow requests from the frontend
- dotenv: Loads environment variables from a .env file

## API Endpoint

### GET /historical_data

Fetches the historical closing prices for a list of stock symbols over the past 3 months.

#### Request

- Method: GET
- Headers:
  - `Authorization`: Bearer `your_api_key` (required)
- Query Parameters:
  - `stocks`: A comma-separated list of stock symbols (required)

#### Response

JSON object containing:

- A key for each stock symbol
- For each stock, a dictionary where dates are keys and closing prices are values

Example request:

```
curl -X GET "http://127.0.0.1:5000/historical_data?stocks=AAPL,GOOGL/" -H "Authorization: Bearer your_secret_api_key"

```

Example response:
Example response:

```json
{
  "AAPL": {
    "2025-01-27": 148.75,
    "2025-01-26": 147.55,
    "2025-01-25": 149.25
  },
  "GOOGL": {
    "2025-01-27": 2745.5,
    "2025-01-26": 2718.75,
    "2025-01-25": 2728.9
  }
}
```

## Installation and Setup

1. Clone the repository:

   ```
   git clone https://github.com/Preterno/StockDataAPI.git
   cd StockDataAPI
   ```

2. Install required packages:

   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with the following:

   ```
   API_KEY=your_secret_api_key
   ```

4. Run the Flask application:
   ```
   python app.py
   ```

The API will be available at `http://127.0.0.1:5000/`.

## Connect with Me

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/aslam8483).