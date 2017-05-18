# -*- coding: utf-8 -*-
'''
Created on 2017-5-17
迭代 Iteration  迭代是通过for ... in来完成
@author: Administrator
'''
from collections import Iterable


'''Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，
都可以迭代，比如dict就可以迭代'''
d = {'a': 1, 'b': 2, 'c': 3}

for v in d:
    print ("key:%s" % v)

for v in d.values():
    print ("value: %s" % v)
    
for k,v in d.items():
    print ("Key=%s ,Value=%s" %(k,v))


#由于字符串也是可迭代对象
for v in 'abc':
    print (v)
    

'''如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：'''    
print (isinstance('abc', Iterable))
print (isinstance(123, Iterable))

'''，如果要对list实现类似Java那样的下标循环怎么办？
Python内置的enumerate函数可以把一个list变成索引-元素对，
这样就可以在for循环中同时迭代索引和元素本身
'''
for i,v in enumerate(['a','b','c']):
    print ("index[%d]:%s" %(i,v))
    

for x,y in [(1,3),(2,4),(3,9)]:
    print (x,y)
