import traceback

from flask import Blueprint, jsonify, request, session, redirect, url_for

# 创建蓝图对象
from application import db
from models import User

user = Blueprint('user', __name__)


@user.route('/login', methods=['POST'])
def login():
    """
    登录
    :return:
    """
    name = request.json.get('name')
    password = request.json.get('password')
    if not all([name, password]):
        return jsonify(code=400, msg='参数不完整!')

    us = User.query.filter_by(name=name).first()
    if us and us.password == password:
        # 保存信息到服务器session
        session['user_id'] = us.id
        return jsonify(code=200, msg='登录成功!')
    else:
        return jsonify(code=400, msg='登录失败!密码或账号错误')


@user.route('/register', methods=['POST'])
def register():
    """
    注册账号
    :return:
    """
    name = request.json.get('name')
    password = request.json.get('password')
    us = User.query.filter_by(name=name).first()
    if not us:
        new_user = User(name=name, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return jsonify(code=201, msg='注册成功!',
                           admin={'name': new_user.name, 'password': new_user.password})
        except Exception as e:
            traceback.print_exc()
            db.session.rollback()
            return jsonify(code=500, msg='注册失败!')
    else:
        return jsonify(code=400, msg='用户名已存在！', admin={'name': us.name, 'password': us.password})


@user.route('/logout')
def logout():
    """
    退出登录
    :return:
    """
    if session.get('user_id'):
        # 三种方式都可以首次session里面的键
        # session.pop('admin_id')
        # del session['admin_id']
        session.clear()
        # 退出登录后 重定向到欢迎
        # return redirect(url_for('home.index'))
        return jsonify(code=200, msg='退出登录成功!')
    else:
        return jsonify(code=400, msg='未登录，不能进行退出登录操作!')

