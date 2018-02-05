#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def run_crawler_beta():
    response = requests.get('https://github.com/')
    # response = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(html)
    # print(soup.title)
    # print(soup.title.name)
    print(soup.title.string)
    # print(soup.get_text())
    # for link in soup.find_all('a'):
    #     print(link)
    print(soup.a)
    print(soup.p.find_all('a'))
    print(soup.find(id='facebox'))

    # print(soup.id.quick-start) # error
    # print(soup.div(id='quick-start')) # []
    # print(soup.get('div', id='quick-start')) # error
    # print(soup.find(id='quick-start')) # correct

if __name__ == '__main__':
    run_crawler_beta()