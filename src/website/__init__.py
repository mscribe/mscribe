from flask import Flask


def create_website():
    app = Flask(__name__)

    from .blueprints import index_blueprint
    app.register_blueprint(index_blueprint)

    return app
