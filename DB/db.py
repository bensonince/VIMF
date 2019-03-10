from DBConnect import *

#Type tweet, adds to database
def add_tweet(tweet1):
    tweetID = db_add_tweet(tweet1)
    return (tweetID)

#Type tweet, reads first found tweet from database
def read_tweet(tweetID):
    tweet1 = db_read_tweet(ID = tweetID)
    return (tweet1)
