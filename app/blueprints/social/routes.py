from flask import render_template
from flask_login import current_user
from . import bp 

from app.models import Post 
from app.forms import PostForm

@bp.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    # if FORM HAS ('POST')
    if form.validate_on_submit():
        p = Post(body=form.body.data)
        p.user_id = current_user.user_id
        p.commit()
        print(f"{p.author= } {p.author.posts[0]}")
    return render_template(
        'post.jinja',
        form=form
        )