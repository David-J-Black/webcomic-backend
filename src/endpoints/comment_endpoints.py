import json

import flask
from flask import Blueprint, jsonify, request, make_response
from models import Pagination
from service import comment_service
from logger import log
from models import SystemException
from decorators import secure_route

comment_endpoints = Blueprint('comment', __name__, url_prefix='/comment')


@comment_endpoints.route('/<int:chapter_number>/<int:page_number>', methods=['GET'])
@secure_route
def get_comments(chapter_number: int, page_number: int):
    """
    Get comments for an indicated page
    """
    try:
        log.info('Request to get comments')
        pagination_page_size = int(request.args.get('pageSize'))
        pagination_page_number = int(request.args.get('pageNumber')) # Not a ComicPage number! See pagination
        pagination = Pagination(pagination_page_size, pagination_page_number)
        comments: list[dict] = comment_service.get_comments(chapter_number, page_number, pagination)
        response = make_response(comments)
        response.status_code=200
        response.headers['Content-Type'] = 'application/json'
        return response
    except SystemException as se:
        return jsonify({'message': str(se)}), se.code.value
    except Exception as e:
        log.warning(f'Ran into a problem trying to get comments!'
                    f'[chapter_number: {chapter_number}, page_number: {page_number}]', exc_info=e)
        return jsonify({'message': 'Problem getting comments'}), 500


@comment_endpoints.route('/<int:chapter_number>/<int:page_number>', methods=['POST'])
@secure_route
def post_comment(chapter_number: int, page_number):
    try:
        log.info(f'Got a request to post a comment [ch: {chapter_number}, pg: {page_number}]')
        comment_request = request

        request_json = request.get_json()
        request_json['authorIp'] = json.dumps(comment_request.access_route)
        saved_comment: dict = comment_service.post_comment(chapter_number, page_number, request_json)

        return flask.make_response(saved_comment.get('comment_guid'))

    except SystemException as se:
        return jsonify({'message': 'Problem getting comments...'}), se.code.value

    except Exception as e:
        log.warning(f'Ran into a problem trying to get comments!'
                    f'[chapter_number: {chapter_number}, page_number: {page_number}]', exc_info=e)
        return jsonify({'message': 'Problem posting comments'}), 500