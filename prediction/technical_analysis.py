# pip install ta
# pip install pandas_ta

import pandas as pd
import yahoo_fin.stock_info as si
from ta import add_all_ta_features
from ta.momentum import RSIIndicator
from ta.trend import macd

ticker = 'TSLA'


def macd_rsi():
    # pull data from Yahoo Finance
    data = si.get_data("aapl")
    # add technical analysis features
    data = add_all_ta_features(data, open="open", high="high", low="low", close="adjclose", volume="volume")
    # print(data)
    rsi_21 = RSIIndicator(close=data.adjclose, window=21)
    data["rsi_21"] = rsi_21.rsi()
    data["macd"] = macd(data.adjclose, window_slow=26, window_fast=12)
    print(data)


def pe_ta():
    global ticker, combined_stats
    # https://algotrading101.com/learn/yahoo-finance-api-guide/
    # get_data(ticker, start_date=None, end_date=None, index_as_date=True, interval="1d")
    # amazon_weekly = get_data(ticker, start_date="2022-02-02", end_date="2022-04-20", index_as_date=True, interval="1wk")
    # print(amazon_weekly)
    quote_table = si.get_quote_table(ticker, dict_result=False)
    print(quote_table)
    stats = si.get_stats_valuation(ticker)
    print(f"\n Stats:{stats}")
    # Divident
    # quote_table = si.get_quote_table("aapl")
    # quote_table["Forward Dividend & Yield"]
    # print(quote_table)
    cash_flow_statement = si.get_cash_flow(ticker)
    print(cash_flow_statement)
    exit(1)
    # get list of Dow tickers
    dow_list = si.tickers_nasdaq()
    dow_stats = {}
    for ticker in dow_list:
        try:
            temp = si.get_stats_valuation(ticker)
            cash_flow_statement = si.get_cash_flow(ticker)
            print(cash_flow_statement)

            if temp['Market Cap (intraday)'] > '1B':
                print(temp)
            # temp = temp.iloc[:, :2]
            # temp.columns = ["Attribute", "Recent"]
            # dow_stats[ticker] = temp
        except Exception as ex:
            print(ex)
    # dow_stats
    exit(1)
    combined_stats = pd.concat(dow_stats)
    combined_stats = combined_stats.reset_index()
    del combined_stats["level_1"]
    # update column names
    combined_stats.columns = ["Ticker", "Attribute", "Recent"]
    print(combined_stats)
    pe_ratios = combined_stats[combined_stats["Attribute"] == "Trailing P/E"].reset_index()
    print(pe_ratios)
    pe_ratios_sorted = pe_ratios.sort_values('Recent', ascending=False)
    print(pe_ratios_sorted)


# pe_ta()

macd_rsi()
