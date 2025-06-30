import csv
import pandas as pd
from datetime import datetime


def signup():
    username = input("Choose a username: ").strip()
    password = input("Choose a password: ").strip()
    with open("users.csv",mode= "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
        print("Signup successful!")
        main()

def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    try:
        with open("users.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row == [username, password]:
                    print("Login successful!")
                    return username
        print("Invalid username or password.")
        main()
    except FileNotFoundError:
        print("No users found.")
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
            print("❌ Future dates are not allowed.")
            return
        
        amount = float(amount)
    except ValueError:
        print("Invalid date or amount format.")
        return

    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username,date, category, amount, location])
        print("Expense added successfully!")

def view_expenses(username):
    try:
        df = pd.read_csv("data.csv", names=["Username","Date", "Category", "Amount","Location"])
        user_df = df[df["Username"]== username]
        #df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
        
        if user_df.empty:
            print("NO expenses found.")
            return    
        #summary = df.groupby(["Date", "Category", "location"])["Amount"].sum().reset_index()
    
        print("\n Your Expenses:")
        for _, row in user_df.iterrows():
                print(f"{row['Date']} | {row['Category']} |{row['Amount']} |{row['Location']}")
    except FileNotFoundError:
        print("No expense found.")

        
def main():
    print("Welcome to Expenses Tracker")
    print("1.Sign Up")
    print("2.Log In")
    choice = input("Enter choice (1/2): ").strip()
    
    if choice == "1":
        signup()
        return
    elif choice == "2":
        username = login()
        if not username:
            return
    else:
        print("Invalid choice.")
        return

    
    while True:
        #print("\n===== Expense Tracker Menu =====")
        print("\n1.Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        action = input("Choose an option : ").strip()

        if action == "1":
           add_expense(username)
        elif action == "2":
           view_expenses(username)
        elif action == "3":
            print("Logged out.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()


