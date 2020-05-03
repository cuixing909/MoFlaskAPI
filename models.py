from datetime import datetime

from application import db


class Admin(db.Model):
    """
    管理员表
    """
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)


class User(db.Model):
    """
    用户表
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)


class Tag(db.Model):
    """
    标签表
    一对多：管理员1 -> 标签多
    """
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    admin = db.relationship('Admin', backref=db.backref('tags'))


class Message(db.Model):
    """
    信息表
    一对多：用户1 -> 信息多
    """
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 在其中一个表写即可
    tags = db.relationship('Tag', secondary='message_to_tag', backref=db.backref('messages'))
    user = db.relationship('User', backref=db.backref('messages'))


class MessageToTag(db.Model):
    """
    中间表
    多对多：
    """
    __tablename__ = 'message_to_tag'
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
