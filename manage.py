from flask_migrate import MigrateCommand
from flask_script import Server
from application import manage, app
# 导入数据模型
from models import *
# 导入视图
import www

# 运行服务器命令扩展
manage.add_command('runserver', Server(port=app.config['SERVERPORT'], use_debugger=True, use_reloader=True))
# 数据库操作命令
manage.add_command('db', MigrateCommand)


def main():
    manage.run()


if __name__ == '__main__':
    try:
        import sys

        sys.exit(main())  # 以main()的结束状态码作为退出码
    except Exception as e:
        # 要是服务器炸了，输出信息
        import traceback

        traceback.print_exc()
