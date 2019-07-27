
from . import db

class User(db.Model):
    __tablename__ = 'user'
    id =db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255)) # 注册邮箱，可以根据邮箱找回密码
    root = db.Column(db.Integer()) # 0为root权限，不设置上线，越大权限越小 可以以后根据模块灵活调整
    posts = db.relationship(
        'Post',
        backref='user',
        lazy='dynamic',
    )

    pictures = db.relationship(
        'Picture',
        backref='picture',
        lazy='dynamic'
    )
    self_videos = db.relationship(
        'Self_video',
        backref = 'selfvideo',
        lazy='dynamic'
    )
    def __repr__(self):
       return"<user '{}>'".format(self.username)
    def check_password(self,username,password):
        return password==User.query.filter_by(username=username).first().password
    def check_username(self,username):
        return User.query.filter_by(username=username).first()==None
    def insert_user(self,username,password,email,root):
        try:
            user = User()
            user.username=username
            user.password=password
            user.email=email
            user.root = root
            db.session.add(user)
            db.session.commit()
            print('successful insert')
            return True
        except:
            print('insert error')
    def updata_password(self,**kwargs):
        if kwargs['password'] == User.query.filter_by(username=kwargs['username']).first().password:
            User.query.filter_by(username=kwargs['username']).updata(
                {'password':kwargs['repassword']}
            )
            return True
        else:
            return False
    def delete_user(self,username,id):
        if int(User.query.filter_by(username=username).first().root) == 0:
            db.session.delete(User.query.fliter_by(id=id))
            db.commit()
            return True
        else:
            return False
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.TEXT)
    publish_date=db.Column(db.DateTime())
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))#外键约束
    comments = db.relationship(
        'Comment',
        backref = 'comment',
        lazy = 'dynamic'
    )
    def __repr__(self):
        return "<Post '{}'>".format(self.title)
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.TEXT)
    ate = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(),db.ForeignKey('post.id'))#外键约束
    def __repr__(self):
        return "<Comment '{}'>".format(self.title)
class Picture(db.Model):
    __tablename__= 'picture'
    id = db.Column(db.Integer(),primary_key=True)
    url= db.Column(db.String(255))
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
class Self_video(db.Model):
    __tablename__= 'selfvideo'
    id = db.Column(db.Integer(),primary_key=True)
    url = db.Column(db.String(255))
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
