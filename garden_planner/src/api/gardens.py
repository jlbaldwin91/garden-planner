from flask import Blueprint, jsonify, request, abort
from ..models import Garden, db

bp = Blueprint('gardens', __name__, url_prefix='/gardens')

# Create garden
@bp.route('', methods=['POST'])
def create_garden():
    data = request.get_json()
    name = data.get('name')
    zone = data.get('zone')
    user_id = data.get('user_id')
    
    if not name or not zone or not user_id:
        abort(400, 'Name, zone, and user_id are required')
    
    garden = Garden(name=name, zone=zone, user_id=user_id)
    db.session.add(garden)
    db.session.commit()
    return jsonify(garden.serialize()), 201

# Read all gardens
@bp.route('', methods=['GET'])
def get_gardens():
    gardens = Garden.query.all()
    return jsonify([garden.serialize() for garden in gardens])

# Read a single garden
@bp.route('/<int:id>', methods=['GET'])
def get_garden(id):
    garden = Garden.query.get(id)
    if garden is None:
        abort(404, 'Garden not found')
    return jsonify(garden.serialize())

# Update a garden
@bp.route('/<int:id>', methods=['PUT'])
def update_garden(id):
    garden = Garden.query.get(id)
    if garden is None:
        abort(404, 'Garden not found')

    data = request.get_json()
    garden.name = data.get('name', garden.name)
    garden.zone = data.get('zone', garden.zone)
    
    db.session.commit()
    return jsonify(garden.serialize())

# Delete a garden
@bp.route('/<int:id>', methods=['DELETE'])
def delete_garden(id):
    garden = Garden.query.get(id)
    if garden is None:
        abort(404, 'Garden not found')
    
    db.session.delete(garden)
    db.session.commit()
    return '', 204