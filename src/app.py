from flask_sqlalchemy import SQLAlchemy
from flask import Flask, send_file, request, jsonify, Response
from typing import Dict
from flask_cors import CORS

from config import Config

app = Flask(__name__)
config: Config = Config()
app.config['SQLALCHEMY_DATABASE_URI'] = config.database_path
database = SQLAlchemy()
database.init_app(app)
CORS(app)
