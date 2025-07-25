import matplotlib.pyplot as plt
from db_handler import fetch_all_transactions

def show_spending_chart():
    transactions = fetch_all_transactions()
    categories = {}

    for t in transactions:
        if t[4].lower() == 'expense':
            cat = t[0]
            amt = float(t[1])
            categories[cat] = categories.get(cat, 0) + amt

    if not categories:
        print("❌ No expenses to display.")
        return

    plt.figure(figsize=(8, 5))
    plt.bar(categories.keys(), categories.values(), color='teal')
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
