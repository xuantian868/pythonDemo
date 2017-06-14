# -*- coding: utf-8 -*-
'''
Created on 2017-6-6

创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。

@author: Administrator
'''
import socket

#创建socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.baidu.com',80))
print('111')
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
print('222')
#接收数据
buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
	
data = b''.join(buffer)
print('333')
s.close()
print('444')
#接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header ,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

#写文件
with open('c:/baidu.html','wb') as f:
	f.write(html)

