#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


'''
千图网爬取图片
'''

import urllib.request
import re
import urllib.error


for i in range(1,10):
    pageurl="http://www.58pic.com/piccate/3-151-0-default-0_2_0_0_default_0-"+str(i)+".html"
    data=urllib.request.urlopen(pageurl).read().decode("utf-8","ignore")
    # print(data)
    # pat='<img src="(.*?).jpg!'
    pat='<a class="thumb-box".*?src="(.*?).jpg!'
    # print(pat)
    imglist=re.compile(pat).findall(data)
    for j in range(0,len(imglist)):
        try:
            thisimg=imglist[j]
            thisimgurl=thisimg+"_1024.jpg"
            file="/Users/jiajia/Desktop/qiantu-img/"+str(i)+str(j)+".jpg"
            urllib.request.urlretrieve(thisimgurl,filename=file)
            print("第"+str(i)+"页第"+str(j)+"图片爬取成功")
        except urllib.error.HTTPError as e:
            if hasattr(e,"code"):
                print(e.code)
            if hasattr(e,"reason"):
                print(e.reason)
        except Exception as e:
            print(e)



#http://www.58pic.com/      前图网地址




