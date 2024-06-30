import yfinance as yf
import pandas as pd
import warnings
import os, certifi
from sklearn.preprocessing import MinMaxScaler

os.environ['SSL_CERT_FILE'] = certifi.where()

# Clear console method and suppress future warnings
warnings.filterwarnings("ignore", category=FutureWarning)
def clear_console():
    os.system('clear') # 'cls' for windows

# Returns cumulative returns for each sector (for cov_matrix in BL)
def download_sector_returns(period='10y'):
    tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0][['Symbol', 'GICS Sector']]
    tickers['Symbol'] = tickers['Symbol'].str.replace('.', '-')

    sp500_sectors = tickers.groupby('GICS Sector')['Symbol'].apply(list)
    sp500_sectors = sp500_sectors.to_dict()

    sector_data = {}
    for sector, tickers in sp500_sectors.items():
        data = yf.download(tickers, progress=False, period=period)
        data = data.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume'])

        data = data.fillna(method='bfill', axis=0)
        data = data.fillna(method='ffill', axis=0)

        returns = data.pct_change()
        returns = returns.droplevel(0, axis=1)
        returns = returns.mean(axis=1)

        sector_data[sector] = returns
        print(f"{sector} data downloaded")

    return sector_data

# Returns average sector data (normalized mean adj close) for each sector (for LSTM)
# def download_sector_data(period='10y'): # data time period
#     tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0][['Symbol', 'GICS Sector']]
#     tickers['Symbol'] = tickers['Symbol'].str.replace('.', '-')

#     sp500_sectors = tickers.groupby('GICS Sector')['Symbol'].apply(list)
#     sp500_sectors = sp500_sectors.to_dict()

#     sector_data = {}
#     for sector, tickers in sp500_sectors.items():
#         data = yf.download(tickers, progress=False, period=period)
#         data = data.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume'])

#         data = data.fillna(method='bfill', axis=0)
#         data = data.fillna(method='ffill', axis=0)

#         scaler = MinMaxScaler()
#         normalized_data = pd.DataFrame(scaler.fit_transform(data), data.index)

#         normalized_data = normalized_data.mean(axis=1)
#         sector_data[sector] = normalized_data
#         print(f"{sector} data downloaded")

#     return sector_data

# Returns average sector data (weighted sum overall sector price) for each sector (for LSTM)
def download_sector_data(period='10y'): # data time period
    tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0][['Symbol', 'GICS Sector']]
    tickers['Symbol'] = tickers['Symbol'].str.replace('.', '-')

    sp500_sectors = tickers.groupby('GICS Sector')['Symbol'].apply(list)
    sp500_sectors = sp500_sectors.to_dict()

    sector_data = {}
    for sector, tickers in sp500_sectors.items():
        data = yf.download(tickers, progress=False, period=period)
        data = data.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume'])

        data = data.fillna(method='bfill', axis=0)
        data = data.fillna(method='ffill', axis=0)

        # get market cap and weights based on market cap
        total_market_cap = 0
        market_caps = {}
        for ticker in tickers:
            mc = yf.Ticker(ticker).info['marketCap']
            if mc:
                market_caps[ticker] = mc
                total_market_cap += mc

        weights = {ticker: market_cap / total_market_cap for ticker, market_cap in market_caps.items()}

        weighted_sum = 0
        for ticker, weight in weights.items():
            data['Adj Close'][ticker] = data['Adj Close'][ticker] * weight

        data = data.sum(axis=1)
        sector_data[sector] = data
        print(f"{sector} data downloaded")

    return sector_data