from flask import Blueprint
from flask import render_template


index_blueprint = Blueprint(name="index",
                            import_name=__name__)


@index_blueprint.route("/")
def index() -> None:
    return render_template("index.html", blogs=[])
