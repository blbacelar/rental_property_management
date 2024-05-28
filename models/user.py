from passlib.hash import sha256_crypt

from create_app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = sha256_crypt.hash(password)

    def check_password(self, password):
        return sha256_crypt.verify(password, self.password_hash)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }
