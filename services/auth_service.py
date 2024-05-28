from flask_jwt_extended import create_access_token

from create_app import db
from models.user import User


def register_user(username, password):
    if User.query.filter_by(username=username).first():
        return None, "User already exists"
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user, None

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return access_token, None
    return None, "Invalid credentials"
