import flask
from flask import Blueprint, jsonify
from models import ComicPageCached
from service import page_service
from decorators import secure_route

comic_page_endpoints = Blueprint('comic_page', __name__)


@comic_page_endpoints.route('/page/<int:chapter_number>/<int:page_number>', methods=['GET'])
def get_page(chapter_number: int, page_number: int):
    try:
        return flask.make_response(page_service.get_comic_page_image(chapter_number, page_number))
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@secure_route
@comic_page_endpoints.route('/pages/first')
def get_first_page():
    try:
        comic_page: ComicPageCached = page_service.get_first_page()
        return jsonify(comic_page.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@secure_route
@comic_page_endpoints.route('/pages/last')
def get_last_page():
    try:
        comic_page: ComicPageCached = page_service.get_last_page()
        return jsonify(comic_page.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@secure_route
@comic_page_endpoints.route('/pageInfo/<int:chapter_number>/<int:page_number>', methods=['GET'])
def get_page_info(chapter_number: int, page_number: int):
    try:
        comic_page_extended: ComicPageCached = page_service.get_comic_page(chapter_number, page_number)
        return jsonify(comic_page_extended.to_dto())
    except Exception as e:
        return jsonify({'error': str(e)}), 500