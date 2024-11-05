import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def lstm_model(df):
    # Ensure Date column is set as the index and convert it to datetime if it isn't already
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)

    # Step 1: Scaling only the numeric data
    df_numeric = df.select_dtypes(include=[np.number])  # Select only numeric columns
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df_numeric)

    # Step 2: Creating sequences for LSTM model
    sequence_length = 60  # using the last 60 time steps for prediction
    X, y = [], []

    for i in range(sequence_length, len(scaled_data)):
        X.append(scaled_data[i-sequence_length:i])  # sequence of 60 time steps
        y.append(scaled_data[i, 0])  # predicting 'Price_Returns' (first column)

    X, y = np.array(X), np.array(y)
    
    # Step 3: Splitting data into training and testing sets
    split_index = int(len(X) * 0.8)  # 80% training, 20% testing
    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]

    # Step 4: Defining the LSTM model
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])),
        LSTM(50),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    # Step 5: Training the LSTM model
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

    # Step 6: Making predictions
    predictions = model.predict(X_test)

    # Step 7: Inverse scale the predictions to get them back to original scale
    predictions_extended = np.zeros((predictions.shape[0], scaled_data.shape[1]))
    predictions_extended[:, 0] = predictions[:, 0]
    predictions = scaler.inverse_transform(predictions_extended)[:, 0]  # Get the 'Price_Returns' back

    # Step 8: Returning predictions and actuals for evaluation
    actuals = scaler.inverse_transform(scaled_data[split_index + sequence_length:])[:, 0]
    evaluate_model(y_test, predictions)
    return predictions, actuals , model
def evaluate_model(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"The Mean squared Error {mse}")
    print(f"mean absolute error {mae}")
    print(f"r2: {r2}")
    return mse, mae, r2
