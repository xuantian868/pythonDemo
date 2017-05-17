#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2017年5月17日
if else demo
@author: 123
'''

age = 20
if age >= 6:
    print ("teenager")
elif age >= 18:
    print ('adult')
else:
    print('kid')
    
'''小明身高 1.75，体重 80.5kg。请根据 BMI 公式（体重除以身高的平方）
帮小明计算他的 BMI 指数，并根据 BMI 指数：
 低于 18.5：过轻
 18.5-25：正常
 25-28：过重
 28-32：肥胖
 高于 32：严重肥胖'''
    
height = 1.75
weight = 80.5
bmi = 80.5/(1.75*1.75)
print ('小明的体重指数 :%.2f' % bmi)

msg = ""
if bmi < 18.5:
    msg = "太轻了...."
elif bmi>18.5 and bmi<25:
    msg = "正常"
elif bmi>25 and bmi<28:
    msg = "过重"
elif bmi>28 and bmi<32:
    msg = "肥胖"
else :
    msg = "严重肥胖"
    
print(msg)