import traceback
from typing import Dict, List
from flask import Blueprint
from models import (
    ComicChapterCached,
    ComicPageCached,
    TableOfContentsChapter
)
from cache import chapter_cache
from logger import log
chapter_blueprint = Blueprint('chapter', __name__)


class ChapterService:

    def get_chapter_extended(self, chapter_number: int) -> ComicChapterCached:
        """
        Compiles all relevant chapter information for the frontend
        :param chapter_number: Which chapter is this?
        :return:
        """

        try:
            chapter_info: ComicChapterCached = chapter_cache.get_chapter_by_number(chapter_number)
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

    def get_page_id(self, chapter_number: int, page_number: int):
        page: ComicPageCached = chapter_cache.get_comic_page(chapter_number, page_number)

        if page is None:
            log.warning(f'No page found for get_page_id(chapter_number:{chapter_number}, page_number: {page_number}')
            return None

        return page.comic_page.page_id


    def get_table_of_contents(self) -> List[Dict]:
        """
        Returns the table of contents of all chapters in the comic.

        :return: A list of dictionaries representing the table of contents. Each dictionary
            contains the information of a chapter, including its key, title, and other relevant details.
        :rtype: List[Dict]
        """
        try:
            all_chapters: Dict[int, ComicChapterCached] = chapter_cache.get_all_chapters()
            response: List[Dict] = []

            for chapter_key in all_chapters.keys():
                chapter: ComicChapterCached = all_chapters.get(chapter_key)
                simplified_chapter = TableOfContentsChapter(chapter)
                response.append(simplified_chapter.to_dto())
            return response

        except Exception as e:
            log.warning(f'Error Trying to get all chapters: {traceback.format_exc()}')
            raise e
