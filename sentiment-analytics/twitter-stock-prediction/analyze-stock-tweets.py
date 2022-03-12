from datetime import datetime

import pandas as pd
import plotly.express as px
import yfinance as yf
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def load_data():
    data = pd.read_csv('data/stock_tweets_simple.csv')
    return data


def getSentiment(df, measurement="compound"):
    """
    Given a DF of tweets, analyzes the tweets and returns a new DF
    of sentiment scores based on the given measurement.
    Accepted sentiment measurements: ["pos", "neg", "neu", "compound"]
    """

    # Sentiment Analyzer
    sia = SentimentIntensityAnalyzer()

    # Getting the sentiment score
    df['sentiment'] = df['Text'].apply(lambda x: sia.polarity_scores(x)[measurement])

    # Creating a DF with the average sentiment score each day
    sent_df = df.groupby('Date')['sentiment'].mean().reset_index()

    # Converting the dates to datetime
    sent_df['Date'] = sent_df['Date'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))

    return sent_df


def getStockPrices(ticker, start, end):
    """
    Gets the historical daily prices between two dates. Scaling the prices based on a
    given sentiment dataframe.
    """
    # Setting the stock
    stock = yf.Ticker(ticker)

    # Getting historical prices
    stock_df = stock.history(start=start, end=end, interval="1d")[['Close']]

    # Getting the daily percent returns
    stock_df = stock_df.pct_change(1).dropna()

    # Some reformatting
    stock_df = stock_df.reset_index().rename(
        columns={
            "Date": "Date",
            "Close": "returns"
        }
    )

    return stock_df


df = load_data()
print(df.head())

sent_df = getSentiment(df)
print(sent_df)


fig = px.bar(sent_df,
             x=sent_df['Date'],
             y=sent_df['sentiment'],
             title="Sentiment Score over Time")

fig.show()


stock_df = getStockPrices(
    "TSLA",
    "2022-02-02",
    "2022-02-10"
)

print(stock_df)

fig = px.bar(stock_df,
             x=stock_df['Date'],
             y=stock_df['returns'],
             title="Stock % Returns over Time")

fig.show()

# Merging the two DF
comb_df = sent_df.merge(stock_df, how='outer', sort=True)

# Shifting the sentiment scores 1 day to compensate for lookahead bias
comb_df['sentiment'] = comb_df['sentiment'].shift(1)

# Scaling the data
# scaler = MinMaxScaler(
#     feature_range=(
#         comb_df['sentiment'].min(), comb_df['sentiment'].max()
#     )
# )

# comb_df[['returns']] = scaler.fit_transform(comb_df[['returns']])

# How often sentiment matched return

# Dropping NAs so they are not compared
drop_df = comb_df.dropna()

# Comparing matches
match = (drop_df['sentiment'].apply(lambda x: x>0)==drop_df['returns'].apply(lambda x: x>0))

# Counting instances where they match
match = match.value_counts().rename({False: "Didn't predict return",
                                     True: "Successfully predicted return"}).to_frame()

print(match)

print(comb_df)

fig = px.bar(
    comb_df,
    x='Date',
    y=['returns', 'sentiment'],
    barmode='group',
    title="Returns & Sentiment over Time",
    labels={"value": "Return & Sentiment Values"}
)

fig.show()


fig = px.bar(
    match,
    x=0,
    y=match.index,
    color=match.index,
    title="Instances when Sentiment predicts Return",
    labels={"index": "Prediction",
            "0": "Count"}
)

fig.show()

