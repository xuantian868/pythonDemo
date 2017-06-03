# -*- coding: utf-8 -*-
'''
Created on 2017-6-3
获取查询数据
@author: Administrator
'''

import pymysql


#创建连接
conn = pymysql.connect(host='127.0.0.1', port=3308, user='root', passwd='lihlsereb', db='carshop', charset='utf8')
# 创建游标
cursor = conn.cursor()

#执行sql，并返回影响行数
effect_row = cursor.execute("select * from tb_businessshop")

# 获取剩余结果的第一行数据
row1 = cursor.fetchone()
print ("第一行数据:",row1) #第一行数据: ('56', '测试名称', '天津福建路下瓦房', '天津河西区', None, None, None, None, None, None, None)

# 获取剩余结果前n行数据, 因为上面执行获取第一行数据游标已经下移，所以会取第二条，第三，第四条3条数据
row_2 = cursor.fetchmany(3)
print ("前3行数据:",row_2)
# 获取剩余结果所有数据
row_3 = cursor.fetchall()
for shop in row_3:
    print ("shop:" ,shop)
#print ("剩余数据:",row_3)


cursor.close()
 
cursor = conn.cursor()
#游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute("select * from tb_businessshop")
 
row_1 = cursor.fetchone()
print ("将游标设置为字典后:",row_1) #将游标设置为字典后:{'C_ADDRESS': '天津福建路下瓦房', 'C_CITYAREA': None, 'C_YYTIME': None, 'C_BUSINESSAREA': None, 'C_GONGWEI': None, 'C_CITY': '天津河西区', 'C_CONTENT': None, 'C_XY': None, 'C_NAME': '测试名称', 'BUSINESSSHOP_ID': '56', 'C_PHONE': None}

cursor.close()


cursor = conn.cursor()
phone = '123'
shop_id = '950013686'
row_count=cursor.execute("update tb_businessshop set c_phone=%s where  businessshop_id=%s",(phone,shop_id))
#cursor.executemany("update tb_businessshop set c_phone='123' where id='950013686'")  

cursor.close()
conn.commit()
conn.close() 