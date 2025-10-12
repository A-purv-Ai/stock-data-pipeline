# Stock Data Management App & Data-to-Visualization Pipeline

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3.x-lightgrey?logo=sqlite&logoColor=blue)](https://www.sqlite.org/index.html)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-ModernGUI-orange)](https://github.com/TomSchimansky/CustomTkinter)
[![Tableau](https://img.shields.io/badge/Tableau-Dashboard-purple?logo=tableau&logoColor=white)](https://www.tableau.com/)
[![Pandas](https://img.shields.io/badge/Pandas-DataProcessing-lightblue?logo=pandas&logoColor=black)](https://pandas.pydata.org/)

---

## Overview
This is an **end-to-end stock data management and visualization project**. It integrates:
- **Desktop App (CustomTkinter)** for CRUD operations
- **SQLite** database for local storage
- **Pandas & CSV export** for data manipulation
- **Tableau** for downstream visualization

The workflow automates fetching historical stock data from **Yahoo Finance** (MSFT, IBM, AAPL, MS) and creates a **data-to-visualization pipeline**.

---

## Features
- 🖥️ **Modern GUI** with CustomTkinter
- 🔄 **Full CRUD Operations** (Create, Read, Update, Delete)
- 📥 **Automated Data Fetch** from Yahoo Finance
- 🗄️ **SQLite database** with duplicate prevention
- 📤 **CSV Export** for Tableau or other analysis tools
- ⚡ **Classic & Modern GUI** support (`main_guiC.py` / `main_guiM.py`)

---

## Tech Stack
| Category | Tools / Libraries |
|----------|------------------|
| Frontend GUI | CustomTkinter |
| Backend Database | SQLite3 |
| Data Fetching | yfinance |
| Data Handling | Pandas |
| Visualization | Tableau |
| Environment | Python 3.11+ |

---

## ⚙️ Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/A-purv-Ai/stock-data-management-and-data-to-visualization-pipeline.git](https://github.com/A-purv-Ai/stock-data-management-and-data-to-visualization-pipeline.git)
    cd stock-data-management-and-data-to-visualization-pipeline
    ```
2.  **Install dependencies**
    ```bash
    pip install customtkinter yfinance pandas
    ```
3.  **Run the modern GUI**
    ```bash
    python main_guiM.py
    ```
    *(Alternatively, run `python main_guiC.py` for the classic version.)*

4.  **Inspect the database**
    - Open `stocks.db` using a tool like **DB Browser for SQLite**.
    - Verify that data insertion and other CRUD operations from the GUI are working correctly.

5.  **Export & Visualize**
    - Run the export script to generate a CSV file from the database.
      ```bash
      python export_csv.py
      ```
    - Import the resulting `stock_data_export.csv` file into **Tableau** to create interactive dashboards.

---

## 📂 Project Structure
📦 STOCK-DATA-PIPELINE/
├── main_guiM.py         # Modern GUI (CustomTkinter)
├── main_guiC.py         # Classic GUI (Tkinter)
├── db_utils.py          # Database utilities (table creation, etc.)
├── insert_window.py     # GUI window for INSERT
├── select_window.py     # GUI window for SELECT
├── update_window.py     # GUI window for UPDATE
├── delete_window.py     # GUI window for DELETE
├── import_yahoo.py      # Automated Yahoo Finance data importer
├── export_csv.py        # CSV export script
├── stocks.db            # SQLite database file
└── README.md            # Project documentation


---

## 📊 Data-to-Visualization Flow
Yahoo Finance API → SQLite DB → CustomTkinter App (CRUD) → CSV Export → Tableau Dashboard


---

## 🔮 Future Enhancements
- Interactive charts inside the GUI
- Data filtering, sorting, and search functionality
- Multi-user support & authentication
- Executable build (`.exe` or `.app`) for easy distribution

---

## 👤 Author
**Apurva Upadhyay**
*Data Analytics | Data Science | Python | AI Engineering*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/upadhyayapurva) [![email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:apurvaupadhyayai@gmail.com)

📫 Feel free to connect and share feedback!

---

## 🏷️ Keywords
Python, CustomTkinter, SQLite, Pandas, Yahoo Finance, Tableau, Data Pipeline, Stock Analysis
