#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年5月17日
for 循环 demo
@author: 123
'''

L = ['Bart', 'Lisa', 'Adam']

for name in L:
    print ("hello ,%s" % name)
    
sum = 0
n = 1
while n < 100:
    n = n+2;
    sum = sum +n;
print ("100内的奇数和是:%d"% sum)