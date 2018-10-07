# -*- coding: utf-8 -*-
'''
Created on Fri Oct 5 19:21:35 2018

@author: jc
'''

import sys
import yaml
from twython import Twython

def get_config(key):
    with open('config.yml', 'r') as f:
        config = yaml.load(f)
    return config[key]

def get_twitter_client():
    config_twitter = get_config('twitter')
    twitter = Twython(
        config_twitter['consumer_key'],
        config_twitter['consumer_secret'],
        config_twitter['access_token'],
        config_twitter['access_secret']
    )
    return twitter

def print_tweets(tweets):
    if 'statuses' in tweets:
        tweets = tweets['statuses']
    for tweet in tweets:
        print(f'@{tweet["user"]["screen_name"]}: {tweet["text"]}\n')

def get_home_timeline():
    twitter = get_twitter_client()
    tweets = twitter.get_home_timeline()
    print_tweets(tweets)

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        print('provide an action. options: timeline, search "search term"')
        exit(1)
    action = sys.argv[1]
    if action == 'timeline':
        get_home_timeline()
    elif action == 'search':
        if (len(sys.argv) == 2):
            print('provide a search term')
            exit(1)
        q = sys.argv[2]
        twitter = get_twitter_client()
        print_tweets(twitter.search(q=q))
        