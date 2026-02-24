import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def load_data():
    df = pd.read_csv("data/transformed_stock_data.csv")
    df.to_sql("stock_prices", engine, if_exists="replace", index=False)
    print("Data loaded into PostgreSQL!")

if __name__ == "__main__":
    load_data()
