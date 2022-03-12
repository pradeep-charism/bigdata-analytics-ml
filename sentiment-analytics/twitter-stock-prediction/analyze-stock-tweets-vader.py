from datetime import datetime

import pandas as pd
import plotly.express as px
import yfinance as yf
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def load_data():
    data = pd.read_csv('data/stock_tweets_simple.csv')
    return data


def get_sentiment(df_senti, measurement="compound"):
    """
    Given a DF of tweets, analyzes the tweets and returns a new DF
    of sentiment scores based on the given measurement.
    Accepted sentiment measurements: ["pos", "neg", "neu", "compound"]
    """

    # Sentiment Analyzer
    sia = SentimentIntensityAnalyzer()

    # Getting the sentiment score
    df_senti['sentiment'] = df_senti['Text'].apply(lambda x: sia.polarity_scores(x)[measurement])

    # Creating a DF with the average sentiment score each day
    sent_df = df_senti.groupby('Date')['sentiment'].mean().reset_index()

    # Converting the dates to datetime
    sent_df['Date'] = sent_df['Date'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))

    return sent_df


def get_stock_prices(ticker, start, end):
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


def show_sentiment_chart(df_senti):
    global fig
    fig = px.bar(df_senti,
                 x=df_senti['Date'],
                 y=df_senti['sentiment'],
                 title="Sentiment Score over Time")
    fig.show()


def show_stock_returns_chart(df_stock_returns):
    global fig
    fig = px.bar(df_stock_returns,
                 x=df_stock_returns['Date'],
                 y=df_stock_returns['returns'],
                 title="Stock % Returns over Time")
    fig.show()


def show_sentiment_stock_price_combined_charts(df_combined):
    global fig
    print(df_combined)
    fig = px.bar(
        df_combined,
        x='Date',
        y=['returns', 'sentiment'],
        barmode='group',
        title="Returns & Sentiment over Time",
        labels={"value": "Return & Sentiment Values"}
    )
    fig.show()


def show_prediction_accuracy_charts(df_accuracy):
    global fig
    print(df_accuracy)
    fig = px.bar(
        df_accuracy,
        x=0,
        y=df_accuracy.index,
        color=df_accuracy.index,
        title="Instances when Sentiment predicts Return",
        labels={"index": "Prediction",
                "0": "Count"}
    )
    fig.show()


# Load the stock data from  file
df_stock_data = load_data()

# Build the sentiment analytics data frame
df_sentiment = get_sentiment(df_stock_data)
print(df_sentiment)

# Retrieve the stock prices from Yahoo finance
df_stock_daily_prices = get_stock_prices("TSLA", "2022-02-02", "2022-02-10")
print(df_stock_daily_prices)

# Merge the two sentiment and stock prices data frames
df_combined_sentiment_stock_price = df_sentiment.merge(df_stock_daily_prices, how='outer', sort=True)

# Shifting the sentiment scores 1 day to compensate for lookahead bias
df_combined_sentiment_stock_price['sentiment'] = df_combined_sentiment_stock_price['sentiment'].shift(1)

# Dropping NAs so they are not compared
drop_df = df_combined_sentiment_stock_price.dropna()

# Launch the sentiment vs stock price comparison charts
show_sentiment_stock_price_combined_charts(df_combined_sentiment_stock_price)

# Comparing matches
match_for_accuracy = (drop_df['sentiment'].apply(lambda x: x > 0) == drop_df['returns'].apply(lambda x: x > 0))

# Counting instances where they match
match_for_accuracy = match_for_accuracy.value_counts().rename({False: "Didn't predict return",
                                                               True: "Successfully predicted return"}).to_frame()

show_prediction_accuracy_charts(match_for_accuracy)
