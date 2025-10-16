# Step 1.3A.1 – Create db_utils.py
# This file will hold the database logic (e.g. create table, insert stock).

import sqlite3

def create_table():
    conn = sqlite3.connect("stocks.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL,
            date TEXT NOT NULL,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_stock(ticker, date, open_, high, low, close, volume):
    conn = sqlite3.connect("stocks.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO stocks (ticker, date, open, high, low, close, volume)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (ticker, date, open_, high, low, close, volume))
    conn.commit()
    conn.close()
