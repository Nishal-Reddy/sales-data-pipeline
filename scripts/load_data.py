import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path
from urllib.parse import quote_plus

load_dotenv()
password = os.getenv("DB_PASSWORD")
if not password:
    raise ValueError("DB_PASSWORD not found")

encoded_password = quote_plus(password)

# DB connection
engine = create_engine(f"postgresql://postgres:{encoded_password}@localhost:5433/postgres")

# Load cleaned data
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "processed" / "cleaned_sales_data.csv"
df = pd.read_csv(file_path)

# Load into SQL
df.to_sql("sales_data", engine, if_exists="replace", index=False)

print("Data loaded into PostgreSQL!")