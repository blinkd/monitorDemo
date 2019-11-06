from flask import (
    Flask,
)


from routes.routes_user import user_view
from routes.routes_static import static_view
from routes.routes_todo import todo_view
from routes.api_todo import todo_api
from job.jobs import *


app = Flask(__name__)
app.register_blueprint(user_view)
app.register_blueprint(static_view)
app.register_blueprint(todo_view)
app.register_blueprint(todo_api)





if __name__ == '__main__':
    app.config.from_object(Config())
    # 定时任务启动
    scheduler.init_app(app)
    scheduler.start()

    # 生成配置并且运行程序
    config = dict(
        debug=True,
        host='127.0.0.1',
        port=3000,
    )
    app.run(**config)
