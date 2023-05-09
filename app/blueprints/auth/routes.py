from flask import render_template

from . import bp
from app.forms import RegisterForm

@bp.route('/register')
def register():
    form = RegisterForm()
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