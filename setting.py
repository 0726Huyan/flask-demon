from flask import Config


class MysqlConfig(Config):
    #配置数据库信息
    #CACHE_TYPE='simple'
    SQLALCHEMY_DATABASE_URI= "mysql+pymysql://root:123456@localhost/flaskweb"
    #配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动

    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS= True
    SQLALCHEMY_COMMIT_ON_TEARDOWN= True

    SECRET_KEY= 'top-secret!'

    # Flask-Mail configuration
    MAIL_SERVER= "smtp.qq.com"
    MAIL_PORT= "587"
    MAIL_USE_TLS= True
    MAIL_USERNAME = "1213606635@qq.com"
    MAIL_PASSWORD = "edstgpchvimvfhdc"
    MAIL_DEFAULT_SENDER = "1213606635@qq.com"

    # Celery configuration
    CELERY_BROKER_URL= 'redis://127.0.0.1:6379/0'
    CELERY_RESULT_BACKEND= 'redis://127.0.0.1:6379/0'

    # Initialize extensionsc
    CACHE_TYPE='redis'
    CACHE_REDIS_HOST='localhost'
    CACHE_REDIS_PORT='6379'
    CACHE_REDIS_PASSWORD='password'
    CACHE_REDIS_DB = '0'
class ProdConfig(Config):
    pass
class DevConfig(Config):
    pass