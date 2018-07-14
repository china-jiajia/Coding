#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Author: Mrtao


import urllib.request
import re
import io
import sys

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
print(sys.getdefaultencoding())

data=urllib.request.urlopen("https://read.douban.com/provider/all").read()
data=data.decode("utf-8")
# print(data)
pat='<div class="name">(.*?)</div>'
mydata=re.compile(pat).findall(data)
print(mydata)
fh=open("/Users/jiajia/Desktop/1.txt","w",encoding="utf-8")
for i in range(0,len(mydata)):
    fh.write(mydata[i] + "\n")

fh.close()