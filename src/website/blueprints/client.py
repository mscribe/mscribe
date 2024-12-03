from website.controller import BlogController
from website.controller import LanguageController
from website.utils.converter import Converter

from flask import Blueprint
from flask import render_template
from flask import request

client_blueprint = Blueprint(name="client",
                             import_name=__name__)


@client_blueprint.route("/")
def index(language: str = None, page: int = 1):
    default_language = "en"
    languages = LanguageController.get_languages()

    if language not in languages:
        language = default_language

    page, per_page = (request.args.get("page", 1, type=int), 20)
    blogs, pagination = BlogController.get_blogs(language=language,
                                                 page=page,
                                                 per_page=per_page)

    return render_template("index.html",
                           language=language,
                           blogs=blogs,
                           pagination=pagination)


@client_blueprint.route("/<string:language>/blog/<int:blog_id>")
def blog(language: str, blog_id: int) -> None:
    converter = Converter()
    blog = BlogController.get_blog(language, blog_id)
    blog.body = converter.convert(blog.body)
    return render_template("blogpost.html",
                           language=language,
                           blog=blog)
