import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf

pfizer = yf.Ticker('TSLA')

old = pfizer.history(start="2022-01-01", end="2022-04-21")
old["Date"] = old.index
print(old.head())

print(pfizer.actions)

print(pfizer.sustainability)

print(pfizer.recommendations)

print(pfizer.calendar)


exit(0)
fig = px.line(old, x="Date", y="Open", title='PFizer Stock Prices')
fig.show()

fig = go.Figure(data=go.Ohlc(x=old['Date'],
                             open=old['Open'],
                             high=old['High'],
                             low=old['Low'],
                             close=old['Close']))
fig.show()

old = old.reset_index()
for i in ['Open', 'High', 'Close', 'Low']:
    old[i] = old[i].astype('float64')

fig = go.Figure(data=[go.Candlestick(x=old['Date'],
                                     open=old['Open'],
                                     high=old['High'],
                                     low=old['Low'],
                                     close=old['Close'])])
fig.show()
