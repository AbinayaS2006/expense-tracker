import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression

def load_data():
    conn = sqlite3.connect("expense.db")
    try:
        df = pd.read_sql_query("SELECT date, amount FROM transactions WHERE type='Expense'", conn)
    except Exception as e:
        conn.close()
        return pd.DataFrame(columns=['date', 'amount'])

    conn.close()
    if df.empty:
        return pd.DataFrame(columns=['date', 'amount'])

    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(pd.Grouper(key='date', freq='M')).sum().reset_index()
    df['month_num'] = range(1, len(df) + 1)
    return df

def train_model(df):
    X = df[['month_num']]
    y = df['amount']
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_next(model, last_month):
    next_month = [[last_month + 1]]
    prediction = model.predict(next_month)
    return prediction[0]
