class Transaction:
    def __init__(self, category, amount, description, date, t_type):
        self.category = category
        self.amount = amount
        self.description = description
        self.date = date
        self.type = t_type  # 'Income' or 'Expense'
