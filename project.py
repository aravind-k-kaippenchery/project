import pandas as pd
import matplotlib.pyplot as plt
import os


DATA_FILE = "expenses.csv"

if os.path.exists(DATA_FILE):
    expenses = pd.read_csv(DATA_FILE)
else:
    expenses = pd.DataFrame(columns=["Date", "Category", "Amount"])

def menu():
    print("\nPersonal Expense Tracker")
    print("1. Log Expenses")
    print("2. Analyze Data")
    print("3. Visualize Data")
    print("4. Exit")
    return input("Choose an option (1-4): ")

def log_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel): ")
    amount = float(input("Enter amount: "))
    global expenses
    expenses = pd.concat([expenses, pd.DataFrame({"Date": [date], "Category": [category], "Amount": [amount]})], ignore_index=True)
    expenses.to_csv(DATA_FILE, index=False)
    print("Expense logged successfully!")

def analyze_data():
    if expenses.empty:
        print("No data to analyze.")
        return
    total_spending = expenses["Amount"].sum()
    print(f"Total Spending: ${total_spending:.2f}")
    category_wise = expenses.groupby("Category")["Amount"].sum()
    print("\nCategory-wise Breakdown:")
    print(category_wise)

def visualize_data():
    if expenses.empty:
        print("No data to visualize.")
        return

    category_wise = expenses.groupby("Category")["Amount"].sum()
    category_wise.plot(kind="bar", title="Category-wise Spending")
    plt.ylabel("Amount")
    plt.show()

    expenses["Date"] = pd.to_datetime(expenses["Date"])
    daily_trends = expenses.groupby("Date")["Amount"].sum()
    daily_trends.plot(kind="line", title="Daily Spending Trends")
    plt.ylabel("Amount")
    plt.show()


while True:
    choice = menu()
    if choice == "1":
        log_expense()
    elif choice == "2":
        analyze_data()
    elif choice == "3":
        visualize_data()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")