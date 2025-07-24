import matplotlib.pyplot as plt

def visualize_spending(transactions):
    expense_data = {}
    for t in transactions:
        if t[4] == 'Expense':
            category = t[0]
            amount = t[1]
            expense_data[category] = expense_data.get(category, 0) + amount

    if not expense_data:
        print("❌ No expenses to show in the chart.")
        return

    categories = list(expense_data.keys())
    amounts = list(expense_data.values())

    plt.figure(figsize=(7, 5))
    plt.bar(categories, amounts, color='teal')
    plt.xlabel('Category')
    plt.ylabel('Amount (₹)')
    plt.title('Expenses by Category')
    plt.tight_layout()
    plt.show()
