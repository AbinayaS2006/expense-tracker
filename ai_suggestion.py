def generate_ai_suggestion(transactions):
    total_income = sum(t[1] for t in transactions if t[4] == 'Income')
    total_expense = sum(t[1] for t in transactions if t[4] == 'Expense')
    savings = total_income - total_expense

    suggestion = "\n🧠 AI Suggestion:\n"
    suggestion += f"💰 Total Income: ₹{total_income:.2f}\n"
    suggestion += f"💸 Total Expenses: ₹{total_expense:.2f}\n"
    suggestion += f"💼 Savings: ₹{savings:.2f}\n"

    if total_income == 0:
        suggestion += "❗ You're not recording any income. Add income sources!"
    elif savings < 0:
        suggestion += "⚠️ You're spending more than your income! Try reducing unnecessary expenses."
    elif savings < total_income * 0.2:
        suggestion += "📉 Your savings rate is low. Consider budgeting tighter."
    else:
        suggestion += "✅ Great! You're saving well."

    return suggestion
