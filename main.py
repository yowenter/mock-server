
from app import app


@app.route("/")
def index():
    return "Hello World!"


def create_app():
    from routes import register_routes
    application = register_routes(app)
    return application


if __name__ == "__main__":
    create_app()
    app.run()
