import requests # Needed for financialmodelingprep.com API
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt


symbol = "AAPL"
from_date = "2022-01-01"
to_date = "2023-08-01"
url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?from={from_date}&to={to_date}&apikey={"ZOt7h0Ycts8CwWV1YvbdNCJEBr0KUO2v"}"
def fetch_data(url):
    response = requests.get(url).json()
    return response


def preprocess_data(data):
    df = pd.DataFrame(data["historical"])
    df.reset_index(inplace=True)
    df.rename(columns={'date': 'ds', 'close': 'y'}, inplace=True)
    return df

def train_prophet_model(data):
    model = Prophet(
        changepoint_prior_scale=0.05,
        holidays_prior_scale=15,
        seasonality_prior_scale=10,
        weekly_seasonality=True,
        yearly_seasonality=True,
        daily_seasonality=False
    )
    model.add_country_holidays(country_name='US')
    model.fit(data)
    return model

# periods = how far the dataframe extends into the future
def generate_forecast(model, periods=365):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

data = fetch_data(url)
df = preprocess_data(data)
model = train_prophet_model(df)
forecast = generate_forecast(model)
model.plot(forecast)
plt.show()