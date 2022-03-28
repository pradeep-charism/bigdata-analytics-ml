# For time stamps
from datetime import datetime

import pandas_datareader.data as data_reader

# List to hold the tickers
tickers = ['AAPL']

# Create a directory 'datasets' and the stock data will be downloaded inside this folder
data_file = 'datasets/stock_data.csv'

# Set up End and Start times for data grab
tickers = ['AAPL']

end = datetime.now()
start = datetime(end.year, end.month - 1, end.day)


def download():
    for stock in tickers:
        download_df = data_reader.DataReader(stock, 'yahoo', start, end)
        download_df["Ticker"] = stock
        print(download_df)
        return download_df


df_downloaded_stock_data = download()
# df_downloaded_stock_data.to_csv(data_file, sep=',', index=False)

# print(df_downloaded_stock_data)
