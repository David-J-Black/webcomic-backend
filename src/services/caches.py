from typing import Dict, List

from src.models.ChapterComponents import ComicChapter, ComicPage, ComicChapterExtended
from src.repositorys.Repositories import ChapterRepository
from flask import Flask


class ChapterCache:
    """
    Caches are nice, we use them to avoid touching the database.
    --
    Touching the database, I want to limit that to pages, because image files are intense
    """
    # The key for this dict is the chapter_num
    _chapter_cache_by_number: Dict[int, ComicChapterExtended] = {}
    _chapter_cache_by_id: Dict[int, ComicChapterExtended] = {}

    def __init__(self,
                 app: Flask,
                 chapter_repository: ChapterRepository):
        self._app = app
        self._chapter_repository = chapter_repository
        self.load()

    def load(self):
        with self._app.app_context():
            chapters: list[ComicChapter] = self._chapter_repository.get_all_chapters()

            for chapter in chapters:
                pages: list[ComicPage] = self._chapter_repository.get_all_chapter_pages_wo_image(chapter.chapter_id)
                extended_chapter = ComicChapterExtended(chapter, pages)

                self._chapter_cache_by_number[chapter.chapter_number] = extended_chapter
                self._chapter_cache_by_id[chapter.chapter_id] = extended_chapter

            # Ok time to connect chapters
            for chapter in chapters:
                self.set_neighbor_info(chapter.chapter_number)

    def set_neighbor_info(self, chapter_number: int) -> None:
        """
        Each chapter extended should have a reference to the preceeding chapter and next chapter
        :param chapter_number: Chapter we want connect neighbors too
        """
        chapter = self._chapter_cache_by_number[chapter_number]
        previous_chapter = self.get_chapter_by_number(chapter_number - 1)
        next_chapter = self.get_chapter_by_number(chapter_number + 1)

        # Trying to avoid null pointer exceptions fuck shit ass
        prev_dto = None
        next_dto = None
        if previous_chapter:
            prev_dto = previous_chapter.to_dto_no_neighbors()
        if next_chapter:
            next_dto = next_chapter.to_dto_no_neighbors()

        chapter.connect_neighbors(previous_chapter=prev_dto,
                                  next_chapter=next_dto)

    def get_chapter_by_number(self, chapter_num) -> ComicChapterExtended | None:
        if chapter_num in self._chapter_cache_by_number:
            return self._chapter_cache_by_number[chapter_num]
        else:
            return None

    def get_chapter_by_id(self, chapter_id) -> ComicChapterExtended | None:
        if chapter_id in self._chapter_cache_by_id:
            return self._chapter_cache_by_id[chapter_id]
        else:
            return None

# TODO: Have this return a number for number of items loaded
    def refresh(self) -> None:
        self.load()