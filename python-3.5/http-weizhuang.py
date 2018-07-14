#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao

"""
模拟浏览器http浏览网页的方式进行网页爬取、
"""


import urllib.request

url="https://blog.csdn.net/weiwei_pig/article/details/69891700"
headers="Uuer-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
fh=open("/Users/jiajia/Desktop/python.html","wb")
fh.write(data)
fh.close()

