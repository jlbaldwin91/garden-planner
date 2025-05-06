from flask import Blueprint, jsonify
from ..models import db, User

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('', methods=['GET'])
def index():
    users = User.query.all()
    return jsonify([u.serialize() for u in users])