#!/usr/bin/env python2

from db import models
from getch import getch
import os
import sys

def nextUnclassifiedTweet():
    return models.Tweet.select().where(models.Tweet.classification >> None).limit(1).get()
def remainingUnclassifiedTweets():
    return models.Tweet.select().where(models.Tweet.classification >> None).count()

tweet = nextUnclassifiedTweet()
while tweet:
    additionalFromUser = models.Tweet.select().where(models.Tweet.screen_name == tweet.screen_name).where(models.Tweet.id != tweet.id)

    _=os.system('clear')
    print ""
    print ""
    print ""
    print "  +"+("-"*(len(tweet.text)+6))+"+"
    print "  |"+(" "*(len(tweet.text)+6))+"|"
    print "  |   "+tweet.text+"   |"
    print "  |"+(" "*(len(tweet.text)+6))+"|"
    print "  +--v"+("-"*(len(tweet.text)+3))+"+"
    print "   @"+tweet.screen_name+" "+(" "*(len(tweet.text)-(len(tweet.screen_name)*2)-len(str(tweet.id))-24))+"https://twitter.com/"+tweet.screen_name+"/status/"+str(tweet.id)
    if len(additionalFromUser) > 0:
        print ""
        print "  ----- "+str(len(additionalFromUser))+" others from this user: -----"
        for aTweet in additionalFromUser:
            print "     - "+aTweet.text
    print ""
    print ""
    print "   Please Rate:       1 :)     2 :|     3 :(      4 :( + related      (q to quit)"
    print "  ("+str(remainingUnclassifiedTweets())+" left to classify)"
    sys.stdout.write("   ")
    result = getch()

    if (result == "1"):
        tweet.classification = "ok"
    elif (result == "2"):
        tweet.classification = "neutral"
    elif (result == "3"):
        tweet.classification = "harassing"
    elif (result == "4"):
        tweet.classification = "harassing"
        for aTweet in additionalFromUser:
            aTweet.classification = "harassing"
            aTweet.save()
    elif (result == "0"):
        tweet.classification = "ok"
        for aTweet in additionalFromUser:
            aTweet.classification = "ok"
            aTweet.save()
    elif (result == "q"):
        _=os.system('clear')
        quit()
    tweet.save()
    tweet = nextUnclassifiedTweet()
