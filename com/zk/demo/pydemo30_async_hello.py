# -*- coding: utf-8 -*-
'''
Created on 2017-5-23

ython内建的filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。

注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

@author: Administrator
'''

import threading
import asyncio

@asyncio.coroutine
def hello():
	print('hello world! %s' % threading.current_thread())
	yield  asyncio.sleep(1)
	print ('hello again %s' % threading.current_thread())
	
loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()