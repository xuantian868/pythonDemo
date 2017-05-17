#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年5月17日
list 和 tuple 是 Python 内置的有序集合，一个可变，一个不可变
@author: 123
'''

#list Python 内置的一种数据类型是列表：list。list 是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['zhang','wang','li']
print (len(classmates),classmates[0],classmates[-1])

#append 添加到list末尾
classmates.append("zhang")

print ("添加一个元素后:",classmates)
print (len(classmates),classmates[0],classmates[-1])
#也可以把元素插入到指定的位置，比如索引号为 0 的位置
classmates.insert(0, 'tiger')
print ("插入一个元素后:",classmates)

#要删除 list 末尾的元素，用 pop()方法：
classmates.pop()
print ("删除一个元素后:",classmates)

#list 里面的元素的数据类型也可以不同，
L = ['Apple', 123, True]
print (L)

#list 元素也可以是另一个 list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print (s)

#tuple 另一种有序列表叫元组：tuple。tuple 和 list 非常类似，但是 tuple 一旦初始化就不能修改
classmates2 = ('Michael', 'Bob', 'Tracy')
print (classmates2)

#tuple 的陷阱：当你定义一个 tuple 时，在定义的时候，tuple 的元素就必须被确定下来
t = (1,2)
t1 = ()  #空的元组
'''定义的不是 tuple，是 1 这个数！这是因为括号()既可以表示 tuple，又
可以表示数学公式中的小括号，这就产生了歧义，因此，Python 规定，
这种情况下，按小括号进行计算，计算结果自然是 1'''
t2 = (1)  #元素是1的元组
#只有 1 个元素的 tuple 定义时必须加一个逗号
t3 = (1,)  #要定义一个只有 1 个元素的 tuple 


L = [
 ['Apple', 'Google', 'Microsoft'],
 ['Java', 'Python', 'Ruby', 'PHP'],
 ['Adam', 'Bart', 'Lisa']
]
print (L[0][0],L[2][1])
