import re
from datetime import datetime
from datetime import timedelta

import pandas as pd
import snscrape.modules.twitter as sntwitter

maxTweets = 100
tweets = []

keywords = ['TSLA']
start = '2022-02-01'
end = '2022-02-04'


def clean_text(text):
    text = re.sub("@[A-Za-z0-9]+", '', text)
    text = re.sub("#[A-Za-z0-9_]+", '', text)
    text = re.sub("https?://S+", '', text)
    text = re.sub(r"http\S+", '', text)
    text = re.sub(r"www.\S+", '', text)
    text = re.sub(r'[.*?]', '', text)
    text = re.sub('[()!?]', '', text)
    text = re.sub("\\d+\\w*\\d*", '', text)
    text = re.sub("[^\x01-\x7F]", '', text)  # remove emotions
    return text


for keyword in keywords:
    for d in pd.date_range(start=start, periods=10, inclusive='right'):
        start_date = pd.to_datetime(d).date().strftime("%Y-%m-%d")
        end_date = (pd.to_datetime(d).date() + timedelta(days=1)).strftime("%Y-%m-%d")
        print('Downloading tweets for Stock: {} from: {} to {}'.format(keyword, start_date, end_date))
        query = f'${keyword} since:{start_date} until:{end_date} lang:en'
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i > maxTweets:
                break
            totalMentions = 0
            if tweet.mentionedUsers is not None:
                totalMentions = len(tweet.mentionedUsers)

            content = [keyword, clean_text(tweet.content), tweet.date,
                       tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount,
                       totalMentions]
            tweets.append(content)

# Creating a dataframe from the tweets list above
columns = ['Ticker', 'Text', 'Date', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'mentionedUsers']

tweets_df2 = pd.DataFrame(tweets, columns=columns)
tweets_df2['Date'] = tweets_df2['Date'].dt.date
tweets_df3 = tweets_df2.drop_duplicates(subset='Text', keep="last")
tweets_df3.to_csv('data/stock_tweets_simple.csv', sep=',', index=False)
