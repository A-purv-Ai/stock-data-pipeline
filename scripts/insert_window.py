#  Step 1.3A.2: Create a separate Python file: insert_window.py
#             Move the INSERT form there
#             Link it in main_guiM.py

import customtkinter as ctk
import tkinter.messagebox as messagebox
from db_utils import insert_stock

def open_insert_window():
    insert_win = ctk.CTkToplevel()
    insert_win.title("Insert Stock Data")
    insert_win.geometry("400x600")
    # Either remove win.geometry in order let pop-up window dynamically resize to fit all contents.
    # Or, set height to 600 in insert_win.geometry("400x600")  # Gives you extra buffer

    fields = ["Ticker", "Date (YYYY-MM-DD)", "Open", "High", "Low", "Close", "Volume"]
    entries = {}

    for i, label in enumerate(fields):
        ctk.CTkLabel(insert_win, text=label).pack(pady=(10 if i == 0 else 5, 2))
        entry = ctk.CTkEntry(insert_win, width=250)
        entry.pack(pady=2)
        entries[label.lower()] = entry

    def handle_insert():
        try:
            insert_stock(
                entries["ticker"].get().strip(),
                entries["date (yyyy-mm-dd)"].get().strip(),
                float(entries["open"].get()),
                float(entries["high"].get()),
                float(entries["low"].get()),
                float(entries["close"].get()),
                int(entries["volume"].get())
            )
            messagebox.showinfo("Success", "Stock data inserted successfully.")
            insert_win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to insert data:\n{e}")

    ctk.CTkButton(insert_win, text="Insert", command=handle_insert).pack(pady=20)
