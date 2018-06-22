#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

# 打开数据库 （如果连接失败会报错）
# db = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'minbo', passwd = '123456', db = 'pythontest')
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='tao123456', db='dtest', charset="utf8")


# 获取游标对象
cursor = db.cursor()

# 执行sql查询操作
sql_select = "select version()"
cursor.execute(sql_select)

# 使用fetchone()获取单条数据
data = cursor.fetchone()
print("DB version is : %s" % data)

# 如果user表存在，就删除
cursor.execute("drop table if exists user")

# 创建表user
sql_create = "create table user(id int, name varchar(10)) engine = innodb charset = utf8"
cursor.execute(sql_create)

# 插入操作
sql_insert = '''insert into user(id, name) values (2, "李明")'''
try:
    # 执行sql
    cursor.execute(sql_insert)
    db.commit()
except:
    # 发生异常
    db.rollback()

# 查询操作
sql_select = '''select * from user'''
try:
    # 执行sql语句
    cursor.execute(sql_select)
    # 获取所有记录列表
    result = cursor.fetchall()
    for row in result:
        id = row[0]
        name = row[1]
        print("id = %d, name = %s" % (id, name))
except:
    print("Error: unable to fecth data")

# 执行事务
# 例子
sql_insert = '''insert into test(id, name) values (1, 'china')'''
try:
    cursor.execute(sql_insert)
    db.commit()
except:
    db.rollback()

print("end")
# 关闭连接
db.close()
