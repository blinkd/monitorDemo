import time
from datetime import datetime
import logging
from jinja2 import Environment, FileSystemLoader


def log(*args, **kwargs):
    # time.time() 返回 unix time
    format = '%H:%M:%S'
    value = time.localtime(int(time.time()))
    # 1500057448 -> 7:38:38
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)
    # a append 追加模式
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def logger():
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)


# 得到用于加载模板的目录
# path = '{}/templates/'.format(os.path.dirname(__file__))
path = 'templates'
loader = FileSystemLoader(path)
env = Environment(loader=loader)


def template(path, **kwargs):
    """
    本函数接受一个路径和一系列参数
    读取模板并渲染返回
    """
    t = env.get_template(path)
    return t.render(**kwargs)


def formatted_time(unixtime):
    dt = time.localtime(unixtime)
    ds = time.strftime('%Y-%m-%d %H:%M:%S', dt)
    return ds
