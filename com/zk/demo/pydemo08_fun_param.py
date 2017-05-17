#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年5月17日
参数
@author: 123
'''

#位置参数  对于 power(x)函数，参数 x 就是一个位置参数。
def power(x):
    return x*x 

print ("位置参数:",power(5))
#x的n次方
def power2(x,n):
    ji = x
    while n>1:
        ji = ji*x
        n = n-1
    return ji

print ("任意数的n次方",power2(5,3))

def enroll(name,gender,age=6,city='jinan'):
    print('name:%s'% name)
    print('gender:%s'% gender)
    print('age:',age)
    print('city:%s' % city)

enroll('zhang',10)
enroll('Adam', 'M', city='Tianjin')

'''可变参数
在 Python 函数中，还可以定义可变参数。顾名思义，可变参数就是传
入的参数个数是可变的，可以是 1 个、2 个到任意个，还可以是 0 个'''
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#但是调用的时候，需要先组装出一个 list 或 tuple：
print ("calc([1,3,5])=",calc([1,3,5]))
print (calc((1,3,5)))

def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print ("可变参数:",calc2(1,3,5))
print ("可变参数:",calc2())
'''
'''