#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/6/29
# ---------------------------------
# Comment: 主要功能说明

import MySQLdb

try:
    conn=MySQLdb.connect(host='192.168.8.94',user='mha_user',passwd='gc895316',db='wwn',port=3306)
    cur=conn.cursor()
    cur.execute('select * from a')
    data = cur.fetchall()
    print data
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])