import os

from flask import Flask

from .blueprints import client_blueprint
from .blueprints import admin_blueprint
from .schema import database


def _set_config(app: Flask) -> None:
    host = os.getenv("DATABASE_HOST")
    user = os.getenv("DATABASE_USERNAME")
    password = os.getenv("DATABASE_PASSWORD")
    schema = os.getenv("DATABASE_SCHEMA")
    port = os.getenv("DATABASE_PORT")
    URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'

    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SERVER_NAME'] = "mscribe.ms:3000"
    app.config['VERSION'] = "v0.1.1"


def _register_blueprints(app: Flask) -> None:
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(client_blueprint)


def _initilize_database(app: Flask) -> None:
    database.init_app(app)
    with app.app_context():
        database.create_all()


def create_website():
    app = Flask(__name__, subdomain_matching=True)
    _set_config(app)
    _initilize_database(app)
    _register_blueprints(app)
    return app
