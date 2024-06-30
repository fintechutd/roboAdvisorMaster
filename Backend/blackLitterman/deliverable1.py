import yfinance as yf
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from collections import defaultdict
from sklearn.preprocessing import MinMaxScaler
from tabulate import tabulate
import warnings
import os

# Clear console method and suppress future warnings
warnings.filterwarnings("ignore", category=FutureWarning)
def clear_console():
    os.system('clear') # 'cls' for windows

# Get dictionary {sector: [tickers]}
def get_sp500_sectors():
    tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0][['Symbol', 'GICS Sector']]
    tickers['Symbol'] = tickers['Symbol'].str.replace('.', '-')

    sector_breakdown = tickers.groupby('GICS Sector')['Symbol'].apply(list)
    sector_breakdown = sector_breakdown.to_dict()

    return sector_breakdown

sp500_sectors = get_sp500_sectors()

# Get data for each sector
def download_sector_data(period='5y'):
    sector_data = {}
    for sector, tickers in sp500_sectors.items():
        data = yf.download(tickers, progress=False, period=period, group_by='ticker')
        # data = data.drop(columns=['Open', 'High', 'Low', 'Volume'])
        sector_data[sector] = data
        print(f"{sector} data downloaded")
    return sector_data

# Aggregates data - returns two DataFrames: one is normalized (for graph) and one is NOT normalized (for calculations)
def aggregate_data(df):
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(df)
    normalized_df = pd.DataFrame(normalized_data, index=df.index, columns=df.columns)

    # mean_normalized_df = pd.DataFrame(index=df.index, columns=['Close', 'Adj Close'])
    # mean_unnormalized_df = pd.DataFrame(index=df.index, columns=['Close', 'Adj Close'])

    mean_normalized_df = pd.DataFrame(index=df.index, columns=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
    mean_unnormalized_df = pd.DataFrame(index=df.index, columns=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])

    for metric in ['Close', 'Adj Close']:
        # Aggregate normalized data
        metric_cols = [(ticker, metric) for ticker in normalized_df.columns.levels[0]]
        mean_values = normalized_df[metric_cols].mean(axis=1)
        mean_normalized_df[metric] = mean_values

        # Aggregate unnormalized data
        metric_cols = [(ticker, metric) for ticker in df.columns.levels[0]]
        mean_values = df[metric_cols].mean(axis=1)
        mean_unnormalized_df[metric] = mean_values

    return mean_normalized_df, mean_unnormalized_df

# Calculate portfolio return, risk, and Sharpe ratio
def calculate_results(data):
    # Portfolio returns
    start_price = data['Close'].iloc[0]
    end_price = data['Close'].iloc[-1]
    portfolio_return = (end_price - start_price) / start_price * 100

    # Risk
    risk = data['Adj Close'].std()
    risk_free_rate = 0.012 # 5 year treasury rate - current inflation rate = 4.29% - 3.09% = 1.2%

    # Sharpe ratio
    sharpe_ratio = (portfolio_return - risk_free_rate) / risk

    return portfolio_return, risk, sharpe_ratio

sector_data = download_sector_data()

# Aggregate all sector data
normalized_sector_data = {}
unnormalized_sector_data = {}
for sector, data in sector_data.items():
    normalized, unnormalized = aggregate_data(data)
    normalized_sector_data[sector] = normalized
    unnormalized_sector_data[sector] = unnormalized

# Plot formatting
sb.set_style("darkgrid")
plt.figure(figsize=(10, 6))
for sector, data in normalized_sector_data.items():
    sb.lineplot(data=data['Close'], linewidth=1.5, label=sector)
plt.title('Sector Performance Over the Past Year')
plt.xlabel('Date')
plt.ylabel('Close Price (normalized)')
plt.legend()
plt.tight_layout()

# Tabulate calculations
table_data = []
for sector, data in unnormalized_sector_data.items():
    portfolio_return, risk, sharpe_ratio = calculate_results(data)
    table_data.append([sector, f'{portfolio_return:.2f}%', f'{risk:.2f}', f'{sharpe_ratio:.2f}'])

headers = ['SECTOR', 'PORTFOLIO RETURN', 'RISK', 'SHARPE RATIO']
clear_console()

# Calculate covariance matrix with adjusted close price
adj_close_list = [data['Adj Close'] for sector, data in normalized_sector_data.items()]
adj_close_df = pd.concat(adj_close_list, axis=1)
adj_close_df.columns = normalized_sector_data.keys()
cov_matrix = adj_close_df.cov()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)

# Print calculations and covariance matrix
print(tabulate(table_data, headers=headers, tablefmt='fancy_grid'))
print("\nCovariance Matrix:")
print(cov_matrix.to_string())

# Show plot
plt.show()