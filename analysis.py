import pandas as pd
import matplotlib.pyplot as plt

def show_expense_summary():
    df = pd.read_csv("data.csv", names=["Date","Category", "Amount"])
    df["Date"] = pd.to_datetime(df["Date"])
    
    category_sum = df.groupby("Category")["Amount"].sum()
    category_sum.plot(kind="bar", title="Spending by Category", colormap= "viridis")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()
    
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_sum = df.groupby("Month")["Amount"].sum()
    monthly_sum.plot(kind= "line" , title="Monthly Spending" , marker = 'o')
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()
    
    if __name__ == " __main__":
        show_expense_summary()
                                   