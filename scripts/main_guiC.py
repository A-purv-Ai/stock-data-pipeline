# V1: Classic Desktop App creation using Tkinter library

import tkinter as tk
from tkinter import messagebox

def insert_data():
    messagebox.showinfo("INSERT", "Insert function called!")

def select_data():
    messagebox.showinfo("SELECT", "Select function called!")

def update_data():
    messagebox.showinfo("UPDATE", "Update function called!")

def delete_data():
    messagebox.showinfo("DELETE", "Delete function called!")

# Main window
root = tk.Tk()
root.title("Stock App - Tkinter")
root.geometry("300x300")

title = tk.Label(root, text="Main Menu", font=("Arial", 16))
title.pack(pady=20)

btn_insert = tk.Button(root, text="INSERT", width=20, command=insert_data)
btn_insert.pack(pady=5)

btn_select = tk.Button(root, text="SELECT", width=20, command=select_data)
btn_select.pack(pady=5)

btn_update = tk.Button(root, text="UPDATE", width=20, command=update_data)
btn_update.pack(pady=5)

btn_delete = tk.Button(root, text="DELETE", width=20, command=delete_data)
btn_delete.pack(pady=5)

root.mainloop()
