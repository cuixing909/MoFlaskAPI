from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


class Application(Flask):
    def __init__(self, import_name):
        # 使用父类初始化
        super(Application, self).__init__(import_name)
        # 加载配置文件
        self.config.from_pyfile('config/base_settings.py')
        # 绑定app配置到db self就是app
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__)
# 使用flask_script对app进行扩展命令
manage = Manager(app)
# 封装数据库迁移对象
migrate = Migrate(app, db)

