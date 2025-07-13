# gui/login_window.py
import tkinter as tk
from tkinter import messagebox
from db import fetch_user, insert_user
from gui.dashboard import open_dashboard

def login_window():
    def handle_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        user = fetch_user(username, password)
        if user:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            root.destroy()
            open_dashboard(username)
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    root = tk.Tk()
    root.title("Login - Expense Tracker")
    root.geometry("300x200")

    tk.Label(root, text="Username").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    tk.Button(root, text="Login", command=handle_login).pack(pady=10)
    tk.Button(root, text="Sign Up", command=lambda: [root.destroy(), signup_window()]).pack(pady=5)

    root.mainloop()

def signup_window():
    def handle_signup():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty.")
            return

        success = insert_user(username, password)
        if success:
            messagebox.showinfo("Success", "Account created successfully! Please log in.")
            signup_win.destroy()
            login_window()
        else:
            messagebox.showerror("Error", "Username already exists.")

    signup_win = tk.Tk()
    signup_win.title("Signup - Expense Tracker")
    signup_win.geometry("300x200")

    tk.Label(signup_win, text="Choose a Username").pack(pady=5)
    username_entry = tk.Entry(signup_win)
    username_entry.pack()

    tk.Label(signup_win, text="Choose a Password").pack(pady=5)
    password_entry = tk.Entry(signup_win, show="*")
    password_entry.pack()

    tk.Button(signup_win, text="Sign Up", command=handle_signup).pack(pady=10)

    signup_win.mainloop()
