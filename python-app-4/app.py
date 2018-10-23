#!/usr/bin/env python

"""
Example of a painfully trivial Flask application without setting up uWSGI, and 
otherwise doing dumb things
"""

import logging
import json_logging
import os
import redis
import requests
import socket
import traceback
import sys
from flask import Flask, jsonify
from logging.config import dictConfig


app = Flask(__name__)
json_logging.ENABLE_JSON_LOGGING = True
json_logging.init(framework_name='flask')
json_logging.init_request_instrument(app)
logger = logging.getLogger("test-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


print(os.getenv('TIME_SERVICE'))


@app.route('/hello')
def index():
	time = requests.get(os.getenv(os.getenv('TIME_SERVICE')))
	last_hit = time.json()
	return 'According to the %s service, it was last hit at ' % last_hit['last_hit']


@app.route('/health_check')
def health_check():
	return jsonify({'status': 'ok', 'backend': socket.gethostname()}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
