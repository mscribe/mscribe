from flask import Flask

from website.schema import database


def initilize_database(app: Flask) -> None:
    database.init_app(app)
    with app.app_context():
        database.create_all()
