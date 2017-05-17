#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年5月17日
set 字典
@author: 123
'''
'''set 和 dict 类似，也是一组 key 的集合，但不存储 value。由于 key 不能
重复，所以，在 set 中，没有重复的 key。
''' 

s = set([1, 2, 3])
print (s)

#重复元素在 set 中自动被过滤：
s = set([1, 1, 2, 2, 3, 3])
print (s)

s.add(4)
s.add(7)
print (s)
s.remove(4)
print (s)

#set 可以看成数学意义上的无序和无重复元素的集合，因此，两个 set 可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s3 = s1 & s2
print ("交集:",s3)
print ("并集:",s1 | s2)

#s1.add(['zhang','wang','li'])
'''
set 和 dict 的唯一区别仅在于没有存储对应的 value，但是，set 的原理和
dict 一样，所以，同样不可以放入可变对象，因为无法判断两个可变对
象是否相等，也就无法保证 set 内部“不会有重复元素”。试试把 list 放入
set，看看是否会报错  TypeError: unhashable type: 'list'
'''