from datetime import timedelta
from flask import Blueprint, flash, current_app, redirect, render_template, url_for, session
from flask_login import current_user, login_user, logout_user, login_required

from app.auth.form import LoginForm
from app.auth.model import User

bp = Blueprint("auth", __name__, url_prefix="/")
    
@bp.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for(current_app.config["ROUTES_PATHNAME_PREFIX"]))
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(u)
        return redirect(url_for(current_app.config["ROUTES_PATHNAME_PREFIX"]))
    return render_template('/login.html', title='Sign In', form=form)
    
@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    
@bp.before_request
def before_request():
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(minutes=1500)
    session.modified = True
