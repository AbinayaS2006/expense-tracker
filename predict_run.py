from predictor import load_data, train_model, predict_next

df = load_data()
if not df.empty:
    model = train_model(df)
    prediction = predict_next(model, df['month_num'].max())
    print(f"📈 Predicted expense for next month: ₹{prediction:.2f}")
