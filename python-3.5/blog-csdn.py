#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao

import urllib.request
import re


url="https://blog.csdn.net/"        #这个页面有问题
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
openr=urllib.request.build_opener()
openr.addheaders=[headers]
urllib.request.install_opener(openr)       #添加上面的openr为全局的
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
pat='<h3 class="trackinng-ad" data-mod="popu_254"><a href="(.*?)"'
result=re.compile(pat).findall(data)
# print(result)

for i in range(0,len(result)):
    file="/Users/jiajia/Desktop/csdn"+str(i)+".html"
    urllib.request.urlretrieve(result[i],filenname=file)
    print("第"+str(i)+"次爬取成功")
