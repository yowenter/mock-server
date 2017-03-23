from flask import Flask
from flask.ext.cors import CORS

cors = CORS()
app = Flask(__name__)
cors.init_app(app)
