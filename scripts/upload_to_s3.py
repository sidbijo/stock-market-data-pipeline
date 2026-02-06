import boto3
import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def upload_file(file_path, s3_key):
    s3.upload_file(file_path, BUCKET_NAME, s3_key)
    print(f"Uploaded {file_path} to s3://{BUCKET_NAME}/{s3_key}")

if __name__ == "__main__":
    upload_file(
        "data/raw_stock_data.csv",
        "raw/stock_data.csv"
    )

    upload_file(
        "data/transformed_stock_data.csv",
        "processed/stock_data.csv"
    )
