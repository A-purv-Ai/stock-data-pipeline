# Step 1.5A: Update stock record by ID

import customtkinter as ctk
from tkinter import messagebox
import sqlite3

def open_update_window():
    update_win = ctk.CTkToplevel()
    update_win.title("Update Stock Record")
    update_win.geometry("400x700")

    def fetch_record():
        try:
            stock_id = int(id_entry.get())
            conn = sqlite3.connect("stocks.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM stocks WHERE id = ?", (stock_id,))
            record = cursor.fetchone()
            conn.close()

            if record:
                # Fill fields with existing data
                for i, entry in enumerate(field_entries):
                    entry.delete(0, 'end')
                    entry.insert(0, str(record[i+1]))  # skip ID (i+1)
            else:
                messagebox.showwarning("Not found", f"No record with ID {stock_id} found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_record():
        try:
            stock_id = int(id_entry.get())
            values = [entry.get() for entry in field_entries]

            conn = sqlite3.connect("stocks.db")
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE stocks
                SET ticker=?, date=?, open=?, high=?, low=?, close=?, volume=?
                WHERE id=?
            """, (*values, stock_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Record ID {stock_id} updated.")
            update_win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Step 1: Ask for Stock ID
    ctk.CTkLabel(update_win, text="Enter Stock ID to Update:").pack(pady=5)
    id_entry = ctk.CTkEntry(update_win)
    id_entry.pack(pady=5)
    ctk.CTkButton(update_win, text="Fetch Record", command=fetch_record).pack(pady=10)

    # Step 2: Editable Fields
    labels = ["Ticker", "Date", "Open", "High", "Low", "Close", "Volume"]
    field_entries = []

    for label in labels:
        ctk.CTkLabel(update_win, text=label).pack()
        entry = ctk.CTkEntry(update_win)
        entry.pack(pady=3)
        field_entries.append(entry)

    # Step 3: Save Button
    ctk.CTkButton(update_win, text="Save Changes", command=update_record).pack(pady=20)
