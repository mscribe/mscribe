from flask import Blueprint


admin_blueprint = Blueprint(name="admin",
                            import_name=__name__)


@admin_blueprint.route("/", subdomain="admin")
def index():
    return "Admin page"
