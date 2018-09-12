#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:03:20 2018

Example of web scraping

Data also available on https://www.gold.org/feeds/xml/spot/

@author: jc
"""

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
    with open('goldprices.log', 'w') as f:
        for x in range(0, 3):
            now = datetime.now().strftime('%I:%M:%S%p')
            goldPrice = getGoldPrice()
            line = '{0}, {1}, {2}\n'.format(now, goldPrice, 'USD')
            print(line)
            f.write(line)
            sleep(3)

if __name__ == '__main__':
    main()
