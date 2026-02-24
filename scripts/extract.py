import requests
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

TICKERS = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

def get_stock_data(symbol):
    url = "https://www.alphavantage.co/query"

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    time_series = data.get("Time Series (Daily)", {})
    records = []

    for date, values in time_series.items():
        records.append({
            "symbol": symbol,
            "date": date,
            "open": float(values["1. open"]),
            "high": float(values["2. high"]),
            "low": float(values["3. low"]),
            "close": float(values["4. close"]),
            "volume": int(values["5. volume"]),
            "extracted_at": datetime.now()
        })

    return pd.DataFrame(records)

if __name__ == "__main__":
    all_data = []

    for ticker in TICKERS:
        print(f"Fetching {ticker}...")
        df = get_stock_data(ticker)
        all_data.append(df)

    final_df = pd.concat(all_data, ignore_index=True)

    os.makedirs("data", exist_ok=True)
    final_df.to_csv("data/raw_stock_data.csv", index=False)

    print("Multi-stock data extracted!")
