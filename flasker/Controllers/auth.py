import functools
from flasker.tasks import send_email,send_login_email
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash
from flasker.MyFroms import CommentForm
from flasker.DBModel import User
from flasker import csrf

bp = Blueprint('auth', __name__, url_prefix='/auth')
@csrf.exempt
@bp.route('/register', methods=('GET', 'POST'))
#@cache.cached(timeout=120)
def register():
    if request.method=='GET':
        form = CommentForm()
        return render_template('auth/register.html',form=form)
    else:
        form = CommentForm(formdata=request.form)
        if form.validate():
            username = request.form['username']
            root = int(request.form['root'])
            password = request.form['password']
            email = request.form['email']
            descrption = request.form['descrption']
            print(descrption.__repr__())
           #user=User()
           # user.insert_user(username=username,root=root,password=password,email=email)
            return "登录成功"
        else:
            print(form.errors, "错误信息")
        return render_template("auth/register.html", form=form)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = CommentForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = User()
        if user.check_password(username=username,password=password):
            session.clear()
            session['username'] = username
            #return redirect(url_for('index'))
            return 'login successful'

        else:
            error='error'


        flash(error)

    return render_template('auth/login.html',form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
   # db=get_db()
    if user_id is None:
        g.user = None
    else:
        g.user = usedb.execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)
    return wrapped_view