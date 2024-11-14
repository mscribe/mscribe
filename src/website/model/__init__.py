from flask_sqlalchemy import SQLAlchemy


database = SQLAlchemy()


class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(120), nullable=False, unique=True)


class Blog(database.Model):
    ...
