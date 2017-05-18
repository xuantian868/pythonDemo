# -*- coding: utf-8 -*-
'''
Created on 2017-5-17
关键字参数 和 命名关键字参数
@author: Administrator
'''
#关键字参数
'''关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，
我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，
我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。'''
def person(name,age,**kw):
    print ("name:",name+",age:",age,"other:",kw)
    
    
person('zhang',12)
person('zhang',12,city='bj',sex='man')

#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去： 这种方式过于复杂
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

'''#简化**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
kw将获得一个dict，
注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra'''
person('Jack', 24,**extra)



'''命名关键字参数
如果要限制关键字参数的名字，就可以用命名关键字参数，
例如，只接收city和job作为关键字参数。这种方式定义的函数如下

def student(name,age, * ,city,job):
    print ("name:",name+",age:",age,"city:",city,",job:",job)
    
上面定义报错 ，暂时不知道原因

和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

person('Jack', 24, city='Beijing', job='Engineer')
命名关键字参数必须传入参数名
'''
    
