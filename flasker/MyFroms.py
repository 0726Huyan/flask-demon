from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,HiddenField,TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo
from flasker.WtformCheck import My_Length,cheak_Mail

class CommentForm(FlaskForm):
    my_length = My_Length(max=8,min=3)
    cheak_mail = cheak_Mail()
    username=StringField(
        'Name',
        validators=[DataRequired(message='不能为空'),my_length]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(max=12,min=3,message='3-8')]
    )
    re_password=PasswordField(
        're_password',
        validators=[DataRequired(message='Not null'),Length(min=3,max=12,message='3-8'),EqualTo('password',message='must EqualTo password')]

    )
    email = StringField(
        'email',
        validators=[DataRequired(message='not Null')]
    )
    root = HiddenField(
        'root',
        validators=[DataRequired(message='not Null')],
        render_kw = {'value':'1'}
    )
    descrption = TextAreaField(
        'root',
        validators=[DataRequired(message='not Null')],
    )