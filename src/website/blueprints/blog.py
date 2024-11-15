from flask import Blueprint
from flask import render_template


blog_blueprint = Blueprint(name="blog",
                           import_name=__name__)


@blog_blueprint.route("/blog/")
def blog() -> None:
    return render_template("blog.html")
