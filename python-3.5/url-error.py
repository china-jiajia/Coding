#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


"""
URLError
    1.连接不上服务器
    2.远程的url不存在
    3.本地没有网络
    4.触发httperror子类
"""

import urllib.error
import urllib.request

try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.HTTPError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)


"""
如下是参考代码段
"""
# req = urllib.Request('http://blog.csdn.net')
# try:
#     urllib.urlopen(req)
# except urllib.HTTPError as e:
#     print(e.code)
#     print(e.reason)





