from flask import render_template

from . import bp

@bp.route('/register')
def register():
    return render_template(
        'register.jinja',
        title="Matrix Fakebook: Register Page"
    )

@bp.route('/signin')
def signin():
    return render_template(
        'signin.jinja',
        title="Matrix Fakebook: Signin Page"
    )