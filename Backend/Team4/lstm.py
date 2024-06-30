import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout, LeakyReLU
from keras.callbacks import EarlyStopping
from keras import regularizers
import yfinance as yf
from data import download_sector_data
import os

class SectorLSTM:
    def __init__(self, data, train_sector, name='lstm_model', train_size=0.8, n_steps=180, n_features=1):
        self.data = data # data is already normalized
        self.train_sector = train_sector # which sector data the model is trained on
        self.name = name # name of model to save
        self.train_size = train_size # train size
        self.n_steps = n_steps # how many previous data points (in our case, days) the model uses to predict next data point
        self.n_features = n_features # we're only doing 1 feature

    # prepare data for LSTM
    def _preprocess_data(self):
        X, y = [], []
        for i in range(len(self.data) - self.n_steps):
            X.append(self.data[i:i + self.n_steps])
            y.append(self.data[i + self.n_steps])

        X, y = np.array(X), np.array(y)
        self.X_train, self.X_test = X[:int(len(X) * self.train_size)], X[int(len(X) * self.train_size):]
        self.y_train, self.y_test = y[:int(len(y) * self.train_size)], y[int(len(y) * self.train_size):]

    # build model
    def build_model(self, units=32, dropout=0.2, num_layers=2):
        self._preprocess_data()

        self.model = Sequential([
            LSTM(units=64, activation='relu', kernel_regularizer=regularizers.l2(0.01), return_sequences=True, input_shape=(self.X_train.shape[1], 1)),
            Dropout(0.2),
            LSTM(units=64, activation='relu', kernel_regularizer=regularizers.l2(0.01), return_sequences=True),
            Dropout(0.2),
            LSTM(units=32, activation='relu', kernel_regularizer=regularizers.l2(0.01), return_sequences=True),
            Dropout(0.2),
            LSTM(units=32, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
            Dropout(0.2),
            Dense(units=1, kernel_regularizer=regularizers.l2(0.01))
        ])
        
        self.model.compile(optimizer='adam', loss='mean_squared_error')

    # train model
    def train_model(self, epochs=100, batch_size=32):
        # early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
        # self.history = self.model.fit(self.X_train, self.y_train, epochs=epochs, batch_size=batch_size, validation_split=0.1, verbose=1, callbacks=[early_stopping])
        
        self.history = self.model.fit(self.X_train, self.y_train, epochs=epochs, batch_size=batch_size, validation_split=0.1, verbose=1)
        
        self.model.save(f'models/{self.name}.keras') # save model

    # plot training results
    def plot_training_results(self):
        train_predictions = self.model.predict(self.X_train)
        test_predictions = self.model.predict(self.X_test)

        scaler = MinMaxScaler()
        scaler.fit_transform(self.data.reshape(-1, 1))
        train_predictions = scaler.inverse_transform(train_predictions)
        test_predictions = scaler.inverse_transform(test_predictions)

        folder_name = f'results/training'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        plt.figure(figsize=(14, 7))
        plt.plot(self.data, label='Actual Data')
        plt.plot(np.arange(self.n_steps, len(train_predictions) + self.n_steps), train_predictions, label='Train Predictions')
        plt.plot(np.arange(len(train_predictions) + 2*self.n_steps, len(train_predictions) + 2*self.n_steps + len(test_predictions)), test_predictions, label='Test Predictions')
        plt.xlabel('Time')
        plt.ylabel('Price (normalized)')
        plt.title('LSTM Training')
        plt.legend()
        
        # plt.show()
        plt.savefig(f'{folder_name}/training_results.png')
        plt.close()

# prepare data for predictions
def prepare_test_data(data, n_steps=180, n_features=1):
    X, y = [], []
    for i in range(len(data) - n_steps):
        X.append(data[i:i + n_steps])
        y.append(data[i + n_steps])
    X_test, y_test = np.array(X), np.array(y)
    X_test = np.reshape(X_test, (X_test.shape[0], n_steps, n_features))
    return X_test, y_test

# save testing results as .png
def plot_test_results(X_test, y_test, loaded_model, train_sector, test_sector):
        # use loaded model for predictions
        predictions = loaded_model.predict(X_test)
        mse = mean_squared_error(y_test, predictions) # mean squared error metric

        # make folder in results if it doesnt exist
        folder_name = f'results/test'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        plt.figure(figsize=(14, 7))
        plt.plot(y_test, label='Actual Data')
        plt.plot(predictions, label='Predictions')
        plt.xlabel('Time')
        plt.ylabel('Price (normalized)')
        plt.title(f'LSTM Predictions for {test_sector} | MSE = {mse}')
        plt.legend()
        
        # plt.show()
        plt.savefig(f'{folder_name}/{test_sector}.png')
        plt.close()

def plot_future_results(data, loaded_model, train_sector, test_sector, n_days=365, n_steps=180, n_features=1):
    input_data = data[-n_steps:]
    input_data = np.reshape(input_data, (1, n_steps, n_features))

    predictions = []
    for _ in range(n_days):
        # Predict the next day's stock price
        prediction = loaded_model.predict(input_data)
        # Append the prediction to the list of predictions
        predictions.append(prediction[0, 0])
        # Update input data by removing the first data point and adding the predicted data point
        input_data = np.append(input_data[:, 1:, :], np.reshape(prediction, (1, 1, 1)), axis=1)

        # make folder in results if it doesnt exist
        folder_name = f'results/future/'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        plt.figure(figsize=(14, 7))
        plt.plot(predictions, label='Predictions')
        plt.xlabel('Time')
        plt.ylabel('Price (normalized)')
        plt.title(f'Future Predictions for {test_sector}')
        plt.legend()
        # plt.show()
        plt.savefig(f'{folder_name}/{test_sector}.png')
        plt.close()

def main():
    # get data
    sector_data = download_sector_data()

    train_sector = 'Information Technology'

    # name of model
    model_name = f'lstm_model_IT'
    
    # if not os.path.exists(f'models/{model_name}.keras'): # if model does not exist, train model
    #     training_data = sector_data[train_sector].values
    #     lstm_model = SectorLSTM(data=training_data, name=model_name)
    #     lstm_model.build_model()
    #     print("Model built")
    #     lstm_model.train_model()
    #     lstm_model.plot_training_results()

    # else: # if model exists, load model and plot results
    #     lstm_model = load_model(f'models/{model_name}.keras')

    #     # plot results
    #     for test_sector, data in sector_data.items():
    #         if test_sector != train_sector:
    #             # backtesting
    #             test_data = data.values
    #             X_test, y_test = prepare_test_data(test_data)
    #             plot_test_results(X_test, y_test, lstm_model, train_sector, test_sector)

    #             # predict next month
    #             input_data = data
    #             plot_future_results(input_data, lstm_model, train_sector, test_sector)

    # temporary code to train and plot predictions in one run. above commented code trains and predicts in different runs based on whether model exists or not
    training_data = sector_data[train_sector].values
    lstm_model = SectorLSTM(data=training_data, train_sector=train_sector, name=model_name)
    lstm_model.build_model()
    print("Model built")
    lstm_model.train_model()
    lstm_model.plot_training_results()

    lstm_model = load_model(f'models/{model_name}.keras')

    # plot results
    for test_sector, data in sector_data.items():
        if test_sector != train_sector:
            # backtesting
            test_data = data.values
            X_test, y_test = prepare_test_data(test_data)
            plot_test_results(X_test, y_test, lstm_model, train_sector, test_sector)

            # predict next month
            input_data = data
            plot_future_results(input_data, lstm_model, train_sector, test_sector)

if __name__ == "__main__":
    main()