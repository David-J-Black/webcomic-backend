import config
from flask import Flask
from flask_cors import CORS

from endpoints import chapter_blueprint, comic_page_blueprint, comment_blueprint
from logger import log, setup_logger
from database import database
from cache import chapter_cache

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
app.register_blueprint(chapter_blueprint)
app.register_blueprint(comic_page_blueprint)


