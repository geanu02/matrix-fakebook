from flask import request, jsonify

from . import bp
from app.models import User

# Verify User
@bp.post('/verify-user')
def verify_user():
    content = request.json
    username = content['username']
    password = content['password']
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify([{'userid': user.user_id}])
    return jsonify({'message': 'Invalid User Info'})
# Register User
@bp.post('/register-user')
def register_user():
    content = request.json
    username = content['username']
    email = content['email']
    password = content['password']
    user_check = User.query.filter_by(username=username).first()
    if user_check:
        return jsonify([{'message': 'Username taken. Try again.'}])
    email_check = User.query.filter_by(email=email).first()
    if email_check:
        return jsonify([{'message': 'Email taken. Try again.'}])
    user = User(email=email, username=username)
    user.password = user.hash_password(password)
    user.commit()
    return jsonify([{'message': f"{user.username} registered!"}])