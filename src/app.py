from website import get_app


app = get_app()


if __name__ == "__main__":
    app.run("0.0.0.0", port=3000, debug=True)
