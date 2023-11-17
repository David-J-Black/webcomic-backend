import traceback
from typing import Dict
from flask import Blueprint, Flask, jsonify, request
from app import log
from models.ChapterComponents import ComicChapterCached, ComicPageCached, \
    TableOfContentsChapter, ComicPage
from repositorys.Repositories import Repository
from services.Authentication import admin_secure
from services.caches import ChapterCache

chapter_blueprint = Blueprint('chapter', __name__)


class ChapterService(Blueprint):

    def __init__(self,
                 app: Flask,
                 chapter_repository: Repository,
                 chapter_cache: ChapterCache
                 ):
        super().__init__('chapter', __name__)
        app.register_blueprint(chapter_blueprint, url_prefix='/admin')
        self._chapter_repository = chapter_repository
        self._chapter_cache = chapter_cache

    def get_comic_page_image(self, chapter_number: int, page_number: int) -> bytes:
        """
        Retrieve the image file for a page
        :return:
        """
        try:
            chapter: ComicChapterCached = self._chapter_cache.get_chapter_by_number(chapter_number)

            if chapter is None:
                raise Exception(f"Could not find chapter # {chapter_number}!")

            page: ComicPage = self._chapter_cache.get_comic_page(chapter_number, page_number).comic_page

            # Let's read that frickin' file!! YEAH!
            response: bytes
            with open('../pages/' + page.image_name, 'rb') as file:
                response = file.read()
            return response
        except Exception as e:
            print(f'Error retrieving: image for page: [ch:{chapter_number},pg: {page_number}] {traceback.format_exc()}')
            raise e

    def get_comic_page_info(self, chapter_number: int, page_number: int) -> ComicPageCached:
        """
        Get all the essential info that someone would want from a comic page... (except the image lmao)
        - Release Date
        - Chapter Number
        - Page Number
        - Author Comment
        - Any comments on the page
        """
        if chapter_number is None or page_number is None:
            print(f"Invalid chapter or page number, get out of here fuck-o!! [ch: {chapter_number}, pg: {page_number}]")

        comic_page: ComicPageCached = self._chapter_cache.get_comic_page(chapter_number, page_number)

        return comic_page

    def get_chapter_extended(self, chapter_number: int) -> ComicChapterCached:
        """
        Compiles all relevant chapter information for the frontend
        :param chapter_number: Which chapter is this?
        :return:
        """

        try:
            chapter_info: ComicChapterCached = self._chapter_cache.get_chapter_by_number(chapter_number)
            if chapter_info is None:
                raise Exception(f"Could not find chapter # {chapter_number}!")

            return chapter_info

        except Exception as e:
            print(traceback.format_exc())
            raise e

    def get_all(self):
        """
        Get the entire chapter cache
        :return:
        """
    def get_first_page(self) -> ComicPageCached | None:
        """
        :return The first page chronologically in the entire comic:
        """
        try:
            chapter: ComicChapterCached = self._chapter_cache.get_first_chapter()
            if chapter is not None:
                return self._chapter_cache.get_comic_page(chapter_number=chapter.simple_chapter.chapter_number,
                                                          page_number=chapter.start_page_number)
        except Exception as e:
            print(traceback.format_exc())
            raise e

    def get_last_page(self) -> ComicPageCached | None:
        """
        :return The first page chronologically in the entire comic:
        """
        try:
            chapter: ComicChapterCached = self._chapter_cache.get_last_chapter()
            if chapter is not None:
                return self._chapter_cache.get_comic_page(chapter_number=chapter.simple_chapter.chapter_number,
                                                          page_number=chapter.end_page_number)
        except Exception as e:
            print(traceback.format_exc())
            raise e

    def get_table_of_contents(self) -> dict[int, dict]:
        try:
            all_chapters: Dict[int, ComicChapterCached] = self._chapter_cache.get_all_chapters()
            response: dict = {}

            for chapter_key in all_chapters.keys():
                chapter: ComicChapterCached = all_chapters.get(chapter_key)
                simplified_chapter = TableOfContentsChapter(chapter)
                response[chapter_key] = simplified_chapter.to_dto()
            return response

        except Exception as e:
            log.warn(f'Error Trying to get all chapters: {traceback.format_exc()}')
            raise e


class AdminService(Blueprint):
    """
    The thing in charge of all the admin functions
    """

    def __init__(self, app: Flask):
        super().__init__('admin', __name__)
        self.register_routes()
        app.register_blueprint(self, url_prefix='/admin')
        log.info('Initializing Admin Service')

    def register_routes(self):
        """
        ==========================================
        Initializes all the routes for the server
        ==========================================
        We need
        - upload page
        - delete page
        - delete comment
        - author comment

        """
        self.add_url_rule(
            '/upload-one/<chapter_number>/<page_number>',
            'upload_page',
            self.upload_page,
            methods=['POST', 'PUT']
        )

    @admin_secure
    def upload_page(self, chapter_number: int, page_number: int):

        try:
            log.info(f'Request to upload page: Ch:{chapter_number}, pg:{page_number}')
            print('test')
            # TODO:  upload page
            req = request
            print(req)


            return jsonify({'messge': 'Success'}), 200

        except Exception as e:
            log.warn('Problem uploading page', traceback.format_exc())
            return jsonify({'messge': 'Failure'}), 403
