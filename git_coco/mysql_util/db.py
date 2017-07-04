#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/6/29
# ---------------------------------
# Comment: 主要功能说明

import MySQLdb


# 创建数据库表
def create_table():
    sql = 'create table bb(id int ,name varchar(20),class varchar(30),age varchar(10));'
    cur = conn.cursor()
    cur.execute(sql)
    cur.close()
    conn.commit()


def insert_table():
    # sql = "insert into bb values ('2','Tom','3 year 2 class','9'));"
    cur = conn.cursor()
    # print sql
    cur.execute("insert into bb values ('2','Tom','3 year 2 class','9');")
    cur.close()
    conn.commit()

def select_table():
    sql = "select * from bb;"
    cur=conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    print data



try:
    conn=MySQLdb.connect(host='192.168.8.94',user='mha_user',passwd='gc895316',db='wwn',port=3306)
    create_table()
    insert_table()
    select_table()

except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])




