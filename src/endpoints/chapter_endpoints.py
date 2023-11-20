import traceback
from flask import Blueprint, Response, jsonify, make_response
from models import SystemException
from decorators import secure_route
from service import chapter_service
from cache import chapter_cache
from logger import log

chapter_endpoints = Blueprint('chapter', __name__)


@secure_route
@chapter_endpoints.route('/chapter/<int:chapter_number>', methods=['GET'])
def get_chapter(chapter_number: int) -> Response:
    # Flask/SQLAlchemy is fucky with imports
    from models.ChapterComponents import ComicChapterCached
    try:
        response: ComicChapterCached = chapter_service.get_chapter_extended(chapter_number)
        return jsonify(response.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)}, 500)


@secure_route
@chapter_endpoints.route('/manage/refreshCaches')
def refresh_caches():
    try:
        chapter_cache.refresh()
        return jsonify({'Caches': 'refreshed! 👌'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@secure_route
@chapter_endpoints.route('/chapter/all')
def get_all_chapters():
    try:
        log.info(f'Request to get all chapters')
        all_chapters = chapter_service.get_table_of_contents()
        return jsonify(all_chapters), 200

    except SystemException as se:
        return make_response('Ran into an issue, sorry babe', se.code)

    except Exception as e:
        log.warning(f'Could not make response to getting all chapers!{e}:{traceback.format_exc()}')
        return make_response('Ooops!', 500)
