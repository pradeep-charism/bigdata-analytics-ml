import csv

import snscrape.modules.twitter as sntwitter

maxTweets = 100
# , '$NVDA'
keywords = ['$TSLA', '$NVDA']
start = '2022-02-01'
end = '2022-02-02'

columns = ['Ticker', 'Text', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount',
           'retweetedTweet', 'quotedTweet', 'totalMentions']

csvFile = open('data/all_nasdaq_stock_tweets.csv', 'w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(columns)

for keyword in keywords:
    query = f'{keyword} since:{start} until:{end} lang:en'

    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i > maxTweets:
            break
        users = 0
        if tweet.mentionedUsers is not None:
            users = len(tweet.mentionedUsers)

        content = [keyword, tweet.content.encode('utf-8'),
                   tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount,
                   tweet.retweetedTweet, tweet.quotedTweet, users]
        csvWriter.writerow(content)

csvFile.close()
