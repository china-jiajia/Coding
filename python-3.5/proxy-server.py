#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


import urllib.request

def user_proxy(url,proxy_addr):
    proxy=urllib.request.ProxyHandler({"http":proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    return  data


proxy_addr="114.229.189.140:808"        #建立代理IP池子,代理IP使用列表[]
url="http://www.51cto.com/"

data=user_proxy(url,proxy_addr)
print(len(data))