from website.controller import BlogController

from website.utils.converter import Converter

from flask import Blueprint
from flask import render_template


blog_blueprint = Blueprint(name="blog", import_name=__name__)


@blog_blueprint.route("/<string:language>/blog/<int:blog_id>")
def blog(language: str, blog_id: int) -> None:
    converter = Converter()
    blog = BlogController.get_blog(language, blog_id)
    blog.body = converter.convert(blog.body)
    return render_template("blogpost.html",
                           language=language,
                           blog=blog)
