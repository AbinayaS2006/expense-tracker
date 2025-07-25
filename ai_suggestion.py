def generate_ai_suggestion(transactions):
    total_income = sum(t[1] for t in transactions if t[4].lower() == "income")
    total_expense = sum(t[1] for t in transactions if t[4].lower() == "expense")
    savings = total_income - total_expense

    suggestion = "\n=== AI Suggestion ===\n"
    suggestion += f"💰 Total Income: ₹{total_income:.2f}\n"
    suggestion += f"💸 Total Expenses: ₹{total_expense:.2f}\n"
    suggestion += f"💼 Savings: ₹{savings:.2f}\n"

    if total_income == 0:
        suggestion += "❗ You're not recording any income. Add income sources!\n"
    if total_expense == 0:
        suggestion += "❗ No expenses to analyze. Try spending money wisely!\n"
    elif total_expense > total_income:
        suggestion += "⚠️ You are overspending! Try to cut down unnecessary expenses.\n"
    else:
        suggestion += "✅ Great job! You are managing your finances well.\n"

    return suggestion
