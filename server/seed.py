from config import db, app
from models import User, Project, Portfolio

def seed_database():
    with app.app_context():
        User.query.delete()
        Project.query.delete()
        Portfolio.query.delete()

        user1 = User(username='DesiahB', name='Desiah Barnett', email='desiahbarnett@gmail.com', password_hash='password1')
        user2 = User(username='OctaviaB', name='Octavia Kronemberg', email='octavia@example.com', password_hash='password2')
        user3 = User(username='BatshevaP', name='Batsheva Parshan', email='batsheva@example.com', password_hash='password3')

        project1 = Project(title='Shift Pro', demo_video='https://www.loom.com/share/5ec155e804e54ea48f4259c6e1dbd35f?sid=f59301ac-2579-4454-afd7-414b466883f4', description='Employing React for dynamic frontend interfaces and SQLAlchemy with PostgreSQL backend, I architect comprehensive employee time tracking platforms. Leveraging Render.com for seamless deployment, I ensure scalable solutions for efficient timelog management. Committed to user-centric design and performance optimization, my systems empower organizations to streamline operations and boost productivity with intuitive time tracking functionalities.', github_link='https://github.com/Desiah94/shiftpro', user=user1)
        project2 = Project(title='Cocktail Club', demo_video='https://example.com/demo2', description='Project 2 description', github_link='https://github.com/example/project2', user=user1)
        project3 = Project(title='Car Sales', demo_video='https://example.com/demo3', description='Project 3 description', github_link='https://github.com/example/project3', user=user1)
        project4 = Project(title='Astro Honey', demo_video='https://example.com/demo3', description='Project 3 description', github_link='https://github.com/example/project3', user=user1)
        project5 = Project(title='Arcade-O', demo_video='https://example.com/demo3', description='Project 3 description', github_link='https://github.com/example/project3', user=user1)
        project6 = Project(title='Car Capsule Museum', demo_video='https://example.com/demo3', description='Project 3 description', github_link='https://github.com/example/project3', user=user1)
        
        
        portfolio1 = Portfolio(name='Portfolio 1', users=[user1, user2], projects=[project1, project2])
        portfolio2 = Portfolio(name='Portfolio 2', users=[user2, user3], projects=[project2, project3])

        db.session.add_all([user1, user2, user3, project1, project2, project3,project4, project5, project6, portfolio1, portfolio2])
        db.session.commit()

if __name__ == "__main__":
    seed_database()
    print("Database seeded successfully.")
