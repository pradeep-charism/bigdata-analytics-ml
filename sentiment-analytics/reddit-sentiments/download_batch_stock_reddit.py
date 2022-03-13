import re
from datetime import datetime

import pandas as pd
import praw

from reddit_keys import client_id, client_secret, user_agent

reddit_read_only = praw.Reddit(client_id=client_id,  # your client id
                               client_secret=client_secret,  # your client secret
                               user_agent=user_agent)

subreddit = reddit_read_only.subreddit("wallstreetbets")
tickers = ['TSLA']
data_file = '../data/single_stock_batch_reddit_data.csv'
download_frequency = 'week'

topics_dict = {
    "Date": [],
    "Text": [],
    "score": [],
    "url": [],
    "comments_num": []
}


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


for ticker in tickers:
    for submission in subreddit.search(ticker, sort='top', time_filter=download_frequency, limit=3):
        score = submission.score
        if score > 10:
            title = clean_text(submission.title)
            body = clean_text(submission.selftext)
            body_content = title + "." + body
            fromtimestamp = datetime.fromtimestamp(submission.created).date()
            topics_dict["Date"].append(fromtimestamp)
            topics_dict["Text"].append(body_content)
            topics_dict["score"].append(score)
            topics_dict["url"].append(submission.url)
            num_comments = submission.num_comments
            topics_dict["comments_num"].append(num_comments)

df_reddit_data = pd.DataFrame(topics_dict)

print(df_reddit_data)
df_reddit_data.to_csv(data_file, sep=',', index=False)
