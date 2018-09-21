#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:03:20 2018

Example of web scraping

Data also available on https://www.gold.org/feeds/xml/spot/

@author: jc
"""

import os
from bs4 import BeautifulSoup
import urllib.request
from time import sleep
from datetime import datetime

def getGoldPrice():
    url = 'https://www.gold.org/'
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    priceWrapper = soup.find_all('div', class_='ask')[0]
    price = priceWrapper.find_all('dd', class_='value')[0]
    return price.text

def main():
    dirname = os.path.split(os.path.abspath(__file__))
    log = os.path.join(dirname[0], 'goldprices.log')
    print(f'writing to log {log}\n')
    with open(log, 'w+') as f:
        for x in range(0, 3):
            now = datetime.now().strftime('%I:%M:%S%p')
            goldPrice = getGoldPrice()
            line = f'{now}, {goldPrice}, USD\n'
            print(line)
            f.write(line)
            sleep(3)

if __name__ == '__main__':
    main()
