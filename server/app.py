from flask import request
from flask_restful import Resource, Api
from config import app, db, api
from models import User, Project, Portfolio


# View all users
class Users(Resource):
    def get(self):
        users = User.query.all()
        # Serialize users here using SerializerMixin
        return users

# View a specific user
class UserDetails(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            # Serialize user here using SerializerMixin
            return user
        else:
            return {'error': 'User not found'}, 404

# Create a new user
class NewUser(Resource):
    def post(self):
        data = request.json
        new_user = User(username=data['username'], name=data['name'], email=data['email'], password_hash=data['password_hash'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}

# Update a user
class UpdateUser(Resource):
    def put(self, user_id):
        data = request.json
        user = User.query.get(user_id)
        if user:
            user.username = data['username']
            user.name = data['name']
            user.email = data['email']
            user.password_hash = data['password_hash']
            db.session.commit()
            return {'message': 'User updated successfully'}
        else:
            return {'error': 'User not found'}, 404

# Delete a user
class DeleteUser(Resource):
    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}
        else:
            return {'error': 'User not found'}, 404
# View all projects
class Projects(Resource):
    def get(self):
        projects = Project.query.all()
        # Serialize projects here using SerializerMixin
        return projects

# Create a new project
class NewProject(Resource):
    def post(self):
        data = request.json
        new_project = Project(title=data['title'], demo_video=data['demo_video'], description=data['description'], github_link=data['github_link'], user_id=data['user_id'])
        db.session.add(new_project)
        db.session.commit()
        return {'message': 'Project created successfully'}

# Update a project
class UpdateProject(Resource):
    def put(self, project_id):
        data = request.json
        project = Project.query.get(project_id)
        if project:
            project.title = data['title']
            project.demo_video = data['demo_video']
            project.description = data['description']
            project.github_link = data['github_link']
            db.session.commit()
            return {'message': 'Project updated successfully'}
        else:
            return {'error': 'Project not found'}, 404

# Delete a project
class DeleteProject(Resource):
    def delete(self, project_id):
        project = Project.query.get(project_id)
        if project:
            db.session.delete(project)
            db.session.commit()
            return {'message': 'Project deleted successfully'}
        else:
            return {'error': 'Project not found'}, 404

# View other users' projects
class OtherUsersProjects(Resource):
    def get(self, user_id):
        projects = Project.query.filter(Project.user_id != user_id).all()
        # Serialize projects here using SerializerMixin
        return projects

# Define routes
api.add_resource(Projects, '/projects')
api.add_resource(NewProject, '/projects/new')
api.add_resource(UpdateProject, '/projects/<int:project_id>/update')
api.add_resource(DeleteProject, '/projects/<int:project_id>/delete')
api.add_resource(OtherUsersProjects, '/users/<int:user_id>/projects')

# Welcome message
@app.route('/')
def index():
    return '<h1>Welcome to Portfolio Showcase API</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
