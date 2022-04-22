import matplotlib.pyplot as plt
import talib
import yfinance as yf

# Get symbol OHLC data
data = yf.download("TSLA", start="2022-01-06", end="2022-04-21", interval="1d")

reversed_df = data.iloc[::-1]
data["RSI"] = talib.RSI(reversed_df["Close"], 14)
print(data.head())

ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
ax1.plot(data['Close'], linewidth=2.5)
ax1.grid()

ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)
ax2.plot(data['RSI'], color='red', linewidth=1.5)
ax2.grid()
ax2.axhline(30, linestyle='--', linewidth=1.5, color='grey')
ax2.axhline(70, linestyle='--', linewidth=1.5, color='grey')
ax2.set_title('Bitcoin RSI')

plt.show()
