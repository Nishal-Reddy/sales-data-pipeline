# Sales Data Analysis Pipeline

## 📌 Overview

This project simulates a real-world data engineering workflow by building an ETL pipeline using Python and PostgreSQL. Raw e-commerce data is extracted, transformed, and loaded into a relational database for analysis.

## ⚙️ Tech Stack

* Python (Pandas)
* PostgreSQL
* SQLAlchemy
* SQL

## 🔄 Pipeline Steps

1. Extract raw CSV data
2. Transform data (cleaning, datetime conversion, joins)
3. Load into PostgreSQL
4. Perform analytical queries

## 📊 Key Analysis

* Monthly revenue trends
* Top-selling products
* Customer spending behavior

## 🧠 Key Learnings

* Built end-to-end ETL pipeline
* Handled missing data intelligently
* Designed efficient SQL queries
* Worked with relational data modeling concepts

## 🚀 How to Run

1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt
3. Set DB password:
   export DB_PASSWORD=yourpassword
4. Run pipeline:
   python scripts/etl_pipeline.py

## 📌 Future Improvements

* Add incremental data loading
* Add data validation checks
* Integrate scheduling (Airflow)
