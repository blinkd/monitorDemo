from flask import (
    Blueprint,
    render_template,
    jsonify,
    request,
    redirect,
)
from models.todo import Todo
from routes import (
    login_required,
)
from utils import log

todo_view = Blueprint('todo_view', __name__)


@todo_view.route('/todo/index', methods=['GET'])
@login_required
def index():
    """
    主页的处理函数, 返回主页的响应
    """
    todos = Todo.all_json()
    return render_template('todo_index_render.html', todos = todos)


@todo_view.route('/todo/add', methods=['POST'])
def todo_add():
    form = request.form.to_dict()
    log("form", form)
    # 创建一个 todo
    Todo.new(form)
    return redirect('/newPageTodo')


@todo_view.route('/todo/delete', methods=['GET'])
def todo_delete():
    query = request.args.to_dict()
    log("query", query.get('id'))
    delete_ele = Todo.delete(query.get('id'))
    log("delete_ele", delete_ele)
    return redirect('/newPageTodo')


@todo_view.route('/newPageTodo')
def route_newpage():
    todos = Todo.all_json()
    return render_template('todoExtendRender.html', todos = todos)
