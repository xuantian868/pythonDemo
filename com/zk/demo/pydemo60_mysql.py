# -*- coding: utf-8 -*-
'''
Created on 2017-6-3
pymsql是Python中操作MySQL的模块，其使用方法和MySQLdb几乎相同。但目前pymysql支持python3.x而后者不支持3.x版本。
注意：存在中文的时候，连接需要添加charset='utf8'，否则中文显示乱码。
@author: Administrator
'''

import pymysql

#创建连接
conn = pymysql.connect(host='127.0.0.1', port=3308, user='root', passwd='lihlsereb', db='carshop', charset='utf8')
# 创建游标
cursor = conn.cursor()

#执行sql，并返回影响行数
effect_row = cursor.execute("select * from tb_businessshop")
print("tb_businessshop的数量是:%s" % effect_row)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()