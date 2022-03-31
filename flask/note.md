# 模版笔记

## 一、基本使用
1. 模版文件，也就是html文件，需要放到templates文件夹下，当然在
`Flask(__name__,template_folder)`来修改模版的地址，但是不推荐。
2. 通过`render_template`来渲染模版。
3. 如果想要传递变量到模版中，那么可以把变量定义成字典，然后在
`render_template`中，通过关键字参数的方式传递过去，`render_template('',**contest)`。


# Flask-SQLAlchemy笔记

## 一、SQLAlchemy和Flask_SQLAlchemy的区别：
1. SQLAlchemy：是一个独立的ORM框架，可以独立于Flask存在，也可以在其他项目中使用，比如在Django中
2. Flask-SQLAlchemy：对SQLAlechemy的一个封装，能够更适合在flask中使用


## 一、安装和验证
1. 安装： pip install flask-sqlalchemy
2. 安装连接数据库的库： pip install pymysql

## 二、连接数据库
```python
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'xt_flask'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
```


# Flask-Migrate插件

在实际的开发环境中，经常会发生数据库修改的行为。一般我们修改数据库不会直接手动的去修改，而是去修改ORM对应的模型，然后再把模型映射到数据库中。
这时候如果有一个工具能专门做这种事情，就显得非常有用了，而flask-migrate就是做这个事情的。flask-migrate是基于Alembic进行的一个封装，
并集成到Flask中，而所有的迁移操作其实都是Alembic做的，他能跟踪模型的变化，并将变化映射到数据库中。

使用Flask-Migrate需要安装，命令如下：
pip install flask-migrate


## 使用
要让Flask-Migrate能够管理app中的数据库，需要使用Migrate(app,db)来绑定app和数据库。
首先需要初始化一个迁移文件夹：flask db init
然后再把当前的模型添加到迁移文件中：flask db migrate
可以加参数-m "xxx" 表示备注更新了什么信息

最后再把迁移文件中对应的数据库操作，真正的映射到数据库中：flask db upgrade