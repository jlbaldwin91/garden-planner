import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Index
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gardens = db.relationship('Garden', backref='owner', lazy=True)
    password_hash = db.Column(db.String(128), nullable=False)

    # A method to set the password
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # A method to check the password
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
    

class Garden(db.Model):
    __tablename__ = 'gardens'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    zone = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    __table_args__ = (Index('idx_garden_user_id', 'user_id'),)
    plants = db.relationship('Plant', backref='garden', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "zone": self.zone,
            "user_id": self.user_id
        }

class Plant(db.Model):
    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    garden_id = db.Column(db.Integer, db.ForeignKey('gardens.id'), nullable=False)
    __table_args__ = (Index('idx_plant_garden_id', 'garden_id'),)
    schedules = db.relationship('PlantingSchedule', backref='plant', lazy=True)
    description = Column(db.String, nullable=True) 
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "garden_id": self.garden_id
        }

class PlantingSchedule(db.Model):
    __tablename__ = 'planting_schedule'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    planting_date = db.Column(db.Date, nullable=False)
    harvest_date = db.Column(db.Date, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "plant_id": self.plant_id,
            "planting_date": self.planting_date.isoformat() if self.planting_date else None,
            "harvest_date": self.harvest_date.isoformat() if self.harvest_date else None
        }

class Harvest(db.Model):
    __tablename__ = 'harvests'
    id = db.Column(db.Integer, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey('plants.id'), nullable=False)
    harvest_date = db.Column(db.Date, nullable=False)
    yield_amount = db.Column(db.Float)

    plant = db.relationship('Plant', backref='harvests')