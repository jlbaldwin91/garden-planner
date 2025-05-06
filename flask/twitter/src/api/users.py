from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Tweet, likes_table

import hashlib
import secrets

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all() # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize()) # build list of Users as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())

@bp.route('', methods=['POST'])
def create():

    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)

    username = request.json['username']
    password = request.json['password']

    if len(username) < 3 or len(password) < 8:
        return abort(400)

    u = User(
        password=scramble(request.json['password']),
        username=request.json['username']
    )
    db.session.add(u) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(u.serialize()) 

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

@bp.route('/<int:id>', methods=['PATCH','PUT'])
def update(id):
    u = User.query.get_or_404(id)

    data = request.json

    if 'username' not in data and 'password' not in data:
        return abort(400)

    if 'username' in data:
        if len(data['username']) < 3:
            return abort(400)
        u.username = data['username']


    if 'password' in data:
        if len(data['password']) < 8:
            return abort(400)
        u.password = scramble(data['password']) 

    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)

@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id: int):
    u = User.query.get_or_404(id)
    result = []
    for t in u.liked_tweets:
        result.append(t.serialize())
    return jsonify(result)