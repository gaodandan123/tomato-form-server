#!/usr/bin/env python
#coding:utf-8

import pymysql
pymysql.install_as_MySQLdb()

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from config import DB_URI

db=sqlalchemy.create_engine(DB_URI)
base = declarative_base(db)

class UsersModule(base):
    __tablename__ = "test_users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))
    password = sqlalchemy.Column(sqlalchemy.String(32))


if __name__ == "__main__":
    #创建表
    base.metadata.create_all(db)
