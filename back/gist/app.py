from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from peewee import PostgresqlDatabase
from gist.config import *
import logging

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
db = PostgresqlDatabase(db_name, user=db_user, password=db_pass, host=db_host)

logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
