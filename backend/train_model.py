import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from datetime import datetime

# Download training data (using a stable stock like SPY)
ticker = 'SPY'
now = datetime.now()
start = datetime(now.year-20, now.month, now.day)
end = now

print(f"Downloading {ticker} data...")
df = yf.download(ticker, start, end)
df = df.reset_index()

# Prepare data
data_training = pd.DataFrame(df.Close[0:int(len(df)*0.7)])
data_testing = pd.DataFrame(df.Close[int(len(df)*0.7): int(len(df))])

# Scale data
scaler = MinMaxScaler(feature_range=(0,1))
data_training_array = scaler.fit_transform(data_training)

# Prepare training data
x_train = []
y_train = []

for i in range(100, data_training_array.shape[0]):
    x_train.append(data_training_array[i-100: i])
    y_train.append(data_training_array[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)

# Build LSTM model
print("Building model...")
model = Sequential()
model.add(LSTM(units=50, activation='relu', return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=60, activation='relu', return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(units=80, activation='relu', return_sequences=True))
model.add(Dropout(0.4))
model.add(LSTM(units=120, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')

# Train model
print("Training model... (this will take a while)")
model.fit(x_train, y_train, epochs=50, batch_size=32, verbose=1)

# Save model
model.save('stock_prediction_model.keras')
print("Model saved as 'stock_prediction_model.keras'")