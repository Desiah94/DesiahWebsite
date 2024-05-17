from flask import request
from flask_restful import Resource, Api
from config import app, db, api
from models import User, Project, Portfolio


class Projects(Resource):
    def get(self):
        projects = Project.query.all()
        serialized_projects = [self.project_to_dict(project) for project in projects]
        app.logger.info(f"Fetched {len(serialized_projects)} projects")
        app.logger.debug(f"Fetched projects: {serialized_projects}")
        return serialized_projects, 200

    def project_to_dict(self, project):
        return {
            'id': project.id,
            'title': project.title,
            'loom_embed_url': project.loom_embed_url,
            'description': project.description,
            'github_link': project.github_link,
            'user_id': project.user_id
        }

api.add_resource(Projects, '/projects')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
