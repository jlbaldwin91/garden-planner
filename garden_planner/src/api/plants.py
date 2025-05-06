from flask import Blueprint, jsonify, request, abort
from ..models import Plant, db

bp = Blueprint('plants', __name__, url_prefix='/plants')

# Create plant
@bp.route('', methods=['POST'])
def create_plant():
    data = request.get_json()
    name = data.get('name')
    garden_id = data.get('garden_id')
    
    if not name or not garden_id:
        abort(400, 'Name and garden_id are required')
    
    plant = Plant(name=name, garden_id=garden_id)
    db.session.add(plant)
    db.session.commit()
    return jsonify(plant.serialize()), 201

# Read all plants
@bp.route('', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.serialize() for plant in plants])

# Read a single plant
@bp.route('/<int:id>', methods=['GET'])
def get_plant(id):
    plant = Plant.query.get(id)
    if plant is None:
        abort(404, 'Plant not found')
    return jsonify(plant.serialize())

# Update a plant
@bp.route('/<int:id>', methods=['PUT'])
def update_plant(id):
    plant = Plant.query.get(id)
    if plant is None:
        abort(404, 'Plant not found')

    data = request.get_json()
    plant.name = data.get('name', plant.name)
    
    db.session.commit()
    return jsonify(plant.serialize())

# Delete a plant
@bp.route('/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get(id)
    if plant is None:
        abort(404, 'Plant not found')
    
    db.session.delete(plant)
    db.session.commit()
    return '', 204