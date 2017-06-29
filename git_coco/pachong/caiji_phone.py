#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/6/14
# ---------------------------------
# Comment: 主要功能说明


import urllib2
import urllib

values = {"username":"lantian_929@qq.com","password":"lantian929?"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
# resonse = urllib2.urlopen("http://www.baidu.com")
resonse = urllib2.urlopen(request)

print resonse.read()

