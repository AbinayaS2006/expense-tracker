import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data from CSV and add 'month_num' for model
def load_data(file_path):
    df = pd.read_csv(file_path)
    
    # Check if 'month' and 'total' columns exist
    if 'month' not in df.columns or 'total' not in df.columns:
        raise ValueError("CSV must contain 'month' and 'total' columns")

    # Convert month name (e.g., "January") to month number (1–12)
    df['month_num'] = df['month'].apply(lambda m: pd.to_datetime(m, format='%B').month)
    return df

# Train a linear regression model on month_num vs total expense
def train_model(df):
    X = df[['month_num']]
    y = df['total']
    model = LinearRegression()
    model.fit(X, y)
    return model

# Predict next month's expense based on the model
def predict_next(model, df):
    if 'month' not in df.columns:
        raise ValueError("The input DataFrame must contain a 'month' column.")

    # Ensure 'month_num' exists
    df['month_num'] = df['month'].apply(lambda m: pd.to_datetime(m, format='%B').month)

    X = df[['month_num']]
    prediction = model.predict(X)
    
    return prediction[-1]  # Return the prediction for the latest month
