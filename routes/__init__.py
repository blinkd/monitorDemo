import json

from flask import (
    request,
    redirect,
)

from models.session import Session
from models.todo import Todo
from utils import log
from models.user import User

import random


def random_str():
    """
    生成一个随机的字符串
    """
    seed = 'bdjsdlkgjsklgelgjelgjsegker234252542342525g'
    s = ''
    for i in range(16):
        # 这里 len(seed) - 2 是因为我懒得去翻文档来确定边界了
        random_index = random.randint(0, len(seed) - 2)
        s += seed[random_index]
    return s


def current_user():
    session_id = request.cookies.get('sid', '')
    sessions = Session.all()
    for s in sessions:
        if s.session_id == session_id:
            u = User.find_by(id=s.user_id)
            return u
    return None


def login_required(route_function):
    def f():
        u = current_user()
        if u is None:
            log('非登录用户')
            return redirect('/login')
        else:
            return route_function()

    return f