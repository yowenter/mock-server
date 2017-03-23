# -*- encoding:utf-8 -*-


import ConfigParser
import json
import logging
import sys
import traceback

import os
import flask
from flask import jsonify

LOG = logging.getLogger(__name__)

STATIC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "_static")

ROUTES_CONFIG = os.path.join(STATIC_DIR, "routes.cfg")

assert os.path.exists(ROUTES_CONFIG), "Routes config file `routes.cfg` not exists in `%s`" % str(ROUTES_CONFIG)

routes_config = ConfigParser.ConfigParser()
routes_config.read(ROUTES_CONFIG)
routes_tuples = routes_config._sections.get("routes").items()
routes = set()
for r in routes_tuples:
    if not str(r[0]).startswith('__'):
        routes.add(r)

LOG.info("Loaded routes : \n%s\n", "\n".join([str(r) for r in routes]))


def gen_endpoint_func(json_file_name):
    def f(*args, **kwargs):
        json_file = os.path.join(STATIC_DIR, json_file_name)
        assert os.path.exists(json_file), "json_file `%s` not exists" % json_file
        with open(os.path.join(STATIC_DIR, json_file_name), 'r') as f:
            try:
                response_data = jsonify(json.load(f))
                return response_data
            except Exception as e:
                LOG.error("Fetch Json Error %s %s", json_file, str(e), exc_info=True)
                return "Json File Load Error \n`%s`" % str(e)

    return f


def gen_endpoint(route_path):
    return '_'.join(route_path.split('/'))


def register_routes(app):
    for route in routes:
        try:
            app.add_url_rule(route[0], endpoint=gen_endpoint(route[0]), view_func=gen_endpoint_func(route[1]),
                             methods=['GET', 'PUT', 'POST', 'OPTIONS', 'DELETE', 'PATCH'])
        except Exception as e:
            LOG.warning("Add route failure %s", str(e))
            traceback.print_exc(file=sys.stdout)

    return app
