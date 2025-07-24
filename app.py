import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from predictor import train_model, predict_next
from db_handler import fetch_all_transactions
from ai_suggestion import generate_ai_suggestion

st.title("💸 Smart Expense Predictor & AI Tracker")

# ✅ Load data from database
transactions = fetch_all_transactions()

# Convert to DataFrame
df = pd.DataFrame(transactions, columns=["id", "amount", "category", "date"])

# Fix 1: If no data available, stop the app
if df.empty:
    st.warning("⚠️ No data available. Please add expenses in your console app first.")
    st.stop()

# ✅ Convert 'date' to datetime and extract month number
df['date'] = pd.to_datetime(df['date'])
df['month_num'] = df['date'].dt.month

# Group by month and sum amounts
monthly_df = df.groupby('month_num')['amount'].sum().reset_index()

# Train model
model = train_model(monthly_df)

# Predict next month's expense
last_month = monthly_df['month_num'].max()
prediction = predict_next(model, last_month)

# Display results
st.subheader("📊 Monthly Expense Chart")
plt.figure(figsize=(10, 5))
plt.plot(monthly_df['month_num'], monthly_df['amount'], marker='o', label="Actual")
plt.plot(last_month + 1, prediction, marker='x', markersize=10, color='red', label="Predicted")
plt.xlabel("Month Number")
plt.ylabel("Amount (₹)")
plt.title("Monthly Expenses with Prediction")
plt.legend()
st.pyplot(plt)

st.success(f"🧮 Predicted Expense for Month {last_month + 1}: ₹{prediction:.2f}")

# Fix 2: AI Suggestion
st.subheader("🤖 AI Spending Insight")
ai_message = generate_ai_suggestion(transactions)
st.markdown(ai_message)
