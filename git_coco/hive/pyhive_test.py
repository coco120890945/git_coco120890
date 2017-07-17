#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/7/11
# ---------------------------------
# Comment: 主要功能说明


import sys
reload(sys)
sys.setdefaultencoding('utf8')

from pyhive.presto import *

conn = connect('172.17.17.42',username='hadoop',port=9000)
cur = conn.cursor()


# 从搜索引擎来的pv占总pv的比例:
#  分子 每天的搜索量
# sql= "select count(*),dt from statis_gctongji_collect where dt>'20170701' and dt<'20170706' and info['event']='ready' and info['refer_se'] not in ('','工厂网产品搜索','工厂网企业搜索','工厂网移动产品搜索','工厂网移动企业搜索') group by dt order by dt "
# test
# sql = "select dt, info['refer_se'] from statis_gctongji_collect where dt>'20170701' and dt<'20170706' and info['event']='ready' limit 2 "
# 分母 每天的总pv量
# sql = "select count(*) as pv ,dt  from statis_gctongji_collect where dt>='20170701' and dt<='20170706'  and event='ready' group by dt order by dt "

# #综合分子分母sql：
# sql = "select a.refer_se_count/cast(b.pv as double) as refer_sv_lv , a.refer_se_count,b.pv, a.dt from (select count(*) as refer_se_count,dt from statis_gctongji_collect where dt>'20170701' and dt<'20170706' and info['event']='ready' and info['refer_se'] not in ('','工厂网产品搜索','工厂网企业搜索','工厂网移动产品搜索','工厂网移动企业搜索') group by dt ) a ,(select count(*) as pv ,dt  from statis_gctongji_collect where dt>='20170701' and dt<='20170706'  and event='ready' group by dt ) b  where a.dt=b.dt order by a.dt "

# 留存率：登录用户数/新增用户数*100%（一般统计周期为天）
# 如果是供应商：新增用户数：
# 新增用户数:
# sql= '''select count(*) as new_user_count ,date_format(from_unixtime(addtime),'%Y%m%d') as dt from mysql.gcsupplier.sup_user where addtime >1498838400 and state=1 group by date_format(from_unixtime(addtime),'%Y%m%d')  '''
# test
#sql = "select date_format(from_unixtime(addtime),'%Y%m%d') from  mysql.gcsupplier.sup_user where addtime >1498838400 and state=1 limit 2 "

# 登陆用户数：
# sql = ''' select count(distinct supid) as login_user_count , date_format(from_unixtime(logintime),'%Y%m%d') as dt from mysql.gcsupplier.sup_login_log where supid in (select supid from mysql.gcsupplier.sup_user where addtime >1498838400 and state=1 ) and logintime >1498838400  group by date_format(from_unixtime(logintime),'%Y%m%d') '''

# 留存率：分子分母组合sql
# sql = '''select a.login_user_count/cast(b.new_user_count as double) as lv ,a.login_user_count,b.new_user_count,a.dt from (select count(distinct supid) as login_user_count , date_format(from_unixtime(logintime),'%Y%m%d') as dt from mysql.gcsupplier.sup_login_log where supid in (select supid from mysql.gcsupplier.sup_user where addtime >1498838400 and state=1 ) and logintime >1498838400  group by date_format(from_unixtime(logintime),'%Y%m%d')) a, (select count(*) as new_user_count ,date_format(from_unixtime(addtime),'%Y%m%d') as dt from mysql.gcsupplier.sup_user where addtime >1498838400 and state=1 group by date_format(from_unixtime(addtime),'%Y%m%d'))b where a.dt =b.dt order by a.dt    '''

### 6月份浏览过点金台用户的supid
sql = ''' select split_part(info['active_super'],'\t',1), url_extract_path(info['url']) from statis_gctongji_collect where dt>='20170601' and dt<='20170631' and info['event']='ready' and url_extract_host(info['url'])='seller.gongchang.com' and url_extract_path(info['url'])='/dianjintai/' and info['active_super'] !=''  '''


cur.execute(sql)


# 得到的结果是一个容器。容器中不会转化字符编码,都是unicode编码  需要取出来才能显示汉字。如下 result中 取结果
# print  cur.fetchall()
result = cur.fetchall()
for i in result:
    # print i
    print  i[0] , i[1] ,i[2] ,i[3]

# result= cur.fetchall()
# for i in result:
#     print i[0]

