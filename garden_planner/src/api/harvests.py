from flask import Blueprint, jsonify, request, abort
from ..models import Harvest, db

bp = Blueprint('harvests', __name__, url_prefix='/harvests')

# Create harvest
@bp.route('', methods=['POST'])
def create_harvest():
    data = request.get_json()
    plant_id = data.get('plant_id')
    harvest_date = data.get('harvest_date')
    
    if not plant_id or not harvest_date:
        abort(400, 'Plant ID and harvest date are required')
    
    harvest = Harvest(plant_id=plant_id, harvest_date=harvest_date)
    db.session.add(harvest)
    db.session.commit()
    return jsonify(harvest.serialize()), 201

# Read all harvests
@bp.route('', methods=['GET'])
def get_harvests():
    harvests = Harvest.query.all()
    return jsonify([harvest.serialize() for harvest in harvests])

# Read a single harvest
@bp.route('/<int:id>', methods=['GET'])
def get_harvest(id):
    harvest = Harvest.query.get(id)
    if harvest is None:
        abort(404, 'Harvest not found')
    return jsonify(harvest.serialize())

# Update a harvest
@bp.route('/<int:id>', methods=['PUT'])
def update_harvest(id):
    harvest = Harvest.query.get(id)
    if harvest is None:
        abort(404, 'Harvest not found')

    data = request.get_json()
    harvest.yield_amount = data.get('yield_amount', harvest.yield_amount)
    
    db.session.commit()
    return jsonify(harvest.serialize())

# Delete a harvest
@bp.route('/<int:id>', methods=['DELETE'])
def delete_harvest(id):
    harvest = Harvest.query.get(id)
    if harvest is None:
        abort(404, 'Harvest not found')
    
    db.session.delete(harvest)
    db.session.commit()
    return '', 204