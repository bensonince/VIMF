import db
import time

class Vollybyname:
    def __init__(Self, fullname):
        self.fullname = fullname

class Vollysummary:
    def __init__(self, ID, firstname, lastname, supervisor, primcontactno, email, passtype):
        self.ID = ID
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + ' ' + lastname
        self.supervisor = supervisor
        self.primcontactno = primcontactno
        self.email = email
        self.passtype = passtype

class Vollydetail(Vollysummary):
    def __init__(self, redlistedyear, seccontactno, confirmed, groupedwith, yearoff):
        super().__init__(self)
        self.redlistedyear = redlistedyear
        self.seccontactno = seccontactno
        self.confirmed = confirmed
        self.groupedwith = groupedwith
        self.yearoff = yearoff

class Shiftbyname:
    def __init__(Self, shiftname, shiftday, starttime, shiftlength, minslots, maxslots, priority, notes):
        self.shiftname = shiftname
        self.shiftday = shiftday
        self.starttime = starttime
        self.shiftlength = shiftlength
        self.minslots = minslots
        self.maxslots = maxslots
        self.priority = priority
        self.notes = notes


class VollyShift:
    def __init__(self, shiftname, fullname, extrahours, confirmedshift):
        self.shiftname = shiftname
        self.fullname = fullname
        self.extrahours = extrahours
        self.confirmedshift = confirmedshift

#example class
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
