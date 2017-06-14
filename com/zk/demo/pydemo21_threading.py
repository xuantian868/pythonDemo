# -*- coding: utf-8 -*-
'''
Created on 2017-6-14


@author: Administrator
'''

import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(4)

def move(func):
    for i in range(2):
        print ("I was at the %s! %s" %(func,ctime()))
        sleep(5)

'''
　创建了threads数组，创建线程t1,使用threading.Thread()方法，
在这个方法中调用music方法target=music，args方法对music进行传参。 
把创建好的线程t1装到threads数组中。接着以同样的方式创建线程t2，并把t2也装到threads数组。
'''
threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

'''
setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，
如果不设置为守护线程程序会被无限挂起。子线程启动后，父线程也继续执行下去，
当父线程执行完最后一条语句print "all over %s" %ctime()后，没有等待子线程，直接就退出了，
同时子线程也一同结束。
  join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。
  
  执行结果
  I was listening to 爱情买卖. Wed Jun 14 21:29:07 2017
I was at the 阿凡达! Wed Jun 14 21:29:07 2017
I was listening to 爱情买卖. Wed Jun 14 21:29:11 2017
I was at the 阿凡达! Wed Jun 14 21:29:12 2017
all over Wed Jun 14 21:29:17 2017

从上面看music和movie是同事启动的 ，所有自线程执行完后 ，才会执行主线程
'''
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join() #join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞

    print ("all over %s" %ctime())


