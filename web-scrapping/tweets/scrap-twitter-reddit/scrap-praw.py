import pandas as pd
import praw

reddit_read_only = praw.Reddit(client_id="mUDx28SwnElkOkkZP_fMYA",  # your client id
                               client_secret="vJ1g77oYII-EqJjuzAn7dz76DOzV8Q",  # your client secret
                               user_agent="Scraper 1.0 by /u/mtech-proj")

subreddit = reddit_read_only.subreddit("wallstreetbets")

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

top_posts.to_csv("top_reddit_posts.csv", index=True)
