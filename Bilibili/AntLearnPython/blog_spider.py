#!/usr/bin/env python3
# coding:utf-8
import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}" for page in range(1, 50 + 1)
]


def craw(url):
    r = requests.get(url)
    return r.text


def parse(html):
    # post-item-title
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link['href'], link.get_text())for link in links]

if __name__ == '__main__':
    for result in parse(craw(urls[10])):
        print(result)