# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from predictor import load_data, train_model, predict_next

st.title("📈 Expense Tracker ML Predictor")

df = load_data()
st.write("### Monthly Expense Summary")
st.dataframe(df[['date', 'amount']])

model, df = train_model(df)
prediction = predict_next(model, df)
st.write(f"**Predicted next month expense:** ₹{prediction:.2f}")

plt.figure(figsize=(8,4))
plt.plot(df['date'], df['amount'], marker='o', label='Actual')
plt.plot(df['date'].iloc[-1] + pd.offsets.MonthBegin(), prediction, 'ro', label='Predicted')
plt.legend()
plt.xlabel("Date")
plt.ylabel("Amount")
plt.title("Expense Prediction")
st.pyplot(plt)
