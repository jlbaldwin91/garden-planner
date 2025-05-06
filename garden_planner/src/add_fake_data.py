import sys
import os

# Add the root project folder to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from garden_planner.src import create_app
from garden_planner.src.models import db, User, Garden, Plant, PlantingSchedule, Harvest
from faker import Faker

fake = Faker()

app = create_app()

# Push the application context
with app.app_context():
    # Add users
    users = []
    for _ in range(10): 
        user = User(
            username=fake.user_name(),
            email=fake.email(),
        )
        user.set_password(fake.password())  # Hash the password before saving
        users.append(user)
    db.session.add_all(users)
    db.session.commit()

    gardens = []
    for user in users:
        for _ in range(2):  
            garden = Garden(
                name=fake.word(),
                zone=fake.random_int(min=1, max=13), 
                user_id=user.id
            )
            gardens.append(garden)
    db.session.add_all(gardens)
    db.session.commit()

    plants = []
    for garden in gardens:
        for _ in range(5): 
            plant = Plant(
                name=fake.word(),
                description=fake.sentence(),
                garden_id=garden.id
            )
            plants.append(plant)
    db.session.add_all(plants)
    db.session.commit()

    planting_schedules = []
    for plant in plants:
        planting_schedule = PlantingSchedule(
            plant_id=plant.id,
            planting_date=fake.date_this_decade(),
            harvest_date=fake.date_this_decade(),
            
        )
        planting_schedules.append(planting_schedule)
    db.session.add_all(planting_schedules)
    db.session.commit()

    harvests = []
    for schedule in planting_schedules:
        harvest = Harvest(
        plant_id=schedule.plant_id,
        harvest_date=schedule.harvest_date,
        yield_amount=fake.random_number(digits=2)
        )
        harvests.append(harvest)
    db.session.add_all(harvests)
    db.session.commit()

    print("Fake users, gardens, plants, planting schedules, and harvests added successfully.")