# -*- encoding:utf-8 -*-


import os
import sys
import traceback
import logging

import ConfigParser

from app import app
import json

from flask import jsonify

LOG = logging.getLogger(__name__)

JSON_FILES_DIR = os.path.join(os.path.dirname(__file__), 'json_files')

if os.path.exists(os.path.join(os.path.dirname(__file__), 'routes.cfg')):
    LOG.info("Reading routes config")
    config = ConfigParser.ConfigParser()
    config.read('routes.cfg')
    _routes = config._sections.get("routes").items()
    routes = set()
    for _r in _routes:
        if not str(_r[0]).startswith('__'):
            routes.add(_r)

    LOG.info("Loaded routes : %s", routes)


else:
    routes = (
        ('/ping', 'ping.json'),
    )


def gen_endpoint_func(json_file_name):
    def f(*args, **kwargs):
        json_file = os.path.join(JSON_FILES_DIR, json_file_name)
        assert os.path.exists(json_file), "json_file `%s` not exists" % json_file
        with open(os.path.join(JSON_FILES_DIR, json_file_name), 'r') as f:
            try:
                response_data = jsonify(json.load(f))
                return response_data
            except Exception as e:
                LOG.error("Fetch Json Error %s %s", json_file, str(e), exc_info=True)
                return "Json File Load Error %s" % str(e)

    return f


def gen_endpoint(route_path):
    return '_'.join(route_path.split('/'))


def register_routes():
    for route in routes:
        try:

            app.add_url_rule(route[0], endpoint=gen_endpoint(route[0]), view_func=gen_endpoint_func(route[1]),
                             methods=['GET', 'PUT', 'POST', 'OPTIONS', 'DELETE', 'PATCH'])
        except Exception as e:
            LOG.warning("Add route failure %s", str(e))
            traceback.print_exc(file=sys.stdout)

    return app

