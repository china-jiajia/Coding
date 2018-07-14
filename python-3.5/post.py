#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao

"""
模拟http的post 请求抓取数据
"""


import urllib.request
import urllib.parse

url="http://www.iqianyue.com/mypost/"
mydata=urllib.parse.urlencode({"name":"526453770@qq.com","pass":"123456"}).encode("utf-8")
req=urllib.request.Request(url,mydata)

# req.add_header()      #伪装成浏览器
data=urllib.request.urlopen("req").read()
fh=open("/Users/jiajia/Desktop/post.html","wb")
fh.write(data)
fh.close()

