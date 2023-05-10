from flask import render_template, redirect, flash, url_for
from flask_login import login_user
from app.models import User

from . import bp
from app.forms import RegisterForm, SigninForm

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        user_check = User.query.filter_by(username=username).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not user_check and not email:
            u = User(username=username,email=form.email.data)
            u.password = u.hash_password(form.password.data)
            u.commit()
            flash(f"Request for {username}: {email} successfully registered!", "success")
            return redirect(url_for("main.home"))
        if user_check:
            flash(f"{username} already taken. Try again.", "warning")
        else:
            flash(f"{form.email.data} already taken. Try again.", "warning")
    return render_template(
        'register.jinja',
        title="Matrix Fakebook: Register Page",
        form=form
    )

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            flash(f"{form.username.data} signed in.", "success")
            login_user(user)
            return redirect(url_for("main.home"))
        else:
            flash(f"{form.username.data} does not exist or incorrect password.", "warning")
    return render_template(
        'signin.jinja',
        title="Matrix Fakebook: Signin Page",
        form=form
    )