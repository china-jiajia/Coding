#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao

import urllib.request
import re
import urllib.error

data=urllib.request.urlopen("http://news.sina.com.cn/").read()
data2=data.decode("utf-8","ignore")
pat='href="(http://news.sina.com.cn/.*?)"'
allurl=re.compile(pat).findall(data2)

for i in range(0,len(allurl)):
    try:
        print("第"+str(i)+"次爬取")
        thisurl=allurl[i]
        file="/Users/jiajia/Desktop/sinannews/"+str(i)+".html"
        urllib.request.urlretrieve(thisurl,file)
        print("------------成功--------------")
    except urllib.error.HTTPError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

