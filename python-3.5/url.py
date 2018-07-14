#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


import urllib.request

# urllib.request.urlretrieve("http://www.hellobi.com",filename="/Users/jiajia/Desktop/1.html")
# urllib.request.urlcleanup()
# file=urllib.request.urlopen("http://www.hellobi.com",timeout=0.5)
# print(file.info())
# print(file.getcode())
# print(file.geturl())


for i in range(0,100):
    try:
        file=urllib.request.urlopen("http://yum.iqianyue.com",timeout=0.1)
        data=file.read()
        print(len(data))
    except Exception as e:
        print("出现异常:"+str(e))

