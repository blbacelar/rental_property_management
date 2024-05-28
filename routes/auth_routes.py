from flask import Blueprint, jsonify, request

from services.auth_service import authenticate_user, register_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user, error = register_user(data['username'], data['password'])
    if error:
        return jsonify({'error': error}), 400
    return jsonify(user.to_dict()), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    token, error = authenticate_user(data['username'], data['password'])
    if error:
        return jsonify({'error': error}), 401
    return jsonify({'token': token}), 200
