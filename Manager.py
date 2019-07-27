
from flask_script import Manager,Server
from flasker import create_app
from setting import MysqlConfig
app = create_app(MysqlConfig)
manager = Manager(app)
manager.add_command('server',Server())
@manager.command
def make_shell_context():
    return dict(app=app)
if __name__ == "__main__":
    manager.run()