#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Fri Sep 14 22:43:33 2018

Source: https://github.com/realpython/python-scripts/blob/master/scripts/08_basic_email_web_crawler.py
'''

import requests
import re

def fetch_website():
    # get url
    url = input('Enter a URL (include `http://`): ')
    headers = {'user-agent': 'Mozilla/5.0'}
    website = None
    # connect to the url
    try:
        website = requests.get(url, headers=headers)
    except requests.ConnectionError as error:
        print(f'Error fetching url {url}', error)
    return website

def main():
    website = fetch_website()
    if website:
        # read html
        html = website.text
        # use re.findall to grab all the links
        links = re.findall(r'"((http|ftp)s?://.*?)"', html)
        emails = re.findall(r'([\w\.,]+@[\w\.,]+\.\w+)', html)
        # print the number of links in the list
        print(f'Found {len(links)} links')
        print(f'Found {len(emails)} emails')
        for email in emails:
            print(email)
    print(f'Done!\n')

if __name__ == '__main__':
    main()

'''
output:

Enter a URL (include `http://`): https://en.wikipedia.org/wiki/Main_Page
Found 127 links
Found 0 emails
Done!

'''
