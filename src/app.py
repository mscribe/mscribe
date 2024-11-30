from website import create_website


app = create_website()


if __name__ == "__main__":
    app.run("0.0.0.0", port=3000, debug=True)
