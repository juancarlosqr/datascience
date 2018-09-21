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
from email.parser import HeaderParser

def head(content, length = 10):
    length = length if len(content) > 10 else len(content)
    for line in range(0,length):
        print(content[line])
    print()
            
def get_file_names(path):
    names = []
    if os.path.exists(path):
        print(f'getting file names from {path}')
        names = [os.path.join(path, name) for name in os.listdir(path)]
    else:
        print(f'path {path} does not exit')
    return names

def load_files(file_names):
    subjects = []
    errors = []
    empty = 0
    parser = HeaderParser()
    for file_name in file_names:
        with open(file_name, 'r') as file:
            try:
                msg = parser.parse(file)
                subject = msg['Subject'].replace(',', '').replace('\n', '').replace('\t', '').strip()
                if len(subject):
                    subjects.append(subject)
                else:
                    empty += 1
            except UnicodeDecodeError:
                errors.append(file_name)
            except:
                errors.append(file_name)
    print('file_names', len(file_names))
    print('valid subjects', len(subjects))
    print('errors', len(errors))
    print('empty', empty)
    print()
    return subjects

def get_subjects_from_path(path_base, path_name):
    path = os.path.join(path_base, path_name)
    files = get_file_names(path)
    subjects = load_files(files)
    head(subjects)
    return subjects

def calculate_split_index(total, ratio):
    return int(total * ratio)

def split_datasets(subjects, training_ratio = .8):
    split_index = calculate_split_index(len(subjects), training_ratio)
    training_set = subjects[:split_index]
    test_set = subjects[split_index:]
    return training_set, test_set

def write_datasets(path_name, file_name, ham_set, spam_set):
    lines_count = 0
    path_file = os.path.join(path_name, file_name)
    with open(path_file, 'w+') as file:
        file.write(f'subject,category\n')
        for subject in ham_set:
            lines_count += 1
            file.write(f'{subject},1\n')
        for subject in spam_set:
            lines_count += 1
            file.write(f'{subject},2\n')
    print(f'{lines_count} lines written to {path_file}')

def create_datasets(path_base, subjects_ham, subjects_spam, training_file = 'training.csv',  test_file = 'test.csv'):
    if os.path.exists(path_base):
        if len(subjects_ham) > 0 and len(subjects_spam) > 0:
            training_ham_set, test_ham_set = split_datasets(subjects_ham)
            training_spam_set, test_spam_set = split_datasets(subjects_spam)
            write_datasets(path_base, training_file, training_ham_set, training_spam_set)
            write_datasets(path_base, test_file, test_ham_set, test_spam_set)
        else:
            print(f'no subjects provided')
    else:
        print(f'path {path_base} doesn`t exist')
    print(f'datasets created!\n')

def main():
    path_base = os.path.join(os.path.expanduser('~'), 'dev', 'anaconda', 'datasets', 'spam_classifier')
    subjects_ham = get_subjects_from_path(path_base, 'easy_ham_2')
    subjects_spam = get_subjects_from_path(path_base, 'spam_2')
    create_datasets(path_base, subjects_ham, subjects_spam)

if __name__ == '__main__':
    main()

'''
output:

getting file names from /Users/jc/dev/anaconda/datasets/spam_classifier/easy_ham_2
file_names 1401
valid subjects 1275
errors 126
empty 0

[WM] The MIME information you requested (last changed 3154 Feb 14)
A message for our times
Re: [ILUG] vanquishing the daemons of shell scripting
Re: [Razor-users] Using Razor with non-mbox files
Re: "Ouch. Ouch. Ouch. Ouch. Ouch...."(was Re: My brain hurts)
Re: Pango problems
Re: [Baseline] Raising chickens the high-tech way
Re: [Razor-users] report automation with pine?
Re: [ILUG] expanding a string multiple times
[ILUG] Checking that cronjobs actually ran?

getting file names from /Users/jc/dev/anaconda/datasets/spam_classifier/spam_2
file_names 1397
valid subjects 1265
errors 122
empty 10

Take your love life to the next level               ZIB
[dcms-dev] MY INHERITANCE
Gain Major Cash
< Make $50000 in 90 Days Sending Emails at Home >
Reverse Aging While Burning Fat
Checking Account update
[SA] [Ginger] has sent you a webcam invitation!
HELP WANTED. WORK FROM HOME. FREE INFO
Joke-Of -The- Day
Your approval is needed

2032 lines written to /Users/jc/dev/anaconda/datasets/spam_classifier/training.csv
508 lines written to /Users/jc/dev/anaconda/datasets/spam_classifier/test.csv
datasets created!

'''
