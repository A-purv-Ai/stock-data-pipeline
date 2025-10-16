# 🧱 Step 3.1 – Create the File export_csv.py

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("stocks.db")

# Query to fetch all stock data
query = "SELECT * FROM stocks ORDER BY ticker, date"

# Load the query result into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Export the DataFrame to CSV
csv_filename = "stock_data_export.csv"
df.to_csv(csv_filename, index=False)

# Close the connection
conn.close()

print(f"✅ Exported data to: {csv_filename}")


# 🧪 Step 3.2 – Run It
# Run the script in PyCharm or terminal:
# python export_csv.py

# It will generate a file in your current folder:
# 📁 stock_data_export.csv