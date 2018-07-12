#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


import re

pat="yue"
string="http://yum.iqianyue.com"
rst1=re.search(pat, string)
print(rst1)


pat1="[a-zA-Z]+://[^\s]*[.com|.cn]"
string1='<a href="http://www.baidu.com>hasghj</a>"'
rst=re.compile(pat1).findall(string1)
print(rst)