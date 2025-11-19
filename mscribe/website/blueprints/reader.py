from flask import Blueprint
from flask import render_template


reader_blueprint = Blueprint("reader_blueprint",
                             import_name=__name__)


@reader_blueprint.route("/")
def index():
    return render_template("index.html")


@reader_blueprint.route("/post/")
def post():
    return render_template("post.html")
