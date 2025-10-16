# Step 1.1 : Set up customTkinter GUI in main_guiM.py
# V2: Install customtkinter package using Terminal in PyCharm
#     pip install customtkinter

# Then continue with App creation
# import customtkinter as ctk
# from tkinter import messagebox
#
# ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
# ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"
#
# # Step 1.2: Added buttons: INSERT, SELECT, UPDATE, DELETE
# def insert_data():
#     messagebox.showinfo("INSERT", "Insert function called!")
#
# def select_data():
#     messagebox.showinfo("SELECT", "Select function called!")
#
# def update_data():
#     messagebox.showinfo("UPDATE", "Update function called!")
#
# def delete_data():
#     messagebox.showinfo("DELETE", "Delete function called!")
#
# # Main app
# app = ctk.CTk()
# app.geometry("300x350")
# app.title("Stock App - Modern")
#
# label = ctk.CTkLabel(app, text="Main Menu", font=ctk.CTkFont(size=20, weight="bold"))
# label.pack(pady=20)
#
# btn_insert = ctk.CTkButton(app, text="INSERT", width=200, command=insert_data)
# btn_insert.pack(pady=10)
#
# btn_select = ctk.CTkButton(app, text="SELECT", width=200, command=select_data)
# btn_select.pack(pady=10)
#
# btn_update = ctk.CTkButton(app, text="UPDATE", width=200, command=update_data)
# btn_update.pack(pady=10)
#
# btn_delete = ctk.CTkButton(app, text="DELETE", width=200, command=delete_data)
# btn_delete.pack(pady=10)
#
# app.mainloop()

# Now, Making Modifications to our main_guiM.py
import customtkinter as ctk
# Step 1.3B: Modify main_guiM.py to Connect insert_window to main_guiM.py
from insert_window import open_insert_window  # ✅ Import INSERT form

# Step 1.4B: Import SELECT window function   #Step 1.4A was to check stock.db data stored successfully using db browser sqlite.
from select_window import open_select_window

# Step 1.5A: Import UPDATE window
from update_window import open_update_window

# Step 1.6: Import DELETE window
from delete_window import open_delete_window

from db_utils import create_table  # ✅ Ensure DB table is created

# ✅ Initialize table (creates it only if not already there)
create_table()

# ✅ Setup main window
app = ctk.CTk()
app.geometry("300x350")
app.title("Stock App - Modern")

# ✅ Title label
ctk.CTkLabel(app, text="Main Menu", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

# ✅ Buttons
# Step 1.3B: INSERT button Modification
insert_button = ctk.CTkButton(app, text="INSERT", command=open_insert_window)
insert_button.pack(pady=10)

# Step 1.4B: SELECT button Modification
# ctk.CTkButton(app, text="SELECT", width=200, command=lambda: print("SELECT clicked")).pack(pady=10) #old code during 1.3B
select_button = ctk.CTkButton(app, text="SELECT", command=open_select_window) #new code as per step 1.4B
select_button.pack(pady=10)

# Step 1.5A: UPDATE button Modification
# ctk.CTkButton(app, text="UPDATE", width=200, command=lambda: print("UPDATE clicked")).pack(pady=10) #old code during 1.3B
update_button = ctk.CTkButton(app, text="UPDATE", command=open_update_window) #new code as per step 1.5B
update_button.pack(pady=10)

# Step 1.6: DELETE button Modification
# ctk.CTkButton(app, text="DELETE", width=200, command=lambda: print("DELETE clicked")).pack(pady=10) #old code during 1.3B
delete_button = ctk.CTkButton(app, text="DELETE", command=open_delete_window) #new code as per step 1.6B
delete_button.pack(pady=10)

# ✅ Start GUI loop
app.mainloop()
