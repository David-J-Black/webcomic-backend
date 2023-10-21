from flask_sqlalchemy import SQLAlchemy
from flask import Flask, send_file, request, jsonify, Response
from typing import Dict
from config import read_config
from flask_cors import CORS

app = Flask(__name__)
config: Dict = read_config('../configuration/config.yml')
app.config['SQLALCHEMY_DATABASE_URI'] = config['database-config']['uri']
database = SQLAlchemy()
database.init_app(app)
CORS(app)
