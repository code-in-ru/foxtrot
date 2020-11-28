from flask import Flask
from config import Config
from flask_cors import CORS

webapp = Flask(__name__)
CORS(webapp, resources={r"/api/*": {"origins": "*"}})
webapp.config.from_object(Config)

from webapp import routes
