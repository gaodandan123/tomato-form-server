#!/usr/bin/env python
#coding:utf-8

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from config import DB_URI
from utilitys.sqlalchemy.models import UsersModule


db=sqlalchemy.create_engine(DB_URI)
cursor = sessionmaker(bind=db)  # 得到的是一个类
session = cursor()  # 实例

'''
#①插入一条数据
user = UsersModule(
    id = 1,
    name = "张1",
    password = '111111'
)
session.add(user)
session.commit()

#②同时插入多条数据
session.add_all([
    UsersModule(id=2,name="张2",password='222222'),
    UsersModule(id=3,name="张3",password='333333')
])
session.commit()

#①查询所有数据
all_data = session.query(UsersModule).all() #得到的是一个可迭代对象
for data in all_data:
    print("id:%s，name:%s，password:%s"%(data.id,data.name,data.password))

#②根据条件查询多条数据
many_data = session.query(UsersModule).filter_by(password='333333').all()
print(many_data)#实际是一个sql查询语句，其还是一个存储一个对象的带迭代内容
for data in many_data:
    print("id:%s，name:%s，password:%s"%(data.id,data.name,data.password))
'''
#查询一条数据
one_data = session.query(UsersModule).filter_by(password='333333').first()
print("id:%s，name:%s，password:%s"%(one_data.id,one_data.name,one_data.password))

'''
#10、删除
#先查询需要删除的数据
data = session.query(UsersModule).filter_by(password='333333').all()
#然后删除
for i in data:
    session.delete(i)
#然后提交操作
session.commit()


#11、修改
# 先查询需要修改的数据
data = session.query(UsersModule).get(ident=1)
#然后修改
data.name = "老李头"
#然后提交操作
session.commit()
'''
#释放数据库连接
session.close()


#more:
# https://www.cnblogs.com/tangpg/p/8528835.html
# https://www.cnblogs.com/shenckicc/p/6797990.html
# https://www.cnblogs.com/jingqi/p/8059673.html
