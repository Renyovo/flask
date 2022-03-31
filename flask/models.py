#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@Time: 2022/3/24 15:52
@Author: y
@QQ: 77386059
@Wechat: Reny-ovo-
@Description：数据库模型
"""
from exts import db
from datetime import datetime


# # 1.添加数据
# # insert table article value(xx)
# article = Article(title="qwe", content="rty")
# db.session.add(article)
# # 做一个提交操作
# db.session.commit()

# # 2. 查询数据
# # filter_by: 返回一个类列表的对象
# article = Article.query.filter_by(id=1)[0]
# print(article.title)

# # 3. 修改数据
# article = Article.query.filter_by(id=1)[0]
# article.content = "uio"
# db.session.commit()

# # 4. 删除操作
# Article.query.filter_by(id=1).delete()
# db.session.commit()

class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    captcha = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)
    # db.backref
    # 1. 在反向引用的时候，如果需要引用一些其他的参数，那么就需要用到这个函数，否则不需要使用，只要在relationship的backref的参数上，设置反向引用的名称就可以了。
    # 2. uselist=False：代表反向引用的时候，不是一个列表，而是一个对象。
    # user = db.relationship("User", backref=db.backref("extension", uselist=False))


class QuestionModel(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 外键
    # 1. 外键的数据类型一定要看，所引用的字段的类型
    # 2. db.ForeignKey("表名.字段名")
    # 3. 外键是属于数据库层面的，不推荐直接在ORM中使用
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # relationship:
    # 1. 第一个参数是模型的名字，必须要和模型的名字保持一致
    # 2. backref(back reference):代表反向引用,代表对方访问我的时候的字段名称
    author = db.relationship("UserModel", backref="question")


class AnswerModel(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    question = db.relationship("QuestionModel", backref=db.backref("answers", order_by=create_time.desc()))
    author = db.relationship("UserModel", backref="answers")

# ORM迁移数据库的版本管理就不需要用到以下命令
# db.drop_all()  # 删除所有表
# db.create_all()  # 创建所有表
