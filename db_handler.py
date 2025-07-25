import sqlite3

def create_table():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount REAL,
            description TEXT,
            date TEXT,
            type TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_transaction(transaction):
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (category, amount, description, date, type)
        VALUES (?, ?, ?, ?, ?)
    """, (transaction.category, transaction.amount, transaction.description, transaction.date, transaction.t_type))
    conn.commit()
    conn.close()

def fetch_all_transactions():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, amount, description, date, type FROM transactions")
    transactions = cursor.fetchall()
    conn.close()
    return transactions
