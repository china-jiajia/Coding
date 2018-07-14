#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao

"""
模拟http的get请求爬取数据
"""

import urllib.request

keywd="陶家家"
# keywd="Python"
keywd=urllib.request.quote(keywd)       #进行中文编码
url="http://www.baidu.com/s?wd="+keywd
# url="https://www.baidu.com/s?wd="+keywd   #这里注意不能使用https进行爬取,https需要证书认证
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
fh=open("/Users/jiajia/Desktop/python.html","wb")
fh.write(data)
fh.close()