from flask_sqlalchemy import SQLAlchemy
from flask import Flask, send_file, request, jsonify, Response
from typing import Dict
from src.config import read_config
from flask_cors import CORS

app = Flask(__name__)
config: Dict = read_config('../configuration/config.yml')
app.config['SQLALCHEMY_DATABASE_URI'] = config['database-config']['uri']
database = SQLAlchemy()
database.init_app(app)
CORS(app)


@app.route('/pageOld/<int:page_number>')
def get_page(page_number):

    formatted_page_number = str(page_number).zfill(3)
    return send_file(f'../pages/Looking For Darwin_{formatted_page_number}.png', mimetype='image/png')


@app.route('/page/<int:chapter_number>/<int:page_number>', methods=['GET'])
def get_page2(chapter_number: int, page_number: int):
    try:
        return Response(chapter_service.get_comic_page(chapter_number, page_number), content_type='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/chapter/<int:chapter_number>')
def get_chapter(chapter_number: int) -> Response:
    # Flask/SQLAlchemy is fucky with imports
    from src.models.ChapterComponents import ComicChapterExtended
    try:
        response: ComicChapterExtended = chapter_service.get_chapter(chapter_number)
        return jsonify(response.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)},  500)


@app.route('/manage/uploadPage/<int:chapter_number>/<int:page_number>', methods=['POST'])
def upload_page(chapter_number, page_number):
    try:
        image_data: bytes = request.get_data()
        return chapter_service.upload_comic_page(chapter_number, page_number, image_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    from src.services.ChapterService import ChapterService
    from src.repositorys.Repositories import ChapterRepository
    from src.services.caches import ChapterCache

    chapter_repository = ChapterRepository(database)
    chapter_cache: ChapterCache = ChapterCache(app, chapter_repository)
    chapter_service: ChapterService = ChapterService(chapter_repository, chapter_cache)
    app.run(debug=True, host='0.0.0.0', port=6901)
