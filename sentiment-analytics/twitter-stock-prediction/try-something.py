# Libraries
import nest_asyncio
import twint

nest_asyncio.apply()
import pandas as pd
from datetime import datetime, timedelta


def getTweets(search_term, until, limit=20):
    """
    Configures Twint and returns a dataframe of tweets for a specific day.
    """
    # Configuring Twint for search
    c = twint.Config()

    # c.Username = 'sonusood'

    # The limit of tweets to retrieve
    c.Limit = limit

    # Search term
    c.Search = search_term

    # Removing retweets
    c.Filter_retweets = True

    # Popular tweets
    c.Popular_tweets = True

    # Lowercasing tweets
    c.Lowercase = True

    # English only
    c.Lang = 'en'

    # Tweets until a specified date
    c.Until = until + " 00:00:00"

    # Making the results pandas friendly
    c.Pandas = True

    # Stopping print in terminal
    c.Hide_output = True

    # Searching
    twint.run.Search(c)

    # Assigning the DF
    df = twint.storage.panda.Tweets_df

    # Returning an empty DF if no tweets were found
    if len(df) <= 0:
        return pd.DataFrame()

    # Formatting the date
    df['date'] = df['date'].apply(lambda x: x.split(" ")[0])

    return df


def tweetByDay(start, end, df, search, limit=20):
    """
    Runs the twint query everyday between the given dates and returns
    the total dataframe.
    """
    # Finishing the recursive loop
    if start == end:
        # Removing any potential duplicates
        df = df.drop_duplicates(subset="id")
        print(len(df))
        return df

    # Appending the new set of tweets for the day
    tweet_df = getTweets(search, end, limit)

    # Running the query a few more times in case twint missed some tweets
    run = 0

    while len(tweet_df) == 0 or run <= 2:
        # Running query again
        tweet_df = getTweets(search, end, limit)

        # Counting how many times it ran
        run += 1

    # Adding the new tweets
    df = df.append(tweet_df, ignore_index=True)

    # Updating the new end date
    new_end = (datetime.strptime(end, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")

    # Printing scraping status
    print(f"\t{len(df)} Total Tweets collected as of {new_end}\t")

    # Running the function again
    return tweetByDay(start, new_end, df, search)


df = tweetByDay("2021-09-01", "2021-08-21", pd.DataFrame(), search="$GME", limit=20)
print(df)

