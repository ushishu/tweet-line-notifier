#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import config
from requests_oauthlib import OAuth1Session
import requests

TCK = config.TWI_CONSUMER_KEY
TCS = config.TWI_CONSUMER_SECRET
TAT = config.TWI_ACCESS_TOKEN
TATS = config.TWI_ACCESS_TOKEN_SECRET
LT = config.LINE_TOKEN

twitter_oauth = OAuth1Session(TCK, TCS, TAT, TATS)

get_timeline_url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
search_tweet_word_url = "https://api.twitter.com/1.1/search/tweets.json?"
post_line_url = "https://notify-api.line.me/api/notify"

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
    response = oauth.get(url, params = params)
    return json.loads(response.text)

def post_line_message(token, url, word):
    header = {
        "Authorization": "Bearer " + token
    }
    payload = {
        "message": word
    }

    response = requests.post(url, data = payload, headers = header)
    print(response)


timeline = get_timeline(twitter_oauth, get_timeline_url)
print("timeline:", timeline)

word = "ushi"
search = get_searching_tweet_word(twitter_oauth, search_tweet_word_url, word)
print("search: ", search)

post_line_message(LT, post_line_url, "Succeed")
