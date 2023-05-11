from flask import request, jsonify

from . import bp
from app.models import Post, User

# Receive all Posts
@bp.get('/posts')
def api_posts():
    posts = Post.query.all()
    if posts:
        return jsonify([{
            'id': post.id,
            'body': post.body,
            'timestamp': post.timestamp,
            'author': post.user_id
        } for post in posts]), 200
    return jsonify([{'message':'No posts available to view.'}]), 404
# Receive Posts from Single User
@bp.get('/posts/<username>')
def user_posts(username):
    user = User.query.filter_by(username=username)
    if user:
        return jsonify([{
                'id': post.id,
                'body': post.body,
                'timestamp': post.timestamp,
                'author': post.user_id
            } for post in user.posts]), 200
    return jsonify([{'message':'Invalid username.'}]), 404
# Send Single Post
@bp.get('/post/<id>')
def get_Post(id):
    try:
        post = Post.query.get(id)
        return jsonify([{
                'id': post.id,
                'body': post.body,
                'timestamp': post.timestamp,
                'author': post.user_id
            }])
    except:
        jsonify([{'message':'Invalid post.'}]), 404


# Make a Post