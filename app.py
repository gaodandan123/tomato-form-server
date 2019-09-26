#!/usr/bin/env python
# coding:utf-8
from flask import Flask
from flask import jsonify

app = Flask(__name__)
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from config import DB_URI
from utilitys.sqlalchemy.models import UsersModule

db = sqlalchemy.create_engine(DB_URI)
cursor = sessionmaker(bind=db)  # 得到的是一个类


@app.route('/hello_world')
def hello_world():
    session = cursor()  # 实例
    # 查询一条数据
    one_data = session.query(UsersModule).filter_by(password='333333').first()
    print("id:%s，name:%s，password:%s" % (one_data.id, one_data.name, one_data.password))
    # 释放数据库连接
    session.close()
    data = {
        'code': 0,
        'data': 'hello world',
        'message': '成功'
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
