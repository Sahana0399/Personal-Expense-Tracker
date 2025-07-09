import csv
import pandas as pd
from db import connect
from db import insert_user, fetch_expense , insert_expense,fetch_user
# from signup_login import signup, login, add_expense, view_expenses
from datetime import datetime


def signup():
    username = input("Choose a username: ").strip()
    password = input("Choose a password: ").strip()
    
    insert_user(username,password)
    print("Signup successfull!")
    login()
    
def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    user = fetch_user(username,password)
    
    
    if user:
        print("Login Successfull!")
        return username
    else:
        print("Invalid username or password.")
        return None
    
def add_expense(username):
    date = input("Enter date(YYYY-MM-DD): ").strip()
    category = input("Enter category (e.g. Food, Transport): ").strip()
    amount = input("Enter amount: ").strip()
    location = input("Enter location/place of expense: ").strip()
   
    try:
        expense_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()

        if expense_date > today:
            print("Future dates are not allowed.")
            return
        
        amount = float(amount)
        print(username, date, category, amount, location)
        insert_expense(username, date, category, amount, location)
        
    except ValueError:
        print("Invalid date or amount format.")
        return

    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username,date, category, amount, location])
        print("Expense added successfully!")



def view_expense(username):
    expenses = fetch_expense(username) # type: ignore
    if not expenses:
        print("No records found.")
        return
    
    print("\nDate\t\tCategory\tAmount\tLocation")
    print("-"*50)
    for row in expenses:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
        
def main():
    connect()

    print("Welcome to Expenses Tracker")
    print("1.Sign Up")
    print("2.Log In")
    choice = input("Enter choice (1/2): ").strip()
    
    if choice == "1":
        username = signup()
    elif choice == "2":
        username = login()
    else:
        print("Invalid choice.")
        return
    
    if not username:
        return

    while True:
        print("\n1.Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        action = input("Choose an option : ").strip()

        if action == "1":
           add_expense(username)
        elif action == "2":
           view_expense(username)
        elif action == "3":
            print("Logged out.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()