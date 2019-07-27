from flasker import celery, create_app
from setting import MysqlConfig
app = create_app(MysqlConfig)
app.app_context().push()