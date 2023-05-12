from flask import request, jsonify
from functools import wraps
from app.models import User

def token_required(flask_route):
    @wraps(flask_route)
    def wrapper(*args,**kwargs):
        if 'x-access-token' in request.headers:
            # bearer <token>
            try:
                token = request.headers['x-access-token'].split()[1]
                user = User.query.filter_by(token=token).first()
                if user:
                    return flask_route(user,*args,**kwargs)
                return jsonify([{"message": "Access denied. 'user' not found."}]), 401
            except:
                return jsonify([{"message": "Access denied. Exception."}]), 401
        return jsonify([{"message": "Access denied. x-access-token not in headers."}]), 401
    return wrapper