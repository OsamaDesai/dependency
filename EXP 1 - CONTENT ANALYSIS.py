import nltk
from nltk.corpus import twitter_samples
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# download necessary NLTK data
nltk.download('twitter_samples')
nltk.download('vader_lexicon')
nltk.download('stopwords')

# load positive and negative tweets from the NLTK twitter_samples corpus
pos_tweets = twitter_samples.strings('positive_tweets.json')
neg_tweets = twitter_samples.strings('negative_tweets.json')

# create a list of all tweets by combining the positive and negative tweets
all_tweets = pos_tweets + neg_tweets

for tweet in all_tweets[1:10]:
    print(tweet)
    
# create a list of stop words and punctuation to filter out from the tweets
stop_words = stopwords.words('english')
punctuations = list(string.punctuation)
stop_words += punctuations

# initialize the SentimentIntensityAnalyzer from NLTK to analyze the sentiment of the tweets
sia = SentimentIntensityAnalyzer()

# create an empty dictionary to store the topics and their sentiment scores
topics = {}

# loop through each tweet and tokenize the text
for tweet in all_tweets:
    tokens = word_tokenize(tweet)

    # filter out stop words and punctuation from the tokens
    filtered_tokens = [token.lower() for token in tokens if token.lower() not in stop_words]

    # loop through each token and determine its sentiment score using SentimentIntensityAnalyzer
    for token in filtered_tokens:
        sentiment_score = sia.polarity_scores(token)

        # loop through each topic in the dictionary and update its sentiment score
        for topic in topics:
            if topic in filtered_tokens:
                topics[topic]['positive'] += sentiment_score['pos']
                topics[topic]['negative'] += sentiment_score['neg']
                topics[topic]['neutral'] += sentiment_score['neu']
                topics[topic]['count'] += 1
                break
        else:
            # if the token is not already a topic, add it to the dictionary with its initial sentiment score
            topics[token] = {
                'positive': sentiment_score['pos'],
                'negative': sentiment_score['neg'],
                'neutral': sentiment_score['neu'],
                'count': 1
            }

# print the sentiment scores for each topic
for topic in topics:
    print(topic)
    print('Positive score:', topics[topic]['positive'] / topics[topic]['count'])
    print('Negative score:', topics[topic]['negative'] / topics[topic]['count'])
    print('Neutral score:', topics[topic]['neutral'] / topics[topic]['count'])
    print('\n')
