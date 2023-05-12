from flask import request, jsonify

from . import bp
from app.models import Post, User
from app.blueprints.api.helpers import token_required

# Receive all Posts
@bp.get('/posts')
@token_required
def api_posts(user):
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
@token_required
def user_posts(user, username):
    u = User.query.filter_by(username=username)
    if u:
        return jsonify([{
                'id': post.id,
                'body': post.body,
                'timestamp': post.timestamp,
                'author': post.user_id
            } for post in u.posts]), 200
    return jsonify([{'message':'Invalid username.'}]), 404

# Send Single Post
@bp.get('/post/<post_id>')
@token_required
def get_Post(user, post_id):
    try:
        post = Post.query.get(post_id)
        return jsonify([{
                'id': post.id,
                'body': post.body,
                'timestamp': post.timestamp,
                'author': post.user_id
            }])
    except:
        jsonify([{'message':'Invalid post.'}]), 404

# Make a Post
@bp.post('/post')
@token_required
def make_post(user):
    try:
    # Receive Post data
        content = request.json
    # Create a post entry (instantiate Post)
        post = Post(
            body=content.get('body'), 
            user_id=user.user_id
        )
    # Add foreign key to user id
    # # commit our post
        post.commit()
    # return message
        return jsonify([{"message": "Post created.", "body": post.body}]), 200
    except:
        return jsonify([{"message": "Invalid form data."}]), 401