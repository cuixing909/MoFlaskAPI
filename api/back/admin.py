import json
import traceback

from flask import Blueprint, jsonify, request, session, redirect, url_for

from application import db
from models import Admin

# 创建蓝图对象
admin = Blueprint('admin', __name__)


@admin.route('/login', methods=['POST'])
def login():
    """
    登录
    :return:
    """
    name = request.json.get('name')
    password = request.json.get('password')
    if not all([name, password]):
        return jsonify(code=400, msg='参数不完整!')

    adm = Admin.query.filter_by(name=name).first()
    if adm and adm.password == password:
        # 保存信息到服务器session
        session['admin_id'] = adm.id
        return jsonify(code=200, msg='登录成功!')
    else:
        return jsonify(code=400, msg='登录失败!密码或账号错误')


@admin.route('/register', methods=['POST'])
def register():
    """
    注册管理员账号
    :return:
    """
    name = request.json.get('name')
    password = request.json.get('password')
    adm = Admin.query.filter_by(name=name).first()
    if not adm:
        new_admin = Admin(name=name, password=password)
        try:
            db.session.add(new_admin)
            db.session.commit()
            return jsonify(code=201, msg='注册成功!',
                           admin={'name': new_admin.name, 'password': new_admin.password})
        except Exception as e:
            traceback.print_exc()
            db.session.rollback()
            return jsonify(code=500, msg='注册失败!')
    else:
        return jsonify(code=400, msg='用户名已存在！', admin={'name': adm.name, 'password': adm.password})


@admin.route('/logout')
def logout():
    """
    退出登录
    :return:
    """
    if session.get('admin_id'):
        # 三种方式都可以删除session里面的键
        # session.pop('admin_id')
        # del session['admin_id']
        session.clear()
        # 退出登录后 重定向到欢迎
        # return redirect(url_for('home.index'))
        return jsonify(code=200, msg='退出登录成功!')
    else:
        return jsonify(code=500, msg='未登录，不能进行退出登录操作!')
