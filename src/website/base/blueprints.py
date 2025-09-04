from flask import Flask
from website.blueprints import all_blueprints


def register_blueprints(app: Flask) -> None:
    for blueprint in all_blueprints:
        app.register_blueprint(blueprint)
