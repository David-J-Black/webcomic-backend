import traceback

from models.ChapterComponents import ComicPage, ComicChapter, ComicChapterExtended, ComicPageExtended
from repositorys.Repositories import Repository
from services.caches import ChapterCache


class ChapterService:

    def __init__(self,
                 chapter_repository: Repository,
                 chapter_cache: ChapterCache
                 ):
        self._chapter_repository = chapter_repository
        self._chapter_cache = chapter_cache

    def get_comic_page_image(self, chapter_number: int, page_number: int) -> bytes:
        """
        Retrieve the image file for a page
        :return:
        """
        try:
            chapter: ComicChapterExtended = self._chapter_cache.get_chapter_by_number(chapter_number)

            if chapter is None:
                raise Exception(f"Could not find chapter # {chapter_number}!")

            page: ComicPage = self._chapter_cache.get_comic_page(chapter_number, page_number).comic_page;

            # Let's read that frickin' file!! YEAH!
            response: bytes
            with open('../pages/' + page.image_name, 'rb') as file:
                response = file.read()
            return response
        except Exception as e:
            print(f'Error retrieving: image for page: [ch:{chapter_number},pg: {page_number}] {traceback.format_exc()}')
            raise e

    def get_comic_page_info(self, chapter_number: int, page_number: int) -> ComicPageExtended:
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

        comic_page: ComicPageExtended = self._chapter_cache.get_comic_page(chapter_number, page_number)

        return comic_page

    def get_chapter_extended(self, chapter_number: int) -> ComicChapterExtended:
        """
        Compiles all relevant chapter information for the frontend
        :param chapter_number: Which chapter is this?
        :return:
        """

        try:
            chapter_info: ComicChapterExtended = self._chapter_cache.get_chapter_by_number(chapter_number)
            if chapter_info is None:
                raise Exception(f"Could not find chapter # {chapter_number}!")

            return chapter_info

        except Exception as e:
            print(traceback.format_exc())
            raise e

    def get_first_page(self) -> ComicPageExtended | None:
        """
        :return The first page chronologically in the entire comic:
        """
        try:
            chapter: ComicChapterExtended = self._chapter_cache.get_first_chapter()
            if chapter is not None:
                return self._chapter_cache.get_comic_page(chapter_number=chapter.comic_chapter.chapter_number,
                                                          page_number=chapter.start_page_number)
        except Exception as e:
            print(traceback.format_exc())
            raise e

    def get_last_page(self) -> ComicPageExtended | None:
        """
        :return The first page chronologically in the entire comic:
        """
        try:
            chapter: ComicChapterExtended = self._chapter_cache.get_last_chapter()
            if chapter is not None:
                return self._chapter_cache.get_comic_page(chapter_number=chapter.comic_chapter.chapter_number,
                                                          page_number=chapter.end_page_number)
        except Exception as e:
            print(traceback.format_exc())
            raise e