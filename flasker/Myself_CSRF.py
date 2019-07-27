from wtforms.csrf.core import CSRF
from hashlib import md5
SECRET_KEY='111111'  # 可写入配置文件中 通过 app.config[xxx]调用
class Myself_CSRF(CSRF):
    def setup_form(self, form):
        self.csrf_context=form.meta.csrf_secret
        return super(Myself_CSRF, self).setup_form(form)
    def generate_csrf_token(self, csrf_token_field):
        token=md5(SECRET_KEY+self.csrf_secret).hexdigest() #通过KEY值和传入的csrf_secret值生成TOKEN
        return token
    def validate_csrf_token(self, form, field):
        if field.data != field.current_token:
            raise ValueError('Invalid CSRF') #检测两次TOKEN是否一致

from flask_wtf import FlaskForm
class Form_Token(FlaskForm):
    class Meta:
        csrf=True
        csrf_class=Myself_CSRF
        csrf_secret=None   #继承时自行定义