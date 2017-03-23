from routes import register_routes

app = register_routes()


@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run()


