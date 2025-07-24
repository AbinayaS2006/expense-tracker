import sqlite3

# Connect to the database file
conn = sqlite3.connect("expense.db")
cursor = conn.cursor()

# Sample data to insert
sample_data = [
    ("Food", 1200, "2024-05-10", "May", "Expense"),
    ("Transport", 600, "2024-05-15", "May", "Expense"),
    ("Salary", 5000, "2024-05-01", "May", "Income"),
    ("Shopping", 950, "2024-06-05", "June", "Expense"),
    ("Salary", 5200, "2024-06-01", "June", "Income"),
    ("Medical", 450, "2024-07-03", "July", "Expense"),
    ("Salary", 5300, "2024-07-01", "July", "Income")
]

# Insert into table
cursor.executemany("""
    INSERT INTO expenses (category, amount, date, month, type) 
    VALUES (?, ?, ?, ?, ?)
""", sample_data)

conn.commit()
conn.close()

print("✅ Sample expense data inserted into expenses.db")
