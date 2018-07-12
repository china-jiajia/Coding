#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao

import re
import urllib.request


pat="<p>QQ:(.*?)</p>"
pat1="<div class="name">博集天卷</div>"
data=urllib.request.urlopen("https://read.douban.com/provider/all").read()
# data=urllib.request.urlopen("http://edu.csdn.net/huiyiCourse/detail/215").read()
result=re.compile(pat1).findall(str(data))
print(result)


# https://read.douban.com/provider/all