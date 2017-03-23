#!/bin/bash

python watch_config.py

gunicorn -k gevent --max-requests 1000 --access-logfile - --error-logfile - -b 0.0.0.0:5000 main:app


