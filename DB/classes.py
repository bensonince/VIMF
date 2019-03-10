import db
import time

class tweet:
    def __init__(self, time, author, tweet):
        self.time = time
        self.author = author
        self.tweet = tweet

    @staticmethod
    def print(TweetID):
    #     tweet1 = rad_tweet(TweetID)
    #     #tweet1.print_tweet()
        time, author, tweet = db.read_tweet(TweetID)
        print("reading  ", tweet, "by", author, "at", time)

    @staticmethod
    #def get(cls,TweetID):
    def get(TweetID):
        #from db import db_read_tweet
        if db.read_tweet(TweetID) == 0:
            return {'there is no tweet with ID:': TweetID}, 401
        time, author, tweet = db.read_tweet(TweetID)
        return {'Tweet is:': tweet}, 201
        #return cls(time, author, tweet)

    @classmethod
    def post(cls, author = "None", Mytweettext = "no text"):
        MyTweet = cls(time.time(), author, Mytweettext)
        tweetID = db.add_tweet(MyTweet)
        return tweetID
#write

# def create_tweet(author = "None", Mytweettext = "no text"):
#     #tweet1 = tweet(1223,"Myauthor","ytweet")
#     MyTweet = tweet(time.time(), author, Mytweettext)
#     tweetID = add_tweet(MyTweet)
#     return tweetID
#
# # get tweet based on ID
# def get_tweet(TweetID):
#     tweet1 = read_tweet(TweetID)
#     tweet1.print_tweet()
#MyTweet = tweet(1234, "Name", "Tweet")
#MyTweet.print_tweet()
