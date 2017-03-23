from flask.ext.script import Manager, Shell, Server

from mock_server.app import create_app

app = create_app()

manager = Manager(app)


@app.route("/")
def index():
    return "Mock Server API"


manager.add_command('run_server',
                    Server(host='0.0.0.0', port=5000, threaded=True))

manager.add_command('shell', Shell())

if __name__ == "__main__":
    manager.run(default_command='runserver')
