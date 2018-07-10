#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(i)+"*"+str(j)+"="+str(i+j)+"  ",end="")
#     print()


# def function1(a,b):         #形参
#     if(a>b):
#         print(a)
#     else:
#         print(b)
#
# function1(10,19)        #实参

import urllib
from urllib.request import urlopen
from urllib import request

data1=urllib.request.urlopen("http://www.baidu.com").read()

data2=urlopen("http://m.baidu.com").read()

data3=request.urlopen("http://jd.com").read()


print(len(data1))
print(len(data2))
print(len(data3))

# 自定义那某块