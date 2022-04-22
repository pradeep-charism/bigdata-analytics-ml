# pip install cufflinks
import cufflinks as cf
import plotly
from pandas_datareader import data as web

# cf.set_config_file(theme='pearl', sharing='public', offline=False)


setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)
cf.set_config_file(offline=True)
# cf.go_offline()

# Get the data from remote source
data = web.DataReader('TSLA', 'stooq')
# Finta likes lowercase
data.columns = ["open", "high", "low", "close", "volume"]

apple_df = data.tail(100)
# print(apple_df)

qf = cf.QuantFig(apple_df, title='Apple Quant Figure', legend='top', name='GS')
qf.add_bollinger_bands()
qf.add_sma([10, 20], width=2, color=['green', 'lightgreen'], legendgroup=True)
qf.add_rsi(periods=20, color='java')
qf.iplot()
