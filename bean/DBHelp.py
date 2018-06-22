#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql

from bean.BaseResult import BaseResult


class DBHelp(object):
    creatUser = '''create table usertest(
id int auto_increment primary key,
name varchar(50),
sex varchar(20),
phone varchar(50),
password varchar(100)
)default charset=utf8'''

    def __init__(self):
        self.db = pymysql.connect(host='localhost', port=3306, user='root', passwd='tao123456', db='dtest',
                                  charset="utf8")
        self.cursor = self.db.cursor();

    def getData(self, phone="test", password="test", ):
        data = {}
        baseResult = BaseResult()
        # baseResult = {}
        # 查询操作
        # sql_select = '''select * from usertest'''
        # sql_select = "SELECT `phone`,`password` FROM `usertest`WHERE `phone`='张三'"
        sql_select = "select * from usertest where phone='%s' and password='%s'" % (phone, password)
        try:
            # 执行sql语句
            self.cursor.execute(sql_select)
            # 获取所有记录列表
            result = self.cursor.fetchmany(1)
            for row in result:
                id = row[0]
                name = row[1]
                sex = row[2]
                phone = row[3]
                password = row[3]
                data['id'] = id
                data['name'] = name
                data['sex'] = sex
                data['phone'] = phone
                data['password'] = password
                baseResult.code = 200
                baseResult.message = "成功"
                baseResult.data = data
                print("id = %d, name = %s" % (id, name))
        except:
            print("Error: unable to fecth data")

        if result.__len__() == 0:
            baseResult.code = 201
            baseResult.message = "失败,用户不存在或者密码错误"
        try:
            self.db.commit()
        except:
            self.db.rollback()

        return baseResult

    def closeDB(self):
        print("endcloseDB")
        # 关闭连接
        self.db.close()

    def createTable(self):
        self.cursor.execute(self.creatUser)
        try:
            # 执行sql
            self.db.commit()
        except:
            # 发生异常
            self.db.rollback()
        print("createTable")

    def insertData(self):
        # 插入操作
        sql_insert = '''insert into usertest(name, sex, phone, password) values ("zhoutao","男","13072178888","123456")'''
        try:
            # 执行sql
            self.cursor.execute(sql_insert)
            self.db.commit()
        except:
            # 发生异常
            self.db.rollback()
        print("insertData")

    def __del__(self):
        print("enddel")
        # 关闭连接
        self.db.close()
