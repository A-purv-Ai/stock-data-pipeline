# Step 1.6: Delete a stock record by ID
import customtkinter as ctk
from tkinter import messagebox
import sqlite3

def open_delete_window():
    delete_win = ctk.CTkToplevel()
    delete_win.title("Delete Stock Record")
    delete_win.geometry("300x200")

    def delete_record():
        try:
            stock_id = int(id_entry.get())
            conn = sqlite3.connect("stocks.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM stocks WHERE id = ?", (stock_id,))
            conn.commit()
            if cursor.rowcount == 0:
                messagebox.showwarning("Not Found", f"No record with ID {stock_id} found.")
            else:
                messagebox.showinfo("Success", f"Record ID {stock_id} deleted.")
            conn.close()
            delete_win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Entry UI
    ctk.CTkLabel(delete_win, text="Enter Stock ID to Delete:").pack(pady=10)
    id_entry = ctk.CTkEntry(delete_win)
    id_entry.pack(pady=10)

    delete_button = ctk.CTkButton(delete_win, text="Delete", command=delete_record)
    delete_button.pack(pady=20)
