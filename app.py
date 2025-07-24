import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from predictor import load_data, train_model, predict_next
from db_handler import fetch_all_transactions
from ai_suggestion import generate_ai_suggestion

st.title("💸 Smart Expense Predictor & AI Tracker")

# Load and process data
df = load_data()

# Fix 1: If no data available, stop the app
if df.empty:
    st.warning("⚠️ No data available. Please add expenses in your console app first.")
    st.stop()

# Train model
model = train_model(df)

# Predict next month's expense
last_month = df['month_num'].iloc[-1]
prediction = predict_next(model, last_month)

# Display results
st.subheader("📊 Monthly Expense Chart")
plt.figure(figsize=(10, 5))
plt.plot(df['month_num'], df['amount'], marker='o', label="Actual")
plt.plot(last_month + 1, prediction, marker='x', markersize=10, color='red', label="Predicted")
plt.xlabel("Month Number")
plt.ylabel("Amount (₹)")
plt.title("Monthly Expenses with Prediction")
plt.legend()
st.pyplot(plt)

st.success(f"🧮 Predicted Expense for Month {last_month + 1}: ₹{prediction:.2f}")

# Fix 2: Optional AI Suggestion (based on db)
st.subheader("🤖 AI Spending Insight")
transactions = fetch_all_transactions()
ai_message = generate_ai_suggestion(transactions)
st.markdown(ai_message)
