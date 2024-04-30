from app import db, app
from models import User, Project, Portfolio
from werkzeug.security import generate_password_hash
from random import choice
from faker import Faker

fake = Faker()

def create_tables():
    with app.app_context():
        db.create_all()
        print("All tables created.")

def seed_database():
    db.session.query(Portfolio).delete()
    db.session.query(Project).delete()
    db.session.query(User).delete()
    db.session.commit()

    # Seed users
    users = []
    existing_emails = set()
    for _ in range(10):
        username = unique_username(users)
        email = unique_email(existing_emails)
        user_data = {
            'username': username,
            'name': 'Example Name',
            'email': email,
            'password_hash': generate_password_hash('example_password')
        }
        user = User(**user_data)
        users.append(user)
        db.session.add(user)
    db.session.commit()

    # Seed projects
    projects = []
    for _ in range(20):
        project_data = {
            'title': 'Example Project',
            'demo_video': 'https://example.com/demo',
            'description': 'This is an example project description.',
            'github_link': 'https://github.com/example/example-project',
            'user': choice(users)  # Choose a random user object for each project
        }
        project = Project(**project_data)
        projects.append(project)
        db.session.add(project)
    db.session.commit()

    # Seed portfolios
    portfolios = []
    for _ in range(5):
        portfolio_data = {
            'name': 'Example Portfolio'
        }
        portfolio = Portfolio(**portfolio_data)
        portfolios.append(portfolio)
        db.session.add(portfolio)
    db.session.commit()

    print("Database seeded successfully.")

def unique_username(existing_users):
    """Generate a unique username."""
    username = None
    while not username or username in [user.username for user in existing_users]:
        username = fake.user_name()
    return username

def unique_email(existing_emails):
    """Generate a unique email."""
    email = None
    while not email or email in existing_emails:
        email = fake.email()
    existing_emails.add(email)
    return email

if __name__ == '__main__':
    with app.app_context():
        create_tables()
        seed_database()
