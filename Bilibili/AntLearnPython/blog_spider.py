#!/usr/bin/env python3
# coding:utf-8
import requests

urls = [
    f"https://www.cnblogs.com/#p{page}" for page in range(1, 50 + 1)
]

def craw(url):
    r = requests.get(url)
    print(url, len(r.text))
