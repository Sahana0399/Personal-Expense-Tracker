import tkinter as tk
from tkinter import messagebox, ttk
from db import insert_expense, fetch_expense

def add_expense_window(username):
    win = tk.Toplevel()
    win.title("Add Expense")
    win.geometry("300x350")
    win.resizable(False, False)
    
    tk.Label(win, text="Add New Expense", font=("Arial",16,"bold")).pack(pady=10)

    form_frame = tk.Frame(win)
    form_frame.pack(pady=10)
    
    tk.Label(form_frame, text="Date (YYYY-MM-DD):",anchor="w").grid(row=0, column=0,sticky="w",pady=5)
    date_entry = tk.Entry(form_frame, width=25)
    date_entry.grid(row=0, column=1, pady=5)

    tk.Label(form_frame, text="Category", anchor="w").grid(row=1, column=0, sticky="w",pady=5)
    category_entry = tk.Entry(form_frame,width=25)
    category_entry.grid(row=1, column=1, pady=5)

    tk.Label(form_frame, text="Amount(£):", anchor="w").grid(row=2, column=0, sticky="w",pady=5)
    amount_entry = tk.Entry(form_frame,width=25)
    amount_entry.grid(row=2,column=1,pady=5)

    tk.Label(form_frame, text="Location:", anchor="w").grid(row=3, column=0, sticky="w", pady=5)
    location_entry = tk.Entry(form_frame, width=25)
    location_entry.grid(row=3, column=1, pady=5)

    def submit_expense():
        date = date_entry.get().strip()
        category = category_entry.get().strip()
        amount = amount_entry.get().strip()
        location = location_entry.get().strip()
        
        if not (date and category and amount and location):
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a valid number.")
            return
        
        try:
            insert_expense(username,date, category, amount, location)
            messagebox.showinfo("Success", "Expense added successfully.")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add expense:\n{e}")
                  
    tk.Button(win, text="Add Expense", command=submit_expense).pack(pady=20)
    win.mainloop()

def view_expense_window(username):
    win = tk.Toplevel()
    win.title("View Expenses")
    win.geometry("650x400")

    tk.Label(win, text=f"{username}'s Expenses", font=("Arial", 16, "bold")).pack(pady=10)

    columns = ("Date", "Category", "Amount", "Location")
    tree = ttk.Treeview(win, columns=columns, show="headings", height=15)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    scrollbar = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    scrollbar.pack(side="right", fill="y")

    try:
        expenses = fetch_expense(username)
        if not expenses:
            messagebox.showinfo("Info", "No expenses found.")
            return
        
        for row in expenses:
            tree.insert("",tk.END,values=row)
            
    except Exception as e:
           messagebox.showerror("Error",f"Failed to fetch data:\n{e}") 
    
    win.mainloop()