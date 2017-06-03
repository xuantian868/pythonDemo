# -*- coding: utf-8 -*-
'''
Created on 2017-6-3

执行INSERT等操作后要调用commit()提交事务；

MySQL的SQL占位符是%s。

@author: Administrator
'''

import pymysql


#创建连接
conn = pymysql.connect(host='127.0.0.1', port=3308, user='root', passwd='lihlsereb', db='carshop', charset='utf8')
# 创建游标
cursor = conn.cursor()
cursor.execute('insert into tb_businessshop (businessshop_id, c_name,c_address,c_city) values (%s, %s,%s,%s)', ['58', '测试名称','天津福建路下瓦房','天津河西区'])
print ("影响行数:",cursor.rowcount)
cursor.close()
conn.commit()


cursor = conn.cursor()
cursor.execute('select * from tb_businessshop where businessshop_id= %s', ('56',))
values = cursor.fetchall()
print ("56shop:",values)

cursor.close()


cursor = conn.cursor()
#批量执行插入
cursor.executemany('insert into tb_businessshop (businessshop_id, c_name,c_address,c_city) values (%s, %s,%s,%s)', [('60', '测试名称','天津福建路下瓦房','天津河西区'),('61', '测试名称','天津福建路下瓦房','天津河西区')])


cursor.close()
conn.commit()


conn.close() 