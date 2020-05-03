import os

USER = 'root'
PASSWORD = '111111'
HOSTNAME = '127.0.0.1'
DB = 'lmdb'
# 数据库信息地址
DB_URL = 'mysql+pymysql://{}:{}@{}/{}'.format(USER, PASSWORD, HOSTNAME, DB)
# 连接配置
SQLALCHEMY_DATABASE_URI = DB_URL
# sql修改跟踪
SQLALCHEMY_TRACK_MODIFICATIONS = True
#
SQLALCHEMY_MODIFICATIONS = True
# 当操作数据库时输出SQL语句
SQLALCHEMY_ECHO = False
# 设置编码
SQLALCHEMY_ENCODING = 'utf-8'
# 启动调试
DEBUG = True
# 服务器端口
SERVERPORT = 9999
# 安全key
SECRET_KEY = os.urandom(24)
