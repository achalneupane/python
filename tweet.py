import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'dqNlNmUYjgNXUlibdLfKgcORv'
consumer_secret= 'qs6iUiX13aW5NgX3x7ScF4Jfv08XA0npbhpg0srzD85eCTI00I'

access_token='56014744-hBzKM9KgFGqaJWqXqaUM1gU6mtAupG5P4oNCnoFMX'
access_token_secret='vXfsn4pnD6BooW6Zm07vSw43mUCJbmKfgjGHGZzKrbsjh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('happy or sad')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")

##############test
#from textblob import TextBlob
#wiki= TextBlob("Achal is a very nice guy who likes to eat ice-cream and he is famous, but not so famous")
#wiki.tags
#wiki.words
#wiki.sentences
#wiki.sentiment.polarity