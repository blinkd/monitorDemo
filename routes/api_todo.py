from flask import (
    Blueprint,
    jsonify,
    request,
)

from utils import log
from models.todo import Todo

todo_api = Blueprint('todo_api', __name__)


# 本文件只返回 json 格式的数据
# 而不是 html 格式的数据
@todo_api.route('/api/todo/all', methods=['GET'])
def all():
    todos = Todo.all_json()
    return jsonify(todos)


@todo_api.route('/api/todo/add', methods=['POST'])
def add():
    # 得到浏览器发送的表单, 浏览器用 ajax 发送 json 格式的数据过来
    # 新增加json 函数来获取格式化后的 json 数据
    form = request.json
    # 创建一个 todo
    t = Todo.new(form)
    return jsonify(t.json())


@todo_api.route('/api/todo/delete', methods=['GET'])
def delete():
    todo_id = int(request.args.get('id', None))
    t = Todo.delete(todo_id)
    return jsonify(t.json())


@todo_api.route('/api/todo/update', methods=['POST'])
def update():
    form = request.json
    log('api todo update', form)
    todo_id = int(form.get('id', None))
    t = Todo.update(todo_id, form)
    return jsonify(t.json())