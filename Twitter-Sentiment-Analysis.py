import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'VfP9SDvNALbpYvG7uEChSkt57'
consumer_secret= 'AKQHx5O0sXbQjkkDwKcmOswUIbI9Ihkurl6tHnDIDQoTkHFQfa'

access_token='596056430-IsFgy7sTKf1vKYXrz26cccYasCoZA9MLlHgwlmSo'
access_token_secret='npwA7M3co7ewnYNWjJjzv5GueYTgvsHyk0gYGfptV5iYR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('BTC')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
