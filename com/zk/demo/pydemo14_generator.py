# -*- coding: utf-8 -*-
'''
Created on 2017-5-17
生成器  这种一边循环一边计算的机制，称为生成器：generator。
要创建一个 generator，有很多种方法。第一种方法很简单，只要把一个
列表生成式的[]改成()，就创建了一个 generator：
@author: Administrator
'''
 
L = (x*x for x in range(1,11))
print (L)
 
#，可以通过 next()函数获得 generator 的下一个返回值
print (next(L))

#使用for循环取出 gennerator的值
for i in L:
    print ("---",i)