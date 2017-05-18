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
    
'''。如果一个函数定义中包含 yield 关
键字，那么这个函数就不再是一个普通函数，而是一个 generator：'''
def odd():
    print ('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
    
obj = odd()
next(obj)
next(obj)
next(obj)


def fib(max):
    n,a,b = 0,0,1
    while(n<max):
        yield b
        a,b = b,a+b
        n = n+1
    
    return 'done'  

for n in fib(5):
    print (n)
        
        
#杨辉三角
def triangles(num):
    n =1
    b = []
    yield b
    while (n<num):
        print('n=',n)
        if n==1:
            b[0] = [1]
        elif n==2:
            b[1] = [1,1]
        else:
            '''b[n-1].append(1)
            i = 1
            while i<n-1: 
                b[n].append(b[n-1][i-1]+b[n-1][i])
                i = i+1
                
            return 'done'
            '''
        n=n+1      
        #yield b
        
for x in triangles(3):
    print (x)
                 
               
    
