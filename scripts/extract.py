import requests
import pandas as pd
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_stock_data(symbol="AAPL"):
    url = "https://www.alphavantage.co/query"

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    time_series = data["Time Series (Daily)"]

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

    df = pd.DataFrame(records)
    return df

if __name__ == "__main__":
    df = get_stock_data("AAPL")
    df.to_csv("data/raw_stock_data.csv", index=False)
    print("Stock data extracted!")
