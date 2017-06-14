# -*- coding: utf-8 -*-
'''
Created on 2017-6-6

urllib是Python标准库的一部分,包含urllib.request,urllib.error,urllib.parse,urllib.robotparser四个子模块,这里主要介绍urllib.request的一些简单用法/

打开url后,我们可以将内容写入一个本地文件来达到保存网页的目的,但是这里有一个更方便的方法,那就是调用urlretrieve()

@author: Administrator
'''
import urllib.request
#urlopen返回一个类文件对象,可以像文件一样操作,同时支持一下三个方法
url = 'http://www.baidu.com'
local_path = 'c:\\baidu.html'
response = urllib.request.urlopen(url)
html = response.read()
print(html)

urllib.request.urlretrieve(url,local_path)



