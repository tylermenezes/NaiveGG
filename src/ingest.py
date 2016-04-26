#!/usr/bin/env python2

import twitter
from db import models
import re

tw = twitter.Api(
        consumer_key="",
        consumer_secret="",
        access_token_key="",
        access_token_secret=""
)

def ingestMentions(username, pages = 1):
    lastId = None
    for page in range(0, pages):
        mentions = tw.GetSearch(
                term="to:"+user,
                result_type="recent",
                count=100,
                max_id=lastId
        )
        
        for tweet in mentions:
            lastId = tweet.id
            text = tweet.text.replace("\n", " ").replace("\t", "")
            text = re.sub(r"(?:\@|https?\://)\S+", "", text)
            text = re.sub(r" +", " ", text)
            text = text.strip()

            if len(text) < 3:
                continue
            
            if tweet.user.screen_name == username:
                continue

            try:
                models.Tweet.create(
                    id = tweet.id,
                    screen_name = tweet.user.screen_name,
                    text = text,
                    mentioning = user,
                    created_at = tweet.created_at,
                    classification = None
                )
            except:
                pass



users = ['femfreq', 'UnburntWitch']
for user in users:
    ingestMentions(user, 2)
