#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@Time: 2022/3/30 09:41
@Author: y
@QQ: 77386059
@Wechat: Reny-ovo-
@Description：验证是否登录的装饰器
"""
from flask import g, redirect, url_for
from functools import wraps


def login_required(func):
    # 这个装饰器一定不能忘记写
    @wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(g, "user"):
            return func(*args, **kwargs)
        else:
            return redirect(url_for("user.login"))
    return wrapper
