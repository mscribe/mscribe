from website.model import Blog

from flask import Blueprint
from flask import render_template
from flask import request

index_blueprint = Blueprint(name="index",
                            import_name=__name__)


@index_blueprint.route("/")
def index(page: int = 1) -> None:
    request.args.get("language", "en", type=str)
    page = request.args.get("page", 1, type=int)
    per_page = 20

    query = Blog.query.order_by(Blog.created_date.desc())
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    return render_template("index.html",
                           blogs=pagination.items,
                           pagination=pagination)
