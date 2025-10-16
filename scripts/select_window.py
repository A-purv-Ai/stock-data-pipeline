# Step 1.4B: Create the SELECT Window in the App (To View Records)
# When we click SELECT in the main menu, a window should open and display all records from the stocks table in a nice-looking scrollable format.

# select_window.py
import customtkinter as ctk
from tkinter import messagebox
import sqlite3

def open_select_window():
    select_win = ctk.CTkToplevel()
    select_win.title("View Stock Data")
    select_win.geometry("700x500")

    frame = ctk.CTkScrollableFrame(select_win, width=650, height=450)
    frame.pack(pady=10, padx=10)

    try:
        conn = sqlite3.connect("stocks.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stocks")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            ctk.CTkLabel(frame, text="No records found.", text_color="gray").pack()
        else:
            headers = ["ID", "Ticker", "Date", "Open", "High", "Low", "Close", "Volume"]
            header_text = " | ".join([f"{h:<10}" for h in headers])
            ctk.CTkLabel(frame, text=header_text, font=ctk.CTkFont(weight="bold")).pack(anchor="w")

            for row in rows:
                row_text = " | ".join([f"{str(item):<10}" for item in row])
                ctk.CTkLabel(frame, text=row_text).pack(anchor="w")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data:\n{e}")
