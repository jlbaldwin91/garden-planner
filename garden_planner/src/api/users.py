from flask import Blueprint, jsonify, request, abort
from ..models import User, db

bp = Blueprint('users', __name__, url_prefix='/users')

# Create user
@bp.route('', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    if not username:
        abort(400, 'Username is required')
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()), 201

# Read all users
@bp.route('', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

# Read a single user
@bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user is None:
        abort(404, 'User not found')
    return jsonify(user.serialize())

# Update a user
@bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if user is None:
        abort(404, 'User not found')
    
    data = request.get_json()
    user.username = data.get('username', user.username)
    
    db.session.commit()
    return jsonify(user.serialize())

# Delete a user
@bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        abort(404, 'User not found')
    
    db.session.delete(user)
    db.session.commit()
    return '', 204