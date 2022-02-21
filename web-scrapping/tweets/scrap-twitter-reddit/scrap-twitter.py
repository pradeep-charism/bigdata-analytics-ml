import pandas as pd
import snscrape.modules.twitter as sntwitter

maxTweets = 1000

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
# query = '$TSLA since:2022-01-01 until:2022-02-01 near:Singapore lang:en'

keywords = ['$TSLA', '$AMZN']
start = '2022-02-01'
end = '2022-02-02'

for keyword in keywords:
    query = f'{keyword} since:{start} until:{end}'
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i > maxTweets:
            break
        content = [tweet.date, tweet.url, tweet.id, tweet.user.id, tweet.content, tweet.user.username,
                   tweet.user.location,
                   tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.lang,
                   tweet.retweetedTweet,
                   tweet.quotedTweet, tweet.mentionedUsers]
        tweets_list2.append(content)

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2,
                          columns=['Datetime', 'Tweet URL', 'Tweet Id', 'Tweet User Id', 'Text', 'Username',
                                   'User Location', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'language',
                                   'retweetedTweet', 'quotedTweet', 'mentionedUsers'])

# Display first 5 entries from dataframe
print(tweets_df2.shape)

tweets_df3 = tweets_df2.drop_duplicates(subset='Text', keep="last")
print(tweets_df3.shape)

tweets_df3.head()
tweets_df3.Text.head(30)

# Export dataframe into a CSV
tweets_df3.to_csv('data/stock_twits.csv', sep=',', index=False)
