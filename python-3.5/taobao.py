#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


import urllib.request
import re


keyname="短裙"
key=urllib.request.quote(keyname)
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(0,100):
    url="https://s.taobao.com/list?q="+key+"&cat=16&style=grid&seller_type=taobao&spm=a217f.8051907.1000187.1&bcoffset=12&s="+str(i*60)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat='pic_url":"//(.*?)"'
    imagelist=re.compile(pat).findall(data)
    # print(imagelist)
    for j in range(0,len(imagelist)):
        thisimg=imagelist[j]
        thismgurl="http://"+thisimg
        file="/Users/jiajia/Desktop/taobao-img/"+str(i)+str(j)+".jpg"
        urllib.request.urlretrieve(thismgurl,filename=file)