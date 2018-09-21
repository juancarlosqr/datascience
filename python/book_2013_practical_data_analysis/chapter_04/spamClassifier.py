#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Fri Sep 21 20:21:35 2018

Source, Datasets:
https://github.com/hmcuesta/PDA_Book
https://spamassassin.apache.org/old/publiccorpus/readme.html
https://spamassassin.apache.org/old/publiccorpus/20030228_easy_ham_2.tar.bz2
https://spamassassin.apache.org/old/publiccorpus/20050311_spam_2.tar.bz2

@author: jc
'''

import os
import csv

def list_words(line):
    words = []
    words_temp = line.lower().split()
    for word in words_temp:
        if word not in words and len(word) > 3:
            words.append(word)
    return words

def classifier(subject_line, c_words, c_categories, c_texts, c_total_words):
    category = ''
    category_prob = 0
    for c in c_categories:
        # category probability
        prob_c = float(c_categories[c]) / float(c_texts)
        words = list_words(subject_line)
        prob_total_c = prob_c
        for p in words:
            # word probability
            if p in c_words:
                prob_p = float(c_words[p][c]) / float(c_total_words)
                # probability P(category|word)
                prob_cond = prob_p/prob_c
                # probability P(word|category)
                prob = (prob_cond * prob_p) / prob_c
                prob_total_c = prob_total_c * prob
            if category_prob < prob_total_c:
                category = c
                category_prob = prob_total_c
    return category, category_prob

def training(texts):
    c_words = {}
    c_categories = {}
    c_texts = 0
    c_total_words = 0
    # add the classes to the categories
    for t in texts:
        c_texts = c_texts + 1
        category = t[1]
        if category not in c_categories:
            c_categories[category] = 1
        else:
            c_categories[category] = c_categories[category] + 1
    # add the words with list_words() function
    for t in texts:
        words = list_words(t[0])
        # count total words and create dict with all words
        for p in words:
            if p not in c_words:
                c_total_words += 1
                c_words[p] = {}
                for c in c_categories:
                    c_words[p][c] = 0
            c_words[p][t[1]] = c_words[p][t[1]] + 1
    
    return c_words, c_categories, c_texts, c_total_words

def main():
    path_base = os.path.join(os.path.expanduser('~'), 'dev', 'anaconda', 'datasets', 'spam_classifier')
    path_training = os.path.join(path_base, 'training.csv')
    path_test = os.path.join(path_base, 'test.csv')
    with open(path_training) as f:
        # skip first line (header)
        next(f)
        # when the output of csv.reader goes to dict,
        # it drops duplicated entries for the same key,
        # the same subject in our case
        subjects = dict(csv.reader(f))
    
    p, c, t, tp = training(subjects.items())
    print(f'total training entries: {t}')
    print(f'total words: {tp}')
    print(f'categories: {c}')

    print(f'\nfixed tests')
	# ham test
    clase = classifier('Re: [ILUG] replacement xircom dongle?', p, c, t, tp)
    print('ham test result: {0}'.format(clase))

	# spam test
    clase = classifier('Are you a little behind the times?', p, c, t, tp)
    print('spam test result: {0}'.format(clase))
    
	# ham test
    clase = classifier('Re: [IIU] Recommendations on phone / pda+phone + European GPRS coverage info.', p, c, t, tp)
    print('ham test result: {0}'.format(clase))

    print(f'\ntest.csv dataset')
    # test.csv
    with open(path_test) as f:
        total = 0
        correct = 0
        # skip first line (header)
        next(f)
        tests = csv.reader(f)
        for subject in tests:
            total += 1
            clase = classifier(subject[0], p, c, t, tp)
            if clase[0] == subject[1]:
                correct += 1
        print(f'Efficiency: {correct} correct of {total} test entries ({int((correct*100)/total)}%)\n')

if __name__ == '__main__':
    main()

'''
output:

total training entries: 1537
total words: 2850
categories: {'1': 611, '2': 926}

fixed tests
ham test result: ('1', 0.010485245013069614)
spam test result: ('2', 8.17397212101148e-07)
ham test result: ('1', 1.5175360516316493e-05)

test.csv dataset
Efficiency: 472 correct of 508 test entries (92%)
'''