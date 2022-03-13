import pandas as pd
import praw
from praw.models import MoreComments

from reddit_keys import client_id, client_secret, user_agent

reddit_read_only = praw.Reddit(client_id=client_id,  # your client id
                               client_secret=client_secret,  # your client secret
                               user_agent=user_agent)

subreddit = reddit_read_only.subreddit("wallstreetbets")
tickerlist = ['TSLA']

hot = subreddit.hot(limit=10)
sum = [0] * len(tickerlist)  # our output array
counttotal = 0  # total number of comment read
submissions_counter = 0

for submissions in hot:
    if not submissions.stickied:
        submissions_counter += 1
        if submissions_counter > 5:
            comments = submissions.comments
            for comment in comments:
                if isinstance(comment, MoreComments):
                    continue
                counttotal += 1
                for i, ticker in enumerate(tickerlist):
                    if ticker in comment.body:
                        sum[i] = sum[i] + 1

output = pd.DataFrame(data={'Tick': tickerlist, 'Counts': sum})
print('Total comments read:', counttotal)
print(output[output['Counts'] > 0])

exit(0)

print("Top hot 5")
for post in subreddit.hot(limit=5):
    print(post.title)

posts = subreddit.top("month")
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }

for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)
    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)
    # Unique ID of each post
    posts_dict["ID"].append(post.id)
    # The score of a post
    posts_dict["Score"].append(post.score)
    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)
    # URL of each post
    posts_dict["Post URL"].append(post.url)

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
print(top_posts)

top_posts.to_csv("../data/top_reddit_posts.csv", index=True)
