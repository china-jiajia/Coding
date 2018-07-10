#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

#
# fh1=open("/Users/jiajia/Desktop/file3.txt","w")
#
# contents1="我是文件的内容"
#
# fh1.write(contents1)
#
# fh1.close()


fh2=open("/Users/jiajia/Desktop/file3.txt","r",encoding="utf-8")

# data2=fh2.read()
# print(data2)

# line1=fh2.readline()
# print(line1)

while True:
    line=fh2.readline()
    if len(line)==0:
        break
    print(line)
fh2.close()
