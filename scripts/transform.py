import pandas as pd

def transform_stock_data():
    # Load raw data
    df = pd.read_csv("data/raw_stock_data.csv")

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Sort by date ascending
    df = df.sort_values("date")

    # Feature Engineering
    df["price_change"] = df["close"] - df["open"]
    df["daily_return_pct"] = (df["close"] - df["open"]) / df["open"] * 100

    # Moving averages
    df["7_day_moving_avg"] = df["close"].rolling(window=7).mean()
    df["30_day_moving_avg"] = df["close"].rolling(window=30).mean()

    # Remove rows with null values (from moving averages)
    df = df.dropna()

    # Save cleaned dataset
    df.to_csv("data/transformed_stock_data.csv", index=False)

    print("Data transformed successfully!")

if __name__ == "__main__":
    transform_stock_data()
