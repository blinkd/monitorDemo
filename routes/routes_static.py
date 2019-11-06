from flask import (
    Blueprint,
    render_template,
    request,
    send_from_directory)

from routes import current_user, login_required
from utils import log

static_view = Blueprint('static_view', __name__)


@static_view.route('/')
@login_required
def route_index():
    """
    主页的处理函数, 返回主页的响应
    """
    u = current_user()
    log('current user', u)
    return render_template('index.html', username=u.username)


@static_view.route('/static')
def route_static():
    """
    静态资源的处理函数, 读取静态文件并生成响应返回
    """
    filename = request.args.get('file', None)
    return send_from_directory('static', filename)