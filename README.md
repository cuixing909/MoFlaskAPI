这是一个由flask开发实现的`留言`后端API，实现的接口包含登录、注册、注销、数据的增删改查。接口测试使用的工具是postman。

## 环境

python 3.6

flask

mysql



## 项目效果

![r1](https://github.com/sheppyy/MoFlaskAPI/blob/master/static/imgs/r1.PNG)

![r2](https://github.com/sheppyy/MoFlaskAPI/blob/master/static/imgs/r2.PNG)

![r3](https://github.com/sheppyy/MoFlaskAPI/blob/master/static/imgs/r3.PNG)

![r4](https://github.com/sheppyy/MoFlaskAPI/blob/master/static/imgs/r4.PNG)

![r5](https://github.com/sheppyy/MoFlaskAPI/blob/master/static/imgs/r5.PNG)

## 本项目，你可以

1. 学会使用Flask开发API

2. 蓝图的使用

3. 学会RESTful接口设计风格

4. postman的基本使用

5. 数据关联关系

6. SQLAlchemy的使用

   ...

## 项目开始

1. 创建虚拟环境
2. `pip install -r requirements.txt`
3. 将lmdb.sql导入自己的数据库
4. 配置config\base_settings.py文件，数据库连接改成自己的
5. 启动服务器，`python manage.py runserver`
6. 打开postman工具（没有可以到官[网下载](https://www.postman.com/)）,导入flask_api.postman_collection.json文件即可开始。



## 需求分析

1. 管理员

   登录、退出

   增删改查留信息

   增删查改标签



2. 用户

   登录、退出

   发送留言

   删除自己的留言

   查看自己历史留言



## 数据库分析

1. 管理员表

   - 账号

   - 密码

2. 用户表
   - 账号
   - 密码

3. 留言表
   - 内容
   - 标签
   - 发布者
4. 标签表
   - 标签名称
   - 管理员（表示这个标签是哪个管理员创建的）

