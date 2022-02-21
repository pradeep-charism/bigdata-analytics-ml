import pandas as pd
import snscrape.modules.reddit as snreddit

maxTweets = 2

# Creating list to append tweet data to
results = []

keywords = ['wallstreetbets']
start = '2022-02-01'
end = '2022-02-02'

for keyword in keywords:
    # query = f'{keyword} since:{start} until:{end}'
    query = f'{keyword}'
    for i, tweet in enumerate(snreddit.RedditSubredditScraper(query).get_items()):
        if i > maxTweets:
            break
        results.append(tweet.body)

content = pd.DataFrame(results, columns=['content'])

content.to_csv('data/reddit_raw.csv', sep=',', index=False)
