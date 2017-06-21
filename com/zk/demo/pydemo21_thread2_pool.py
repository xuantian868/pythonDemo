# -*- coding: utf-8 -*-
'''
Created on 2017-6-15
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
@author: Administrator
'''

from multiprocessing import Pool
import os,time,random

#print ('process (%s) start...'% os.getpid())


def long_time_task(name):
	print('Ran task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	#time.sleep((random()*3))
	sleep(2)
	end = time.time()
	print('Task %s rans %0.2f seconds.'%(name,(end-start)))

if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(3)
	for i in range(5):
		p.apply_async(long_time_task,args=(i,))
	print('Waiting for all subprocessed done.')
	p.close()
	p.join()
	print('All subprocesses done.')

