#!/usr/bin/env python2

from db import models
import sys

dumpType = sys.argv[1] if len(sys.argv) > 1 else None
tweets = None
if dumpType == None:
    tweets = models.Tweet.select()
elif dumpType == "none":
    tweets = models.Tweet.select().where(models.Tweet.classification >> None)
elif dumpType in ("harassing", "neutral", "ok"):
    tweets = models.Tweet.select().where(models.Tweet.classification == dumpType)
else:
    print "Usage: dump.py [none,harassing,neutral,ok]"
    quit()

for tweet in tweets:
    try:
        print "\t".join([tweet.mentioning, tweet.screen_name, str(tweet.created_at), str(tweet.ingested_at), str(tweet.classification), str(tweet.id), tweet.text])
    except:
        pass

