#!/usr/bin/env python2

from db import models
from peewee import fn
from reverend.thomas import Bayes

tweets = models.Tweet.select().where(
    (models.Tweet.classification == 'ok') | (models.Tweet.classification == 'harassing')       
).order_by(fn.Random())
countTrain = int(len(tweets) * 0.8)

train = tweets[:countTrain]
test = tweets[countTrain:]

guesser = Bayes()

for tweet in train:
    guesser.train(tweet.classification, tweet.text.lower())


correct = 0
correctHarassing = 0
totalHarassing = 0
incorrect = 0
falsePos = 0
falseNeg = 0
for tweet in test:
    resultsRaw = guesser.guess(tweet.text.lower())
    results = {}
    for k,v in resultsRaw:
        results[k] = v

    guess = 'harassing' if results.get('harassing', 0.0) > 0.4 else 'ok'

    if tweet.classification == 'harassing':
        totalHarassing += 1

    if (guess == tweet.classification):
        correct += 1
        if (tweet.classification == 'harassing'):
            correctHarassing += 1
    else:
        incorrect += 1
        if (tweet.classification == 'harassing'):
            falseNeg += 1
        else:
            falsePos += 1

print str(correctHarassing)+"/"+str(totalHarassing)+" harassing tweets filtered!"
print "Correct: "+str(round(100*correct/float(len(test))))+"%"
print "False Pos: "+str(round(100*falsePos/float(len(test))))+"%"
print "False Neg: "+str(round(100*falseNeg/float(len(test))))+"%"
