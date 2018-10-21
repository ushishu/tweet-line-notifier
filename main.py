#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter_oauth = OAuth1Session(CK, CS, AT, ATS)

get_timeline_url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
search_tweet_word_url = "https://api.twitter.com/1.1/search/tweets.json?"

def get_timeline(oauth, url):
    responce = oauth.get(url)
    return json.loads(responce.text)

def get_searching_tweet_word(oauth, url, word):
    params = {
        "q": word,
        "lang": "ja",
        "result_type": "recent",
        "count": "5"
    }
    responce = oauth.get(url, params)
    return json.loads(responce.text)


timeline = get_timeline(twitter_oauth, get_timeline_url)
print("timeline:", timeline)

word = "ushi"
search = get_searching_tweet_word(twitter_oauth, search_tweet_word_url, word)
print("search: ", search)