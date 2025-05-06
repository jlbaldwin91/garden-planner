from faker import Faker
from garden_planner.src.models import db, User, Garden  # Use one consistent import path

fake = Faker()

def seed_users_and_gardens(num_users=5, gardens_per_user=2):
    for _ in range(num_users):
        user = User(
            username=fake.user_name(),
            email=fake.email()
        )
        db.session.add(user)
        db.session.flush()  # To get user.id before commit

        for _ in range(gardens_per_user):
            garden = Garden(
                name=fake.word().capitalize() + " Garden",
                zone=fake.random_element(elements=('6a', '7b', '8a', '8b', '9a')),
                user_id=user.id
            )
            db.session.add(garden)

    db.session.commit()
    print(f"Seeded {num_users} users with {gardens_per_user} gardens each.")

if __name__ == "__main__":
    from garden_planner.wsgi import app  # Import app from where it is defined
    with app.app_context():
        seed_users_and_gardens()