import time

from flask import Blueprint, jsonify, session, request

# 创建蓝图对象
from application import db
from models import Tag, Admin, Message

admin_op = Blueprint('admin_op', __name__)


@admin_op.route('/tags', methods=['GET'])
def tags():
    """
    标签列表
    :return:
    """
    tag_list = Tag.query.all()
    tag_list = [
        {
            'id': t.id,
            'name': t.name,
            'admin_name': t.admin.name,
            'create_time': t.create_time.strftime('%Y-%m-%d %X')
        }
        for t in tag_list]
    return jsonify(code=200, msg='获取所有标签成功', tags=tag_list)


@admin_op.route('/tags/add', methods=['POST'])
def tags_add():
    """
    增加标签标签
    :return:
    """
    admin_id = session.get('admin_id')
    name = request.json.get('name')
    if all([admin_id, name]):
        db_tag = Tag.query.filter_by(name=name).first()

        if db_tag:
            return jsonify(code=400, msg='标签已存在！')

        tag = Tag(name=name)
        tag.admin = Admin.query.filter_by(id=admin_id).first()
        try:
            db.session.add(tag)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify(code=500, msg='创建标签失败!')
        return jsonify(code=201, msg='创建标签成功!')
    else:
        return jsonify(code=400, msg='参数不完整!')


@admin_op.route('/tags/<int:id>', methods=['DELETE'])
def tags_op(id):
    """
    标签操作
    :return:
    """
    admin_id = session.get('admin_id')
    if not all([admin_id, id]):
        return jsonify(code=400, msg='参数不完整')
    try:
        tag = Tag.query.filter_by(id=id).first()
        if tag:
            db.session.delete(tag)
            db.session.commit()
        else:
            return jsonify(code=400, msg='要删除的标签不存在!')
    except Exception as e:
        db.session.rollback()
        return jsonify(code=500, msg='删除标签失败!')
    return jsonify(code=201, msg='删除标签成功!')


@admin_op.route('/messages', methods=['GET'])
def messages():
    """
    信息列表
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


@admin_op.route('/messages/<id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def messages_op(id):
    """
    信息操作
    :return:
    """
    admin_id = session.get('admin_id')
    if not all([id, admin_id]):
        return jsonify(code=400, msg="参数不完整")
    message = Message.query.filter_by(id=id).first()
    if message:
        if request.method == 'GET':
            return jsonify(code=200, msg='success!',
                           message={'id': message.id, 'content': message.content, 'author': message.user.name,
                                    'create_time': message.create_time})
        elif request.method == 'DELETE':
            try:
                db.session.delete(message)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify(code=500, msg='删除失败!')
            return jsonify(code=200, msg='删除成功!')
    else:
        return jsonify(code=400, msg='找不到一个id={}的留言!'.format(id))
