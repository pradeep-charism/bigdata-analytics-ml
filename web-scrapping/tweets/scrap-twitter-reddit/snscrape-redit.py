import snscrape.modules.reddit as snreddit

maxTweets = 5

# Creating list to append tweet data to
results = []

keywords = ['wallstreetbets']
start = '2022-03-13'
end = '2022-03-13'

for keyword in keywords:
    query = f'{keyword} before:{start} after:{end}'
    # query = f'{keyword}'
    scraper = snreddit.RedditSubredditScraper(query)

    for i, tweet in enumerate(scraper.get_items()):
        if i > maxTweets:
            break
        results.append(tweet.body)
        print(tweet.created.date())

print(results)

# content = pd.DataFrame(results, columns=['content'])

# content.to_csv('data/reddit_raw.csv', sep=',', index=False)
