#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@Time: 2022/3/24 13:12
@Author: y
@QQ: 77386059
@Wechat: Reny-ovo-
@Description：配置文件
"""
# 数据库配置
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'flask_2'
USERNAME = 'root'
PASSWORD = 'Ry990910'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "qwertyuiop123"


# 邮箱配置
# 项目中使用QQ邮箱
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "1838521691@qq.com"
MAIL_PASSWORD = "hfksunaphmlqfdga"
MAIL_DEFAULT_SENDER = "1838521691@qq.com"
