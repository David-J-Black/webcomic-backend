from app import app, database
from flask import Flask, send_file, request, jsonify, Response

from services.ChapterService import ChapterService
from repositorys.Repositories import ChapterRepository
from services.caches import ChapterCache

chapter_repository = ChapterRepository(database)
chapter_cache: ChapterCache = ChapterCache(app, chapter_repository)
chapter_service: ChapterService = ChapterService(chapter_repository, chapter_cache)

@app.route('/pageOld/<int:page_number>')
def get_page(page_number):

    formatted_page_number = str(page_number).zfill(3)
    return send_file(f'../pages/Looking For Darwin_{formatted_page_number}.png', mimetype='image/png')


@app.route('/page/<int:chapter_number>/<int:page_number>', methods=['GET'])
def get_page2(chapter_number: int, page_number: int):
    try:
        return Response(chapter_service.get_comic_page_image(chapter_number, page_number), content_type='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/chapter/<int:chapter_number>')
def get_chapter(chapter_number: int) -> Response:
    # Flask/SQLAlchemy is fucky with imports
    from models.ChapterComponents import ComicChapterExtended
    try:
        response: ComicChapterExtended = chapter_service.get_chapter(chapter_number)
        return jsonify(response.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)},  500)


@app.route('/manage/refreshCaches')
def refresh_caches():
    try:
        chapter_cache.refresh()
        return jsonify({'Caches': 'refreshed!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':

    app.run()