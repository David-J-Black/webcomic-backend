import traceback

from models import ComicChapterCached, ComicPage, ComicPageCached
from cache import chapter_cache


class PageService:

    def get_comic_page_image(self, chapter_number: int, page_number: int) -> bytes:
        """
        Retrieve the image file for a page
        :return:
        """
        try:
            chapter: ComicChapterCached = chapter_cache.get_chapter_by_number(chapter_number)

            if chapter is None:
                raise Exception(f"Could not find chapter # {chapter_number}!")

            page: ComicPage = chapter_cache.get_comic_page(chapter_number, page_number).comic_page

            # Let's read that frickin' file!! YEAH!
            response: bytes
            with open('../pages/' + page.image_name, 'rb') as file:
                response = file.read()
            return response
        except Exception as e:
            print(f'Error retrieving: image for page: [ch:{chapter_number},pg: {page_number}] {traceback.format_exc()}')
            raise e

    def get_comic_page(self, chapter_number: int, page_number: int) -> ComicPageCached:
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

        comic_page: ComicPageCached = chapter_cache.get_comic_page(chapter_number, page_number)

        return comic_page

    def get_first_page(self) -> ComicPageCached | None:
        """
        :return The first page chronologically in the entire comic:
        """
        try:
            chapter: ComicChapterCached = chapter_cache.get_first_chapter()
            if chapter is not None:
                return chapter_cache.get_comic_page(chapter_number=chapter.simple_chapter.chapter_number,
                                                    page_number=chapter.start_page_number)
        except Exception as e:
            print(traceback.format_exc())
            raise e

    def get_last_page(self) -> ComicPageCached | None:
        """
        :return The first page chronologically in the entire comic:
        """
        try:
            chapter: ComicChapterCached = chapter_cache.get_last_chapter()
            if chapter is not None:
                return chapter_cache.get_comic_page(chapter_number=chapter.simple_chapter.chapter_number,
                                                    page_number=chapter.end_page_number)
        except Exception as e:
            print(traceback.format_exc())
            raise e
