import matplotlib.pyplot as plt
import pandas as pd

dataset_file = "datasets/stock_data.csv"


def load_data():
    data = pd.read_csv(dataset_file)
    # print(data)
    return data


df = load_data()

plt.figure(figsize=(10, 5))
top = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4)
bottom = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=4)
top.plot(df.index, df['Adj Close'])
bottom.bar(df.index, df['Volume'])

# set the labels
top.axes.get_xaxis().set_visible(False)
top.set_title('CapitalMall Trust')
top.set_ylabel('Adj Closing Price')
bottom.set_ylabel('Volume')

# simple moving averages
sma10 = df['Close'].rolling(10).mean()  # 10 days
sma20 = df['Close'].rolling(20).mean()  # 20 days
sma50 = df['Close'].rolling(50).mean()  # 50 days

sma = pd.DataFrame({'CMT': df['Close'], 'SMA 10': sma10, 'SMA 20': sma20, 'SMA 50': sma50})
sma.plot(figsize=(10, 5), legend=True, title='Apple')
plt.show()
