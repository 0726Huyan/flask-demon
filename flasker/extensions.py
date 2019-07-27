
#from flask_bcrypt import Bcrypt
#from flask_openid import OpenID
#from flask_oauth import OAuth
#from flask_login import LoginManager
#from flask_principal import Principal,Permission,RoleNeed
#from flask_restful import Api
#from flask_debugtoolbar import DebugToolbarExtension
#from setting import MysqlConfig

#oid = OpenID()
#oauth = OAuth()
#principals = Principal()
#debug_toolbar = DebugToolbarExtension()
#flask_bcrypt = Bcrypt()
#login_Manager = LoginManager()
#rest_api = Api()
#from flask_cache import Cache
#cache = Cache()
from flask import (
    redirect,
    url_for,
    session,
    render_template,
    Blueprint,
    Markup
)
class Youtube(object):
    def __init__(self,app=None,**kwargs):
        if app:
            self.init_app(app)
    def init_app(self,app):
            self.register_blueprint(app)

            app.add_template_global(youtube)
            app.add_template_global(test1)
    def register_blueprint(self,app):
        module = Blueprint(
                'youtube',
                __name__,
                template_folder="templates"
            )
        app.register_blueprint(module)
        return module
class Video(object):
    def __init__(self,video_id,cls="youtube"):
        self.video = video_id
        self.cls = cls
    def render(self,*args,**kwargs):
        return render_template(*args,**kwargs)
    @property
    def html(self):
        return Markup(
            render_template('video.html',video=self)
        )
def youtube(id):

    video = Video(video_id=id)
    return video.html

def test1():
    return "1"