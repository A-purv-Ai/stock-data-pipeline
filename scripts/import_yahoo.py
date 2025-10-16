# Step 2.2: Fetch and insert stock data from Yahoo Finance

# 🧩 1. Imports & DB Connection
import yfinance as yf
import sqlite3
from datetime import datetime


# Connect to database
conn = sqlite3.connect("stocks.db")
cursor = conn.cursor()

# Optional: Clear old data (uncomment if needed)
# ⚠️ WARNING: This will delete all records in the stocks table
# ⚠️ Step 1: Clear old data (only run once intentionally)
cursor.execute("DELETE FROM stocks")
conn.commit()
print("🧹 Cleared all existing stock records.")

# 📥 2. Stock List and Date Range
# Define the stocks and date range
tickers = ["MSFT", "IBM", "AAPL", "MS"]  # you can adjust this
start_date = "2014-01-01"
end_date = "2024-12-31"

# 🔁 3. For Each Ticker: Download + Duplicate-Checked Insert (STEP 2 GOES HERE)
for ticker in tickers:
    print(f"\n📥 Fetching data for {ticker}...")

    # Download daily stock data for the past 10 years
    data = yf.download(ticker, start=start_date, end=end_date, interval="1d")

    # Counter to track how many new rows we insert (for visibility)
    insert_count = 0

    # Iterate over each row (i.e., each date's data)
    for index, row in data.iterrows():
        # Format the index (which is a datetime object) as a string date
        date_str = index.strftime("%Y-%m-%d")

        # 🔍 STEP 2: Duplicate Check if the (ticker, date) record already exists in the DB
        cursor.execute("""
            SELECT 1 FROM stocks WHERE ticker = ? AND date = ?
        """, (ticker, date_str))

        exists = cursor.fetchone()

        if not exists:
            # ✅ Record does NOT exist, safe to insert it into the table
            cursor.execute("""
                INSERT INTO stocks (ticker, date, open, high, low, close, volume)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                ticker,
                date_str,
                row["Open"].item(),   # Ensure it's native Python float
                row["High"].item(),
                row["Low"].item(),
                row["Close"].item(),
                int(row["Volume"].item())  # Convert volume safely to int
            ))
            insert_count += 1  # Increment insert counter
        else:
            # 🚫 Skip: this (ticker, date) entry already exists
            continue

    # 🧾 Print how many new records were inserted for each ticker
    print(f"✅ Inserted {insert_count} new records for {ticker}")


# 🔒 4. Save & Close
conn.commit()
conn.close()
print("✅ Data imported into stocks.db")


