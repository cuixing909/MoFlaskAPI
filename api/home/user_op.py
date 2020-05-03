import traceback

from flask import Blueprint, jsonify, session, request

# 创建蓝图对象
from application import db
from models import User, Message, Tag

user_op = Blueprint('user_op', __name__)


@user_op.route('/messages', methods=['GET'])
def messages():
    """
    全部信息列表
    :return:
    """
    message_list = Message.query.order_by(db.desc('create_time')).all()
    message_list = [
        {
            'id': m.id,
            'content': m.content,
            'user_name': m.user.name,
            'tags': [t.name for t in m.tags],
            'create_time': m.create_time.strftime('%Y-%m-%d %X')
        }
        for m in message_list]
    return jsonify(code=200, msg='获取全部信息列表成功！', messages=message_list, total=len(message_list))


@user_op.route('/messages/history', methods=['GET'])
def messages_history():
    """
    用户个人历史信息列表
    :return:
    """
    user_id = session.get('user_id')
    if user_id:
        message_list = Message.query.filter_by(user_id=user_id).order_by(db.desc('create_time')).all()
        message_list = [
            {'id': m.id, 'content': m.content, 'user_name': m.user.name, 'tags': [t.name for t in m.tags],
             'create_time': m.create_time.strftime('%Y-%m-%d %X')}
            for m in message_list]
        return jsonify(code=200, msg='获取个人历史留言成功！', messages=message_list, total=len(message_list))
    else:
        return jsonify(code=400, msg='请先登录！')


@user_op.route('/messages/add', methods=['POST'])
def messages_add():
    """
    信息列表
    :return:
    """
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter_by(id=user_id).first()
        content = request.json.get('content')
        tags = request.json.get('tags')

        tags = Tag.query.filter(Tag.name.in_(tags)).all()
        if all([content, tags]):
            message = Message(content=content, user_id=user_id)
            message.user = user

            for t in tags:
                message.tags.append(t)

            try:
                db.session.add(message)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                traceback.print_exc()
                return jsonify(code=500, msg='发布留言失败')
        else:
            return jsonify(code=400, msg='参数不完整')
        return jsonify(code=201, msg='发布留言成功!')
    else:
        return jsonify(code=400, msg='请先登录!')


@user_op.route('/messages/<int:id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def messages_op(id):
    """
    用户获取一条信息
    删除一个信息
    修改一个信息（给信息增加标签）
    :return:
    """
    user_id = session.get('user_id')
    if not all([id, user_id]):
        return jsonify(code=400, msg="参数不完整")
    message = Message.query.filter_by(id=id).first()
    if message:
        if request.method == 'GET':
            return jsonify(code=200, msg='success!',
                           message={'id': message.id, 'content': message.content, 'author': message.user.name,
                                    'create_time': message.create_time})
        elif request.method == 'DELETE':
            if user_id != message.user_id:
                return jsonify(code='400', msg='不能删除别人的留言！')

            try:
                db.session.delete(message)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify(code=500, msg='删除失败!')
            return jsonify(code=200, msg='删除成功!')
        elif request.method == 'PUT':
            tags = request.json.get('tags')
            tags = Tag.query.filter(Tag.name.in_(tags)).all()
            if not tags:
                return jsonify(code=400, msg='找不到标签!')
            try:
                message.tags.append(tags)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify(code=500, msg='增加标签失败!')
            return jsonify(code=200, msg='增加标签成功!')
    else:
        return jsonify(code=400, msg='找不到一个id={}的留言!'.format(id))
