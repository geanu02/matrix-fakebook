from flask import render_template, redirect, flash, url_for

from app.models import User
from app import db

from . import bp
from app.forms import RegisterForm

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        user_check = User.query.filter_by(username=username).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not user_check and not email:
            u = User(username=username,email=form.email.data,password=form.password.data)
            u.commit()
            flash(f"Request for {username}: {email} successfully registered!")
            return redirect(url_for("main.home"))
        if user_check:
            flash(f"{username} already taken. Try again.")
        else:
            flash(f"{form.email.data} already taken. Try again.")
    return render_template(
        'register.jinja',
        title="Matrix Fakebook: Register Page",
        form=form
    )

@bp.route('/signin')
def signin():
    return render_template(
        'signin.jinja',
        title="Matrix Fakebook: Signin Page"
    )