#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/7/4
# ---------------------------------
# Comment: 主要功能说明: python 操作hive

'''
    采用Hive和thrift方式连接数据库
'''


import sys
reload(sys)
sys.setdefaultencoding('utf8')

from pyhive.hive     import *


try:
    conn = connect('172.17.17.42',username='hadoop',port=7001)
    assert False
except Exception as e:
    cur = conn.cursor()

    ####创建表语句
    # cur.execute(''' create external table wwn_test2(`database` string,`table` string,`op_type` string,`timestamp` string,xid string,`commit` string,`data` map<string,string>,old map<string,string>) partitioned by(dt string ,`type` string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\u0003' COLLECTION ITEMS TERMINATED BY '\u0002' MAP KEYS TERMINATED BY ':' location '/kafkahdfs/statis-gctongji-binlog' ''')

    ###查询数据库表
    # cur.execute("show tables")

    ###查询表
    cur.execute('''select * from statis_5tongji_collect limit 3 ''')
    print cur.fetchall()


