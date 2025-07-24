# predictor.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import sqlite3

def load_data():
    conn = sqlite3.connect("expense.db")
    df = pd.read_sql_query("SELECT date, amount FROM transactions WHERE type='Expense'", conn)
    conn.close()
    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(pd.Grouper(key='date', freq='M')).sum().reset_index()
    df['month_num'] = range(1, len(df) + 1)
    return df

def train_model(df):
    model = LinearRegression()
    X = df[['month_num']]
    y = df['amount']
    model.fit(X, y)
    return model, df

def predict_next(model, df):
    next_month = pd.DataFrame({'month_num': [df['month_num'].max() + 1]})
    return model.predict(next_month)[0]
