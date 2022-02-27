import re

import pandas as pd
import snscrape.modules.twitter as sntwitter

maxTweets = 1000
tweets = []

keywords = ['TSLA', 'NVDA']
start = '2022-02-01'
end = '2022-02-02'


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
    query = f'${keyword} since:{start} until:{end} lang:en'
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i > maxTweets:
            break
        totalMentions = 0
        if tweet.mentionedUsers is not None:
            totalMentions = len(tweet.mentionedUsers)

        content = [keyword, clean_text(tweet.content),
                   tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount,
                   totalMentions]
        tweets.append(content)

# Creating a dataframe from the tweets list above
columns = ['Ticker', 'Text', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'mentionedUsers']

tweets_df2 = pd.DataFrame(tweets, columns=columns)
tweets_df3 = tweets_df2.drop_duplicates(subset='Text', keep="last")
tweets_df3.to_csv('data/stock_tweets_simple.csv', sep=',', index=False)
