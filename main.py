from transaction import Transaction
from db_handler import create_table, add_transaction, fetch_all_transactions
from ai_suggestion import generate_ai_suggestion
from spending_chart import show_spending_chart
from datetime import datetime
import sqlite3

create_table()

def menu():
    print("\n=== AI-Powered Expense Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Analyze Spending (AI)")
    print("5. 📊 Visualize Expense Report")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        category = input("Enter income category: ")
        amount = float(input("Enter amount: ₹"))
        description = input("Enter description: ")
        date = input("Enter date (YYYY-MM-DD) [leave blank for today]: ")
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')
        t = Transaction(category, amount, description, date, "Income")
        add_transaction(t)
        print("✅ Income added.")

    elif choice == '2':
        category = input("Enter expense category: ")
        amount = float(input("Enter amount: ₹"))
        description = input("Enter description: ")
        date = input("Enter date (YYYY-MM-DD) [leave blank for today]: ")
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')
        t = Transaction(category, amount, description, date, "Expense")
        add_transaction(t)
        print("✅ Expense added.")

    elif choice == '3':
        print("\n=== Transactions ===")
        transactions = fetch_all_transactions()
        if transactions:
            for t in transactions:
                print(f"{t[4]} - ₹{float(t[1]):.2f} - {t[0]} - {t[2]} - {t[3]}")
        else:
            print("No transactions found.")

    elif choice == '4':
        transactions = fetch_all_transactions()
        print(generate_ai_suggestion(transactions))

    elif choice == '5':
        show_spending_chart()

    elif choice == '6':
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
