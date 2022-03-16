import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")

# For reading stock data from yahoo
import yfinance as yf

# For time stamps
from datetime import datetime

# The tech stocks we'll use for this analysis
tech_list = ['AAPL']
data_file = 'data/stock_data.csv'

# Set up End and Start times for data grab
tech_list = ['AAPL']

end = datetime.now()
start = datetime(end.year, end.month - 1, end.day)

AAPL = ''

for stock in tech_list:
    AAPL = yf.download(stock, start, end)

# print(AAPL.describe)

company_list = [AAPL]
company_name = ["APPLE"]

for company, com_name in zip(company_list, company_name):
    company["company_name"] = com_name

df = pd.concat(company_list, axis=0)
df.tail(10)

df.to_csv(data_file, sep=',', index=False)
