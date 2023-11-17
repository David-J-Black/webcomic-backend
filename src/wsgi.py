import traceback

import flask
from flask_cors import CORS

from app import app, database, log
from flask import jsonify, Response
from models.ChapterComponents import ComicPageCached
from services.Authentication import secure_route
from services.Services import ChapterService, AdminService
from repositorys.Repositories import Repository
from services.caches import ChapterCache

# ============================================================
# Initialize Webcomic Singletons
# ============================================================
chapter_repository = Repository(database)
chapter_cache: ChapterCache = ChapterCache(app, chapter_repository)
chapter_service: ChapterService = ChapterService(app, chapter_repository, chapter_cache)
admin_service = AdminService(app)


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
    from models.ChapterComponents import ComicChapterCached
    try:
        response: ComicChapterCached = chapter_service.get_chapter_extended(chapter_number)
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
        comic_page_extended: ComicPageCached = chapter_service.get_comic_page_info(chapter_number, page_number)
        return jsonify(comic_page_extended.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@secure_route
@app.route('/pages/first')
def get_first_page():
    try:
        comic_page: ComicPageCached = chapter_service.get_first_page()
        return jsonify(comic_page.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@secure_route
@app.route('/pages/last')
def get_last_page():
    try:
        comic_page: ComicPageCached = chapter_service.get_last_page()
        return jsonify(comic_page.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/chapter/all')
def get_all_chapters():
    try:
        log.info(f'Request to get all chapters')
        all_chapters = chapter_service.get_table_of_contents()
        return jsonify(all_chapters), 200

    except Exception as e:
        log.warn(f'Could not make response to getting all chapers! {traceback.format_exc()}')
        return flask.make_response('Ooops!', 500)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    CORS(app)
