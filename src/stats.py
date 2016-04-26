#!/usr/bin/env python2

from db.models import *
import sys

allTweets = Tweet.select().count()
byClassification = Tweet.select(Tweet.classification, fn.COUNT(Tweet.id).alias('num_tweets')).group_by(Tweet.classification)

for classification in byClassification:
    print str(classification.classification)+": "+str(classification.num_tweets)
