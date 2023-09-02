import traceback

from models.ChapterComponents import ComicPage, ComicChapter, ComicChapterExtended
from repositorys.Repositories import ChapterRepository
from services.caches import ChapterCache


class ChapterService:

    def __init__(self,
                 chapter_repository: ChapterRepository,
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
            chapter: ComicChapter = self._chapter_repository.get_chapter(chapter_number)
            if chapter is None:
                raise Exception(f"Could not find chapter # {chapter_number}!")

            page: ComicPage = self._chapter_repository.get_comic_page(chapter.chapter_id, page_number)

            # Let's read that frickin' file!! YEAH!
            response: bytearray
            with open('../pages/' + page.image_name, 'rb') as file:
                response = file.read()
            return response
        except Exception as e:
            print(f'Error retrieving: image for page: [ch:{chapter_number},pg: {page_number}] {traceback.format_exc()}')
            raise e

    def get_chapter(self, chapter_number: int) -> ComicChapterExtended:
        """
        Retrieves chapter information for the frontend
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
