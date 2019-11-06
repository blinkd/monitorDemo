from flask import (
    Blueprint,
    render_template,
    make_response,
    redirect,
    request,

)
from models.session import Session
from routes import (
    random_str,
)
from utils import log
from models.user import User

user_view = Blueprint('user_view', __name__)


@user_view.route('/login', methods=['GET', 'POST'])
def route_login():
    """
    登录页面的路由函数
    """
    log('login, cookies', request.cookies)
    if request.method == 'POST':
        form = request.form
        u = User(form)
        if u.validate_login():
            session_id = random_str()
            u = User.find_by(username=u.username)
            s = Session.new(dict(
                session_id=session_id,
                user_id=u.id,
            ))
            log('session', s)
            # 登录后定向到 /
            redirect_to_index = redirect('/')
            response = make_response(redirect_to_index)
            response.set_cookie('sid', value=session_id)
            return response
    # 显示登录页面
    return render_template('login.html')


@user_view.route('/register', methods=['GET', 'POST'])
def route_register():
    """
    注册页面的路由函数
    """
    if request.method == 'POST':
        form = request.form
        u = User.new(form)
        if u.validate_register():
            # 注册成功再保存
            u.save()
            # 注册成功后 定向到登录页面
            return redirect('/login')
        else:
            # 注册失败 定向到注册页面
            return redirect('/register')
    # 显示注册页面
    return render_template('register.html')
