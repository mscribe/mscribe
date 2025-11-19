from flask import Flask

from .configuration import set_configuration
from .database import initilize_database
from .blueprints import register_blueprints


def setup(app: Flask) -> None:
    set_configuration(app)
    initilize_database(app)
    register_blueprints(app)
