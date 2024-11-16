from .blueprints import index_blueprint
from .blueprints import blog_blueprint
from .model import database

from flask import Flask


def _set_config(app: Flask) -> None:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def _register_blueprints(app: Flask) -> None:
    app.register_blueprint(index_blueprint)
    app.register_blueprint(blog_blueprint)


def _initilize_database(app: Flask) -> None:
    database.init_app(app)
    with app.app_context():
        database.create_all()


def create_website():
    app = Flask(__name__)
    _set_config(app)
    _initilize_database(app)
    _register_blueprints(app)
    return app
