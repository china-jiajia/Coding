#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


import re
import urllib.request

# pat="yue"
# string="http://yum.iqianyue.com"
# rst1=re.search(pat,string)
# print(rst1)
#
#
# pat1="[a-zA-Z]+://[^\s]*[.com|.cn]"
# string1='<a href="http://www.baidu.com>hasghj</a>"'
# rst=re.compile(pat1).findall(string1)
# print(rst)


pat="<p>(.*?)</p>"
data=urllib.request.urlopen("https://edu.csdn.net/huiyiCourse/detail/215").read()
result=re.compile(pat).findall(str(data))
print(result)