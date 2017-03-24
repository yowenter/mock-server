from flask import Flask
import logging
from flask.ext.cors import CORS

import config

if config.PROD:
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('app').setLevel(logging.INFO)
    logging.getLogger(__name__).info('log init prod')
else:
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('app').setLevel(logging.DEBUG)
    logging.getLogger(__name__).info('log init debug')

import routes

LOG = logging.getLogger(__name__)

cors = CORS()


def configure_app(app):
    app.config['DEBUG'] = not config.PROD
    app.config['CORS_MAX_AGE'] = 86400


def config_extensions(app):
    cors.init_app(app)


def config_routes(app):
    routes.register_mock_blueprint(app)
    app.register_blueprint(routes.file_blueprint)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    configure_app(app)
    config_extensions(app)
    config_routes(app)

    return app
