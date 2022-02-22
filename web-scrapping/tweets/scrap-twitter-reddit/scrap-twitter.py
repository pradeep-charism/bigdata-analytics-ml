import pandas as pd
import snscrape.modules.twitter as sntwitter

maxTweets = 1000

# Creating list to append tweet data to
tweets = []

keywords = ['$TSLA', '$AMZN']
start = '2022-02-01'
end = '2022-02-02'

for keyword in keywords:
    query = f'{keyword} since:{start} until:{end} lang:en'
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i > maxTweets:
            break
        content = [keyword, tweet.content,
                   tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount,
                   tweet.retweetedTweet, tweet.quotedTweet, tweet.mentionedUsers]
        tweets.append(content)

# Creating a dataframe from the tweets list above
columns = ['Ticker', 'Text', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount',
           'retweetedTweet', 'quotedTweet', 'mentionedUsers']

tweets_df2 = pd.DataFrame(tweets, columns=columns)

# Display first 5 entries from dataframe
print(tweets_df2.shape)

tweets_df3 = tweets_df2.drop_duplicates(subset='Text', keep="last")
# print(tweets_df3.shape)
# tweets_df3.head()
# tweets_df3.Text.head(30)

# Export dataframe into a CSV
tweets_df3.to_csv('data/stock_tweets_simple.csv', sep=',', index=False)
