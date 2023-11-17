import logging
import sys

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS

from config import Config

app = Flask(__name__)
webcomic_config: Config = Config()

# ============================================================
# Initialize logger
# ============================================================

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=webcomic_config.log_location,
                    filemode='a') # Append to log file, don't overwrite
handler = logging.StreamHandler(sys.stdout)
log = logging.getLogger('webcomicLogger')
log.addHandler(handler)

app.config['SQLALCHEMY_DATABASE_URI'] = webcomic_config.database_path
database = SQLAlchemy()
database.init_app(app)
CORS(app)
