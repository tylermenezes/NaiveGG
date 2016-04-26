# NaïveGG: A Naive Bayes Classifier for Online Harassment
## Introduction

NaïveGG is a system for detecting harassing messages based on a Naïve Bayes Classifier, used in one of the earliest
forms of spam filter. "GG" is a reference to GamerGate, where most of the harassers in this test have come from, as
well as nod to Randi Harper's [ggautoblocker](https://github.com/freebsdgirl/ggautoblocker), which is one of the only
real solutions to online harassment at the moment.

I wrote this code to prove a point: online harassment could be solved using technology from the late nineties if
technology companies really cared about preventing harassment. Its "harassment detection engine" comprises only a few
lines of code, so this is really only useful for editorial purposes. If you want to implement it in your own web app,
it's easier to re-write it.

### Requirements

- Python 2.7
- Pip, to install requirements (or all the requirements listed in requirements.txt)
- Twitter API key

## Running

The program consists of several Python scripts for building a corpus, manually classifying tweets, and running
automated classification using a Naive Bayes classifier:

- `ingest.py`: Ingests tweets from training sources
- `classify.py`: Allows you to manually classify Tweets
- `dump.py`: Dumps all tweets for export as a TSV. Takes an optional parameter to dump only tweets with a specific classification.
- `stats.py`: Gets stats about the types of tweets in the corpus
- `test.py`: Learn from a subset of the current corpus, and validate on a separate test set, reporting success

In order to use any of the scripts, you will need to install the requirements with `pip install -r`. (You may want to
create a virtualenv in order to make sure things work properly.)

## Performance

I created and classified a corpus of tweets from three accounts which had recently been subject to harassment. 1391
were ok tweets, and 633 were harassing.

The tool was able to correctly identify 66% of harassing tweets as harassment. Overall, 82% of tweets were categorized
correctly, with an 8% false-positive rate.

Is that a great success? While I wouldn't directly put this tool into production, I think this was a success. This tool
shows that even an extremely naïve system is able to do a decent job of filtering harassment.

Obviously, Twitter couldn't use this to block anyone accused of sending a harassing tweet, but an improved version
could be used to identify serial harassers, and as a tool to hide suspected harassing tweets from high-profile targets.

Several improvements can be made to dramatically increase the detection success rate and reduce the number of false
positives:

- Increase the corpus size
- Create a per-user harassment score, and include that in the tweet's harassment score (many harassing tweets were from repeat offenders)
- Include the user's account age when considering harassment (many harassing tweets were newly created for the purpose)
- Consider other account factors, such as whether the recipient is following the tweeter (or one of the tweeter's followers, etc)
- Switch to a better classifier, perhaps one of the MLaaS providers (Azure Cortana Intelligence Suite, Amazon ML, etc)

The goal of this project was to show that Twitter and other social media companies could take very trivial steps to
combat harassment; I believe the project in its current state does that.

## What is Harassment?

Probably 2-3% of the Tweets in the corpus are complaints that the recipient isn't being harassed, it's just legitimate
criticism. If an organized mob of people was following me around on the street and shouting about how awful I am, I'd
consider that harassment, so I've marked the same as harassment here.

I marked tweets as OK if they seemed to be a genuine criticism, namely if they:

- Directly and specifically addressed something in a tweet (or linked content), and
- Were not from someone who serially critizised everything posted, and
- Did not include ad hominem attacks, and
- Otherwise used reasonable language

If it was a tough call, or the tweet didn't have enough context, I marked it as neutral. Neutral tweets are only
included in the testing set, not the training set.

## Ingestion Process
