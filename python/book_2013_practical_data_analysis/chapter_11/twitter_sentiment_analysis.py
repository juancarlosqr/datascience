# -*- coding: utf-8 -*-
'''
Created on Fri Oct 5 10:21:35 2018

source:
http://help.sentiment140.com/home

The data is a CSV with emoticons removed. Data file format has 6 fields:
0 - the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
1 - the id of the tweet (2087)
2 - the date of the tweet (Sat May 16 23:58:44 UTC 2009)
3 - the query (lyx). If there is no query, then this value is NO_QUERY.
4 - the user that tweeted (robotickilldozr)
5 - the text of the tweet (Lyx is cool)

nltk.download('punkt', download_dir='/anaconda3/envs/practical_data_analysis/nltk_data')

@author: jc
'''

import os
import sys
import csv
import nltk
import read_twitter as tw

def bag_of_words(tweets):
    words_list = []
    for (words, sentiment) in tweets:
        words_list.extend(words)
    return words_list

def get_word_features(word_list):
    word_list = nltk.FreqDist(word_list)
    word_features = word_list.keys()
    return word_features

def get_features(doc):
    doc_words = set(doc)
    feat = {}
    for word in word_features:
        feat['contains(%s)' % word] = (word in doc_words)
    return feat

def get_training_data():
    positive_tweets = []
    negative_tweets = []
    file_name = 'testdata.manual.2009.06.14.csv'
    with open(file_name, 'r') as f:
        reader = csv.reader(f, quotechar='"')
        for row in reader:
            tweet = row[5]
            if (int(row[0]) == 0):
                negative_tweets.append((tweet, 'negative'))
            if (int(row[0]) == 4):
                positive_tweets.append((tweet, 'positive'))
    print(f'positive_tweets: {len(positive_tweets)}')
    print(f'negative_tweets: {len(negative_tweets)}')
    return positive_tweets, negative_tweets

def generate_tweets_corpus(positive_tweets, negative_tweets):
    corpus_of_tweets = []
    for (words, sentiment) in positive_tweets + negative_tweets:
        words_filtered = [e.lower() for e in nltk.word_tokenize(words) if len(e) >= 3]
        corpus_of_tweets.append((words_filtered, sentiment))
    return corpus_of_tweets

def extract_features(tweet):
    words = tweet.lower().split()
    return dict((f'contains({w})', True) for w in words if len(w) >= 3)

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        print('provide a search term')
        exit(1)
    q = sys.argv[1]
    positive_tweets, negative_tweets = get_training_data()
    corpus_of_tweets = generate_tweets_corpus(positive_tweets, negative_tweets)
    word_features = get_word_features(bag_of_words(corpus_of_tweets))
    # nltk
    training = nltk.classify.apply_features(get_features, corpus_of_tweets)
    classifier = nltk.NaiveBayesClassifier.train(training)
    classifier.show_most_informative_features()
    print(f'labels: {sorted(classifier.labels())}\n')
    # classify new tweets
    twitter = tw.get_twitter_client()
    tweets = twitter.search(q=q, result_type='recent', count=100, lang='en')
    positive_sentiment = 0
    negative_sentiment = 0
    for tweet in tweets['statuses']:
        status = tweet['text']
        screen_name = tweet['user']['screen_name']
        sentiment = classifier.classify(extract_features(status))
        if sentiment == 'positive':
            positive_sentiment += 1
        else:
            negative_sentiment += 1
        print(f'@{screen_name}: {status}\nsentiment: {sentiment}\n\n')
    print(f'query: {q}\npositive: {positive_sentiment}\nnegative: {negative_sentiment}')
    