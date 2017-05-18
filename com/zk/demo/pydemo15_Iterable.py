# -*- coding: utf-8 -*-
'''
Created on 2017-5-17
我们已经知道，可以直接作用于 for 循环的数据类型有以下几种：
一类是集合数据类型，如 list、tuple、dict、set、str 等；
一类是 generator，包括生成器和带 yield 的 generator function。
这些可以直接作用于 for 循环的对象统称为可迭代对象：Iterable。

可以被 next()函数调用并不断返回下一个值的对象称为迭代器：
Iterator。
可以使用 isinstance()判断一个对象是否是 Iterator 对象：
可迭代对象 不一定是迭代器


@author: Administrator
'''
from collections import Iterable
from _collections_abc import Iterator

#判断是否时 可迭代对象 
print (isinstance([],Iterable))
print (isinstance({},Iterable))
print (isinstance('abe', Iterable))


print (isinstance((x for x in range(10)), Iterable))
print(isinstance(100,Iterable))

print('----------------------------------------')
#判断是否时 可迭代器对象 
'''生成器都是 Iterator 对象，但 list、dict、str 虽然是 Iterable，却不是
Iterator。
把 list、dict、str 等 Iterable 变成 Iterator 可以使用 iter()函数：
'''
print (isinstance((x for x in range(10)), Iterator))
print (isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))


print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter('abc'),Iterator))

'''是因为 Python 的 Iterator 对象表示的是一个数据流，Iterator 对象可
以被 next()函数调用并不断返回下一个数据，直到没有数据时抛出
StopIteration 错误。可以把这个数据流看做是一个有序序列，但我们却
不能提前知道序列的长度，只能不断通过 next()函数实现按需计算下一
个数据，所以 Iterator 的计算是惰性的，只有在需要返回下一个数据时
它才会计算。
Iterator 甚至可以表示一个无限大的数据流，例如全体自然数。而使用
list 是永远不可能存储全体自然数的。

凡是可作用于 for 循环的对象都是 Iterable 类型；
凡是可作用于 next()函数的对象都是 Iterator 类型，它们表示一个惰性
计算的序列；
集合数据类型如 list、dict、str 等是 Iterable 但不是 Iterator，不过可
以通过 iter()函数获得一个 Iterator 对象。

'''