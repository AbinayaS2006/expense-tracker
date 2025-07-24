import pandas as pd
from sklearn.linear_model import LinearRegression

def load_data(filename):
    try:
        df = pd.read_csv(filename)
        df['month_num'] = range(1, len(df) + 1)
        df.rename(columns={'total': 'amount'}, inplace=True)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

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
