from sqlalchemy_serializer import SerializerMixin
from config import db

class User(db.Model, SerializerMixin):
    serialize_rules = ('-projects.user', '-portfolios.users')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # Field for storing password hash

class Project(db.Model, SerializerMixin):
    serialize_rules = ('-user.projects', '-portfolios.projects')

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    demo_video = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    github_link = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('projects', lazy=True))

class Portfolio(db.Model, SerializerMixin):
    serialize_rules = ('-users.portfolios', '-projects.portfolios')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    users = db.relationship('User', secondary='user_portfolio', backref=db.backref('portfolios', lazy=True))
    projects = db.relationship('Project', secondary='project_portfolio', backref=db.backref('portfolios', lazy=True))

# Association Table for many-to-many relationship between User and Portfolio
user_portfolio = db.Table('user_portfolio',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('portfolio_id', db.Integer, db.ForeignKey('portfolio.id'), primary_key=True)
)

# Association Table for many-to-many relationship between Project and Portfolio
project_portfolio = db.Table('project_portfolio',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'), primary_key=True),
    db.Column('portfolio_id', db.Integer, db.ForeignKey('portfolio.id'), primary_key=True)
)
