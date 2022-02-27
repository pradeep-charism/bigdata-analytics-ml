import matplotlib.pyplot as plt
import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud

plt.style.use('fivethirtyeight')


def load_data():
    data = pd.read_csv('data/stock_tweets_simple.csv')
    return data


def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity


def get_polarity(text):
    return TextBlob(text).sentiment.polarity


df = load_data()
print(df.head())
print('Dataset size:', df.shape)
print('Columns are:', df.columns)

df['Subjectivity'] = df['Text'].apply(get_subjectivity)
df['Polarity'] = df['Text'].apply(get_polarity)
print(df)

# Print word cloud
all_words = ' '.join(txt for txt in df['Text'])
word_count = WordCloud(width=500, height=300, random_state=21, max_font_size=119).generate(all_words)

plt.imshow(word_count, interpolation="bilinear")
plt.axis('off')
plt.show()
