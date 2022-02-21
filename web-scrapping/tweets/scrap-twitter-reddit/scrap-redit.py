import pandas as pd
import snscrape.modules.twitter as sntwitter
import snscrape.modules.reddit as snreddit
maxTweets = 1000

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
# query = '$TSLA since:2022-01-01 until:2022-02-01 near:Singapore lang:en'
snreddit
query = '$TSLA since:2022-02-01 until:2022-02-02 lang:en'


for i, tweet in enumerate(snreddit.RedditSearchScraper(query).get_items()):
    if i > maxTweets:
        break
    tweets_list2.append(
        [tweet.date, tweet.url, tweet.id, tweet.user.id, tweet.content, tweet.user.username, tweet.user.location,
         tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.lang, tweet.retweetedTweet,
         tweet.quotedTweet, tweet.mentionedUsers])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2,
                          columns=['Datetime', 'Tweet URL', 'Tweet Id', 'Tweet User Id', 'Text', 'Username',
                                   'User Location', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'language',
                                   'retweetedTweet', 'quotedTweet', 'mentionedUsers'])

# Display first 5 entries from dataframe
tweets_df2.shape

tweets_df3 = tweets_df2.drop_duplicates(subset='Text', keep="last")

print(tweets_df3.shape)
tweets_df3.head()

tweets_df3.Text.head(30)

# Export dataframe into a CSV
tweets_df3.to_csv('data/tweets_raw.csv', sep=',', index=False)
