from website import create_website

if __name__ == "__main__":
    app = create_website()
    app.run("0.0.0.0", port=80, debug=True)
