from flask import render_template, redirect, flash, url_for

from . import bp
from app.forms import RegisterForm

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = form.username.data
        email = form.email.data
        flash(f"Request for {user}: {email} successfully registered!")
        return redirect(url_for("main.home"))
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