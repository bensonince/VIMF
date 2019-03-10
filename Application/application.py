import time
from flask import Flask
from flask_restful import Api
from classes import tweet
from db import *

app = Flask(__name__)
api = Api(app)

#api.add_resource(tweet, '/Tweets/<int:num>')
api.add_resource(tweet, '/Tweets/')

if __name__ == '__main__':
    app.run(debug=True)

# def create_tweet(author = "None", Mytweettext = "no text"):
#     #tweet1 = tweet(1223,"Myauthor","ytweet")
#     MyTweet = tweet(time.time(), author, Mytweettext)
#     tweetID = add_tweet(MyTweet)
#     return tweetID

# get tweet based on ID
# def get_tweet(TweetID):
#     tweet1 = read_tweet(TweetID)
#     tweet1.print_tweet()

#TweetID = create_tweet("Myauthor","wow this is gettign complicated")
#tweet.post_tweet("James","classwrite")



# TweetID = tweet.post_tweet("Jimmy","MyClasstweet")
# MyTweet = tweet.get_tweet(TweetID)
# If MyTweet = 401:
#     print ("Error, no tweet with that ID found")
# tweet.print_tweet(TweetID)
