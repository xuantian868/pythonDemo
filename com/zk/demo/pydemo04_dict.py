#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年5月17日
dict 字典
@author: 123
'''
'''Python 内置了字典：dict 的支持，dict 全称 dictionary，在其他语言中也
称为 map，使用键-值（key-value）存储，具有极快的查找速度。
'''
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print (d['Bob'])

#把数据放入 dict 的方法，除了初始化时指定外，还可以通过 key 放入
d['Adam'] = 67
print (d)
print (d['Adam'])

#由于一个 key 只能对应一个 value，所以，多次对一个 key 放入 value，后面的值会把前面的值冲掉
d['Michael'] = 62
print (d['Michael'],d.get('Michael'))

if 'aaa' in d:
    print("dict has key 'aaa'")
else:
    print("dict does't has key 'aaa'")
    
#要删除一个 key，用 pop(key)方法，对应的 value 也会从 dict 中删除
d.pop('Michael')
print ("删除后key=Michael的dictionary:",d)


'''和 list 比较，dict 有以下几个特点：
1. 查找和插入的速度极快，不会随着 key 的增加而增加；
2. 需要占用大量的内存，内存浪费多。
而 list 相反：
1. 查找和插入的时间随着元素的增加而增加；
2. 占用空间小，浪费内存很少。
所以，dict 是用空间来换取时间的一种方法。
dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，
正确使用 dict 非常重要，需要牢记的第一条就是 dict 的 key 必须是不可
变对象。在 Python 中，字符
串、整数等都是不可变的，因此，可以放心地作为 key。而 list 是可变
的，就不能作为 key

'''