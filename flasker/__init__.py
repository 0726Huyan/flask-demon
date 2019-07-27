from celery import Celery
from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .extensions import Video,Youtube
from flask_mail import Mail
from setting import MysqlConfig
#from .extensions import cache
csrf = CSRFProtect()
youtube_ext=Youtube()
mail = Mail()
db = SQLAlchemy()
celery = Celery(
    __name__,
    broker=MysqlConfig.CELERY_BROKER_URL,
    backend=MysqlConfig.CELERY_RESULT_BACKEND
)
def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)
    youtube_ext.init_app(app)
    #cache.init_app(app)
    celery.conf.update(app.config)
    @app.route('/')
    def first_html():
        return render_template('base.html')
    from .Controllers.auth import bp
    app.register_blueprint(blueprint=bp)
    return app
