import tkinter as tk
from tkinter import ttk
from DBConnectivity import *


# Connect to MySQL Database
def populateTree():

    rows=fetchstudentData()
    # Populate the Treeview with data
    for row in rows:
        tree.insert("", tk.END, values=row)

# Tkinter GUI
root = tk.Tk()
root.title("Database Viewer")
root.geometry("600x300")

# Treeview Widget for Table
columns = ("ID", "Name", "Address", "Phone")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Set Column Headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=70)

tree.pack(fill="both", expand=True)

# Fetch & Display Data Button
fetch_btn = tk.Button(root, text="Load Data", command=populateTree)
fetch_btn.pack()

root.mainloop()