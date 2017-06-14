# -*- coding: utf-8 -*-
'''
Created on 2017-6-14

python提供了两个模块来实现多线程thread 和threading ，thread 有一些缺点，在threading 得到了弥补，
为了不浪费你和时间，所以我们直接学习threading 就可以了。

setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，
如果不设置为守护线程程序会被无限挂起。子线程启动后，父线程也继续执行下去，
当父线程执行完最后一条语句print "all over %s" %ctime()后，没有等待子线程，
直接就退出了，同时子线程也一同结束。
@author: Administrator
'''
import threading
from time import ctime,sleep

def music(func):
	for i in range(2):
		print ("I was listening to %s %s" %(func,ctime()))
		sleep(1)

def movie(func):
	for i in range(2):
		print ("I was watching %s %s" %(func,ctime()))
		sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'天涯',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=(u'加勒比海盗',))
threads.append(t2)

if __name__ == '__main__':
	for t in threads:
		t.setDaemon(True)
		t.start()
    t.join()


print ("all over time %s %s" %('aaaaa',ctime()))