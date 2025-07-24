import sqlite3

def create_table():
    conn = sqlite3.connect("expense.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount REAL,
            description TEXT,
            date TEXT,
            type TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_transaction(transaction):
    conn = sqlite3.connect("expense.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO transactions (category, amount, description, date, type)
        VALUES (?, ?, ?, ?, ?)
    ''', (transaction.category, transaction.amount, transaction.description, transaction.date, transaction.type))
    conn.commit()
    conn.close()
def fetch_all_transactions():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    return rows