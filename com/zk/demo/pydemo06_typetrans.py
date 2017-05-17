#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年5月17日
函数
@author: 123
'''
'''如果想定义一个什么事也不做的空函数，可以用 pass 语句
实际上 pass 可以用来作为占位符，
比如现在还没想好怎么写函数的代码，就可以先放一个 pass，让代码能
运行起来。'''
import math

def pop():
    pass

#我们修改一下 my_abs 的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数 isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x>0:
        return x
    else:
        return -x


'''
原来返回值是一个 tuple！但是，在语法上，返回一个 tuple 可以省略括
号，而多个变量可以同时接收一个 tuple，按位置赋给对应的值，所以，
Python 的函数返回多值其实就是返回一个 tuple，但写起来更方便。
把第三个参数 n 的默认值设定为 0'''
   
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx ,ny 

x ,y = move(100,100,60,math.pi/6)
print (x,y)
r = move(100, 100, 60, math.pi / 6)
print(r)


#my_abs('a')

'''请定义一个函数 quadratic(a, b, c)，接收 3 个参数，返回一元二次方程：
axx+ bx + c = 0
：计算平方根可以调用 math.sqrt()函数：
一元二次方程的一般形式:20(0)axbxca    四种解法：直接开平方法，配方法，公式法， 因式分解法， 
公式法：

'''
def quadratic(a, b, c):
    return (-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)
    
print (quadratic(2,3,1))


'''
如果你已经把 my_abs()的函数定义保存为 abstest.py 文件了，那么，可
以在该文件的当前目录下启动 Python 解释器，用 from abstest import
my_abs 来导入 my_abs()函数，注意 abstest 是文件名（不含.py 扩展名）
'''