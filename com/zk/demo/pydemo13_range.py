# -*- coding: utf-8 -*-
'''
Created on 2017-5-17
列表生成式  列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
@author: Administrator
'''

L = list(range(10))  #[0,9]
print (L)

L = list(range(1,11))  #[1,10]
print (L)

#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环
L = []
for i in range(1,11):
    L.append(i*i)
    
print (L)
#但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
'''写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用'''
L = [x*x for x in range(1,11)]
print (L)

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
L = [x*x for x in range(1,11) if x%2==0]
print (L)

#还可以使用两层循环，可以生成全排列：
L = [a+b for a in 'abc' for b in 'xyz']
print (L)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
L = [k +'='+v for k,v in d.items()]
print (L)

#将所有大写改为小写
L = ['Hello', 'World', 'IBM', 'Apple']
L = [s.lower() for s in L]
print (L)

#输出结果 ['hello', 'world', 'apple']  使用内建的isinstance函数可以判断一个变量是不是字符
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print (L2)
