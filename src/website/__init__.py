from flask import Flask
from website.base import setup


def get_app() -> Flask:
    app = Flask(__name__, subdomain_matching=True)
    setup(app)
    return app
