from website.controller import BlogController
from website.controller import LanguageController

from flask import Blueprint
from flask import render_template
from flask import request

index_blueprint = Blueprint(name="index",
                            import_name=__name__)


@index_blueprint.route("/")
@index_blueprint.route("/<string:language>/")
def index(language: str = None, page: int = 1) -> None:
    language = language or "en"
    page, per_page = (request.args.get("page", 1, type=int), 20)
    languages = LanguageController.get_languages()
    blogs = BlogController.get_blogs(page=page, per_page=per_page)

    return render_template("index.html",
                           blogs=blogs.items,
                           pagination=blogs)
