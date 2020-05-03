import json

from flask import jsonify

from api.back.admin import admin
from api.back.admin_op import admin_op
from api.home.user import user
from api.home.user_op import user_op
from api.welcome import home
from application import app

# 注册蓝图
app.register_blueprint(home, url_prefix='/api')

app.register_blueprint(admin, url_prefix='/api/admin')
app.register_blueprint(admin_op, url_prefix='/api/admin/op')

app.register_blueprint(user, url_prefix='/api/user')
app.register_blueprint(user_op, url_prefix='/api/user/op')


# 自定义404处理
@app.errorhandler(404)
def handler_404(error):
    return jsonify({'msg': 'ops!', 'status': 404})
