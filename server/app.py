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
    
# View all portfolios
class Portfolios(Resource):
    def get(self):
        portfolios = Portfolio.query.all()
        # Serialize portfolios here using SerializerMixin
        return portfolios

# View a specific portfolio
class PortfolioDetails(Resource):
    def get(self, portfolio_id):
        portfolio = Portfolio.query.get(portfolio_id)
        if portfolio:
            # Serialize portfolio here using SerializerMixin
            return portfolio
        else:
            return {'error': 'Portfolio not found'}, 404

# Create a new portfolio
class NewPortfolio(Resource):
    def post(self):
        data = request.json
        new_portfolio = Portfolio(name=data['name'])
        db.session.add(new_portfolio)
        db.session.commit()
        return {'message': 'Portfolio created successfully'}

# Update a portfolio
class UpdatePortfolio(Resource):
    def put(self, portfolio_id):
        data = request.json
        portfolio = Portfolio.query.get(portfolio_id)
        if portfolio:
            portfolio.name = data['name']
            db.session.commit()
            return {'message': 'Portfolio updated successfully'}
        else:
            return {'error': 'Portfolio not found'}, 404

# Delete a portfolio
class DeletePortfolio(Resource):
    def delete(self, portfolio_id):
        portfolio = Portfolio.query.get(portfolio_id)
        if portfolio:
            db.session.delete(portfolio)
            db.session.commit()
            return {'message': 'Portfolio deleted successfully'}
        else:
            return {'error': 'Portfolio not found'}, 404

# Define routes
api.add_resource(Users, '/users')
api.add_resource(UserDetails, '/users/<int:user_id>')
api.add_resource(NewUser, '/users/new')
api.add_resource(UpdateUser, '/users/<int:user_id>/update')
api.add_resource(DeleteUser, '/users/<int:user_id>/delete')
api.add_resource(Projects, '/projects')
api.add_resource(NewProject, '/projects/new')
api.add_resource(UpdateProject, '/projects/<int:project_id>/update')
api.add_resource(DeleteProject, '/projects/<int:project_id>/delete')
api.add_resource(OtherUsersProjects, '/users/<int:user_id>/projects')
api.add_resource(Portfolios, '/portfolios')
api.add_resource(PortfolioDetails, '/portfolios/<int:portfolio_id>')
api.add_resource(NewPortfolio, '/portfolios/new')
api.add_resource(UpdatePortfolio, '/portfolios/<int:portfolio_id>/update')
api.add_resource(DeletePortfolio, '/portfolios/<int:portfolio_id>/delete')

# Welcome message
@app.route('/')
def index():
    return '<h1>Welcome to Portfolio Showcase API</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
