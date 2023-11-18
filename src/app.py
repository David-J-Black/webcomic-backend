import config
from flask import Flask
from flask_cors import CORS
from logger import log, setup_logger
from database import database
from endpoints import comment_blueprint
from services import chapter_cache

setup_logger()
log.info('Starting App...')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.database_path
database.init_app(app)
chapter_cache.load(app)

# Initialize CORS
CORS(app)

# -- Initialize endpoints --
app.register_blueprint(comment_blueprint)


