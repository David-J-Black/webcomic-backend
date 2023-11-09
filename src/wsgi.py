from functools import wraps
from typing import Tuple

import flask
from flask_cors import CORS
from app import app, database
from flask import request, jsonify, Response, Request
from models.ChapterComponents import ComicPageExtended, ComicPage
from services.Services import ChapterService
from repositorys.Repositories import Repository
from services.caches import ChapterCache

chapter_repository = Repository(database)
chapter_cache: ChapterCache = ChapterCache(app, chapter_repository)
chapter_service: ChapterService = ChapterService(chapter_repository, chapter_cache)


def is_authenticated():
    # Grab the headers from the incoming request
    headers = flask.request.headers
    security_question: str | None = headers['doYouThinkImPretty']
    if security_question == 'yes':
        print('Request passed authentication')
    else:
        print(f'Request failed auth! {request.host_url}')
        return jsonify({'message': "Ah ah ah, you didn\'t say the magic word!"}), 403


def secure_route(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        result = is_authenticated()
        if result is not None:
            return result
        return jsonify({'message':'fuck you!'}), 403

    return wrapper


@app.route('/page/<int:chapter_number>/<int:page_number>', methods=['GET'])
def get_page(chapter_number: int, page_number: int):
    try:
        return Response(chapter_service.get_comic_page_image(chapter_number, page_number), content_type='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@secure_route
@app.route('/chapter/<int:chapter_number>', methods=['GET'])
def get_chapter(chapter_number: int) -> Response:
    # Flask/SQLAlchemy is fucky with imports
    from models.ChapterComponents import ComicChapterExtended
    try:
        response: ComicChapterExtended = chapter_service.get_chapter_extended(chapter_number)
        return jsonify(response.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)}, 500)

@secure_route
@app.route('/manage/refreshCaches')
def refresh_caches():
    try:
        chapter_cache.refresh()
        return jsonify({'Caches': 'refreshed! 👌'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@secure_route
@app.route('/pageInfo/<int:chapter_number>/<int:page_number>', methods=['GET'])
def get_page_info(chapter_number: int, page_number: int):
    try:
        comic_page_extended: ComicPageExtended = chapter_service.get_comic_page_info(chapter_number, page_number)
        return jsonify(comic_page_extended.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@secure_route
@app.route('/pages/first')
def get_first_page():
    try:
        comic_page: ComicPageExtended = chapter_service.get_first_page()
        return jsonify(comic_page.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@secure_route
@app.route('/pages/last')
def get_last_page():
    try:
        comic_page: ComicPageExtended = chapter_service.get_last_page()
        return jsonify(comic_page.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    CORS(app)
