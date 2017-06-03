# -*- coding: utf-8 -*-
'''
Created on 2017-5-17

既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，
这种函数就称之为高阶函数。
把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

@author: Administrator
'''
from functools import reduce

def f(x):
    return x*x


'''map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
因此通过list()函数让它把整个序列都计算出来并返回一个list。'''
L1 = map(f,[1,2,3,4,5])
print (list(L1))

#，map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
L2 = list(map(str,[1,2,3,5]))
print (L2) 
 
'''再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：'''


def add(x,y):
    return x+y

print (reduce(add,[1,2,3,4,5,6]))
 
def fn(x,y):
    return x*10+y

print(reduce(fn,[1,3,4,7,9]))


def char2num(s):
	return {'0':0,'1':1,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

#如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
print (reduce(fn,map(char2num,'13479')))


#整理成一个str2int的函数就是
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		 return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s)) 

print ('str2int:',str2int('13479'))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

##Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(x,y):
	return x*y

L1 = [3,4,5,9]
print('prod:',reduce(prod,L1))


''' 

'''