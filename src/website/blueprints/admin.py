from flask import Blueprint


admin_blueprint = Blueprint("admin_blueprint",
                            import_name=__name__)


@admin_blueprint.route("/", subdomain="admin")
def index():
    return "Admin page"
