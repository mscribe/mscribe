from .admin import admin_blueprint
from .reader import reader_blueprint


all_blueprints = [
    admin_blueprint,
    reader_blueprint
]
