# gui/dashboard.py
import tkinter as tk
# from gui.expense import add_expense_window, view_expense_window

def open_dashboard(username):
    dash = tk.Tk()
    dash.title("Dashboard")
    dash.geometry("400x300")

    tk.Label(dash, text=f"Welcome, {username}!", font=("Arial", 14)).pack(pady=20)

    tk.Button(dash, text="Add Expense", width=20, command=lambda: add_expense_window(username)).pack(pady=5)
    tk.Button(dash, text="View Expenses", width=20, command=lambda: view_expense_window(username)).pack(pady=5)
    tk.Button(dash, text="Logout", width=20, command=dash.destroy).pack(pady=20)

    dash.mainloop()
