from flask import (
    Blueprint,
    render_template,
)

from routes import (
    login_required,
)

todo_view = Blueprint('todo_view', __name__)


@todo_view.route('/todo/index', methods=['GET'])
@login_required
def index():
    """
    主页的处理函数, 返回主页的响应
    """
    return render_template('todo_index.html')