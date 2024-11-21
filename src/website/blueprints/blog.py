from website.utils.converter import Converter

from flask import Blueprint
from flask import render_template


blog_blueprint = Blueprint(name="blog", import_name=__name__)


@blog_blueprint.route("/blog/")
def blog() -> None:
    converter = Converter()
    html_content = converter.convert("")
    return render_template("blogpost.html",
                           html_content=html_content)
