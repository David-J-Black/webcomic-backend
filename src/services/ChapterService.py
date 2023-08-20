import traceback

from src.models.ChapterComponents import ComicPage, ComicChapter, ComicChapterExtended
from src.repositorys.Repositories import ChapterRepository
from src.services.caches import ChapterCache


class ChapterService:

    def __init__(self,
                 chapter_repository: ChapterRepository,
                 chapter_cache: ChapterCache
                 ):
        self._chapter_repository = chapter_repository
        self._chapter_cache = chapter_cache

    def upload_comic_page(self, chapter_number: int, page_number: int, image_data: bytes) -> str:
        """
        Used to save a page
        """
        try:

            chapter: ComicChapter = self._chapter_repository.get_chapter(chapter_number)

            # Is this a valid chapter?
            if chapter is None:
                raise Exception(f"Could not find chapter # {chapter_number}!")

            page = ComicPage(chapter_id=chapter.chapter_id,
                             page_number=page_number,
                             comic_image=image_data,
                             page_position='R',
                             status='A')

            # See whether our page is going to be left side or right side
            if page_number > 0:
                previous_page: ComicPage = self._chapter_repository.get_comic_page(1, page_number - 1)
                if previous_page is not None and previous_page.page_position == 'R':
                    page.page_position = 'L'

            success_page = self._chapter_repository.save_comic_page(page)
            if success_page is not None:
                return "Success"
            else:
                raise Exception('Unable to save page!')

        except Exception as e:
            print(traceback.format_exc())
            raise e

    def get_comic_page(self, chapter_number: int, page_number: int) -> bytes:
        """
        Retrieve a comic page
        :return:
        """
        try:
            chapter: ComicChapter = self._chapter_repository.get_chapter(chapter_number)
            if chapter is None:
                raise Exception(f"Could not find chapter # {chapter_number}!")

            page: ComicPage = self._chapter_repository.get_comic_page(chapter.chapter_id, page_number)
            return page.comic_image
        except Exception as e:
            print(traceback.format_exc())
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
