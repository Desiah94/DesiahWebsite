from flask import request
from flask_restful import Resource, Api
from config import app, db, api
from models import User, Project, Portfolio

class Projects(Resource):
    def get(self):
        projects = Project.query.all()
        serialized_projects = [self.project_to_dict(project) for project in projects]
        return serialized_projects, 200

    def project_to_dict(self, project):
        return {
            'id': project.id,
            'title': project.title,
            'demo_video': project.demo_video,
            'description': project.description,
            'github_link': project.github_link,
            'user_id': project.user_id
        }

api.add_resource(Projects, '/projects')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
