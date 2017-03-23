# -*- encoding:utf-8 -*-


import os
import ConfigParser

from app import app
import json

from flask import jsonify

JSON_FILES_DIR = os.path.join(os.path.dirname(__file__), 'json_files')

if os.path.exists(os.path.join(os.path.dirname(__file__), 'routes.cfg')):
    print "READING ROUTES CONFIG "
    config = ConfigParser.ConfigParser()
    config.read('routes.cfg')
    _routes = config._sections.get("routes").items()
    routes = set()
    for _r in _routes:
        if not str(_r[0]).startswith('__'):
            routes.add(_r)

    print "ROUTES :", routes
else:
    routes = (
        ('/ping', 'ping.json'),
    )



def gen_endpoint_func(json_file_name):
    def f():
        json_file = os.path.join(JSON_FILES_DIR, json_file_name)
        assert os.path.exists(json_file), "json_file `%s` not exists" % json_file
        with open(os.path.join(JSON_FILES_DIR, json_file_name), 'r') as f:
            return jsonify(json.load(f))

    return f


def register_routes(application):
    for route in routes:
        application.add_url_rule(route[0], view_func=gen_endpoint_func(route[1]),
                                 methods=['GET', 'PUT', 'POST', 'OPTIONS', 'DELETE', 'PATCH'])

    return application
