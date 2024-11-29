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
    languages = LanguageController.get_languages()
    page, per_page = (request.args.get("page", 1, type=int), 20)

    if language not in languages:
        language = "en"

    blogs, pagination = BlogController.get_blogs(language=language,
                                                 page=page,
                                                 per_page=per_page)

    return render_template("index.html",
                           blogs=blogs,
                           pagination=pagination)
