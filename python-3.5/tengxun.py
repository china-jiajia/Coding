#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


import urllib.request
import re
import urllib.error


'''
爬取腾讯视频"青云志电视剧"评论
url地址:https://v.qq.com/x/cover/0dfpyvfa7tp0ewe.html
'''


headers=("Uuer-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
cursorid="6168254262588031983"
url="https://video.coral.qq.com/varticle/1485749985/comment/v2?callback=_varticle1485749985commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6166612123968780169&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1531840416698https://video.coral.qq.com/varticle/1485749985/comment/v2?callback=_varticle1485749985commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+cursorid+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1531840416698"
for i in range(0,100):
    data=urllib.request.urlopen(url).read().decode("utf-8")
    patnext='"last":"(.*?)"'
    nextid=re.compile(patnext).findall(data)[0]
    # print(nextid)
    patcur='"content":"(.*?)",'
    cursordata=re.compile(patcur).findall(data)
    for j in range(0,len(cursordata)):
        print("----第"+str(i)+str(j)+"条评论内容是:")
        # print(eval('u'"+cursordata[j]+"""))
        print(eval('u"'+cursordata[j]+'"'))
        # print("用户名是：" + eval('u"' + u_list[k] + '"'))
    url = "https://video.coral.qq.com/varticle/1485749985/comment/v2?callback=_varticle1485749985commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6166612123968780169&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1531840416698https://video.coral.qq.com/varticle/1485749985/comment/v2?callback=_varticle1485749985commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + nextid + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1531840416698"

# print(u"\u8fd9\u662f\u6211\u770b\u8fc7\u6700\u70c2\u7684\u7535\u89c6\u5267\uff0c\u592a\u4e0d\u5c0a\u91cd\u539f\u8457\u4e86\uff0c\u8fd9\u4e2a\u7f16\u5267\u4ee5\u540e\u6240\u6709\u7535\u89c6\u5267\u90fd\u4e0d\u4f1a\u518d\u770b\u4e86\uff0c\u592a\u6076\u5fc3\uff0c\u592a\u8ba9\u4eba\u6c14\u6124\u4e86\uff01")