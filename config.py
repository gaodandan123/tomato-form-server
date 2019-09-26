#!/usr/bin/env python
#coding:utf-8

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'dandan'
USERNAME = 'root'
PASSWORD = 'password'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
