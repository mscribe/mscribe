import os

from flask import Flask


def set_configuration(app: Flask) -> None:
    host = os.getenv("DATABASE_HOST")
    user = os.getenv("DATABASE_USERNAME")
    password = os.getenv("DATABASE_PASSWORD")
    schema = os.getenv("DATABASE_SCHEMA")
    port = os.getenv("DATABASE_PORT")
    URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'

    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SERVER_NAME'] = "mscribe.ms:3000"
    app.config['VERSION'] = "v1.0.0"
