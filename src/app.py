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


if __name__ == '__main__':
    from services.ChapterService import ChapterService
    from repositorys.Repositories import ChapterRepository
    from services.caches import ChapterCache

    chapter_repository = ChapterRepository(database)
    chapter_cache: ChapterCache = ChapterCache(app, chapter_repository)
    chapter_service: ChapterService = ChapterService(chapter_repository, chapter_cache)
    app.run(debug=True, host='0.0.0.0', port=6901)
