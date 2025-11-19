from mscribe.website import get_app


def run_app() -> None:
    app = get_app()
    app.run("0.0.0.0", port=3000, debug=True)
