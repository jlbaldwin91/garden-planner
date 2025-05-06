from flask import Blueprint, jsonify, request, abort
from ..models import PlantingSchedule, db

bp = Blueprint('planting_schedule', __name__, url_prefix='/planting_schedule')

# Create planting schedule
@bp.route('', methods=['POST'])
def create_planting_schedule():
    data = request.get_json()
    plant_id = data.get('plant_id')
    planting_date = data.get('planting_date')
    
    if not plant_id or not planting_date:
        abort(400, 'Plant ID and planting date are required')
    
    planting_schedule = PlantingSchedule(plant_id=plant_id, planting_date=planting_date)
    db.session.add(planting_schedule)
    db.session.commit()
    return jsonify(planting_schedule.serialize()), 201

# Read all planting schedules
@bp.route('', methods=['GET'])
def get_planting_schedules():
    schedules = PlantingSchedule.query.all()
    return jsonify([schedule.serialize() for schedule in schedules])

# Read a single planting schedule
@bp.route('/<int:id>', methods=['GET'])
def get_planting_schedule(id):
    schedule = PlantingSchedule.query.get(id)
    if schedule is None:
        abort(404, 'Planting Schedule not found')
    return jsonify(schedule.serialize())

# Update a planting schedule
@bp.route('/<int:id>', methods=['PUT'])
def update_planting_schedule(id):
    schedule = PlantingSchedule.query.get(id)
    if schedule is None:
        abort(404, 'Planting Schedule not found')

    data = request.get_json()
    schedule.planting_date = data.get('planting_date', schedule.planting_date)
    
    db.session.commit()
    return jsonify(schedule.serialize())

# Delete a planting schedule
@bp.route('/<int:id>', methods=['DELETE'])
def delete_planting_schedule(id):
    schedule = PlantingSchedule.query.get(id)
    if schedule is None:
        abort(404, 'Planting Schedule not found')
    
    db.session.delete(schedule)
    db.session.commit()
    return '', 204