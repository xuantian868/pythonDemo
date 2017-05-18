# -*- coding: utf-8 -*-
'''
Created on 2017-5-17
递归
@author: Administrator
'''
'''使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题'''
def fact(n):
    if n ==1:
        return n
    else:
        return n*fact(n-1)
    
print ("5!=%d" % fact(5))
