from config import db, app
from models import User, Project, Portfolio

from config import db, app
from models import User, Project, Portfolio

def seed_database():
    with app.app_context():
        User.query.delete()
        Project.query.delete()
        Portfolio.query.delete()

        user1 = User(username='DesiahB', name='Desiah Barnett', email='desiahbarnett@gmail.com', password_hash='password1')

        project1 = Project(
            title='Shift Pro',
            loom_embed_url='https://www.loom.com/embed/e68a762f2e154c458ceb3e87f8d4ca84?sid=c8aa84f6-2167-41da-b6a0-8126afc6e1f4',
            description='Employing React for dynamic frontend interfaces and SQLAlchemy with PostgreSQL backend, I architect comprehensive employee time tracking platforms. Leveraging Render.com for seamless deployment, I ensure scalable solutions for efficient timelog management. Committed to user-centric design and performance optimization, my systems empower organizations to streamline operations and boost productivity with intuitive time tracking functionalities.',
            github_link='https://github.com/Desiah94/shiftpro',
            user=user1
        )

        project2 = Project(
            title='Cocktail Club',
            loom_embed_url='https://www.loom.com/embed/22e9e9cefac84d75a0182e3f4cf0565d?sid=599fba6f-9295-4b58-9845-415217f7d42f',
            description='Cocktail Club, our coding bootcamp capstone, features a dynamic site updating weekly with new cocktail recipes, highlighting our skills in JavaScript and React through interactive user engagement and API integration.',
            github_link='https://github.com/Huntmanjoe/Phase-1-Project',
            user=user1
        )

        project3 = Project(
            title='Car Sales',
            loom_embed_url='https://www.loom.com/embed/e68a762f2e154c458ceb3e87f8d4ca84?sid=b060f6ee-1740-442e-84fb-662b29fcddb4',
            description='Introducing the Car App, a dynamic frontend project designed for car enthusiasts and potential buyers. This application features individual car cards loaded from a JSON server, each equipped with a unique inquiry form. Users can view car details, including photos and descriptions, and directly submit inquiries to the dealership. Developed using HTML, CSS, and JavaScript, this app demonstrates innovative web development techniques to enhance user interaction and data management. Join us in exploring a modern approach to digital car shopping!',
            github_link='https://github.com/Desiah94/carapp',
            user=user1
        )

        project4 = Project(
            title='Astro Honey',
            loom_embed_url='https://www.loom.com/embed/dc44aa7b3f904d2e88ec8c01d1ddb210?sid=906f4a75-8e76-4d05-a4d1-ee96826951ce',
            description='Developed a React project that displays information for each zodiac sign, showcasing adeptness in creating reusable components and managing prop-based data flow from parent to child components. The application uses JSON Server to simulate a backend, enabling dynamic fetching of comments upon loading the comment page and handling user-submitted comments via POST requests. Controlled forms are used to ensure consistent state management throughout the user experience. This setup not only highlights fundamental React skills but also integrates frontend interactions with backend-like data handling using JSON Server, enhancing user engagement through interactive and responsive design.',
            github_link='https://github.com/Desiah94/astro-project-phase-2',
            user=user1
        )

        project5 = Project(
            title='Arcade-O',
            loom_embed_url='https://www.loom.com/embed/27b30a99672c404ab7ab79bf467856da?sid=a869e30d-ccda-4864-8cea-d3e9fc6b03b4',
            description='Arcade-O backend SQL database, created via CLI, empowers efficient user management. CRUD operations enable seamless creation and assignment of users to specific locations and arcades. This setup streamlines arcade operations, providing a robust solution for managing user data and enhancing organization in gaming environments. Explore the GitHub demo to experience its functionality firsthand.',
            github_link='https://github.com/stacks-loops/phaze-3-group-project',
            user=user1
        )

        project6 = Project(
            title='Car Capsule Museum',
            loom_embed_url='https://www.loom.com/embed/5629b4e2583b49e7863aee3ff4b8c2f8?sid=f039f723-1725-4bca-9f55-a2caf671d753',
            description='Developed a car showcase app with full CRUD functionality, allowing users to contribute to a car museum by adding cars and leaving reviews. Implemented user account features for enhanced engagement. The Flask backend stores reviews and UI data in a database, ensuring data persistence and efficient management. Project published on GitHub for accessibility and collaboration.',
            github_link='https://github.com/kcastillo3/phase-4-carcapsule-museum',
            user=user1
        )

        portfolio1 = Portfolio(name='Portfolio 1', users=[user1], projects=[project1, project2, project3, project4, project5, project6])

        db.session.add_all([user1, project1, project2, project3, project4, project5, project6, portfolio1])
        db.session.commit()

if __name__ == "__main__":
    seed_database()
    print("Database seeded successfully.")
