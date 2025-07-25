import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data from SQLite database (not CSV)
def load_data():
    try:
        conn = sqlite3.connect("expense.db")  # Use correct file name
        df = pd.read_sql_query("""
            SELECT strftime('%Y-%m', date) AS month, SUM(amount) as total 
            FROM transactions
            WHERE type = 'Expense' 
            GROUP BY month 
            ORDER BY month
        """, conn)
        conn.close()

        if df.empty:
            print("⚠️ No data available. Please add expenses in your console app first.")
            return pd.DataFrame()

        df['month_num'] = range(1, len(df) + 1)
        df.rename(columns={'total': 'amount'}, inplace=True)
        return df

    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return pd.DataFrame()

# Train linear regression model on month_num vs amount
def train_model(df):
    X = df[['month_num']]
    y = df['amount']
    model = LinearRegression()
    model.fit(X, y)
    return model

# Predict next month's expense based on the trained model
def predict_next(model, last_month):
    next_month_num = last_month + 1
    prediction = model.predict([[next_month_num]])
    return prediction[0]
