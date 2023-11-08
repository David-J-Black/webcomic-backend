import logging
from typing import Dict, List

from models.ChapterComponents import ComicChapter, ComicPage, ComicChapterExtended, ComicPageExtended
from repositorys.Repositories import Repository
from flask import Flask


class ChapterCache:
    """
    Caches are nice, we use them to avoid touching the database.
    --
    Touching the database, I want to limit that to pages, because image files are intense
    """
    # Stores all chapters, you can retrieve a ComicChapterExtended if you supply the chapter's number
    _chapter_cache_by_number: Dict[int, ComicChapterExtended] = {}

    # Give the first dictionary a chapter number, and the second dictionary a page number
    _chapter_cache_by_id: Dict[int, ComicChapterExtended] = {}

    _comic_page_cache: Dict[int, Dict[int, ComicPageExtended]] = {}

    def __init__(self,
                 app: Flask,
                 repository: Repository):
        self._app = app
        self._repository = repository
        self.load()

    def load(self):
        with self._app.app_context():
            chapters: list[ComicChapter] = self._repository.get_all_chapters()

            for chapter in chapters:
                pages: List[ComicPage] = self._repository.get_all_chapter_pages_wo_image(chapter_id=chapter.chapter_id)
                extended_chapter = ComicChapterExtended(chapter, pages)

                self._chapter_cache_by_number[chapter.chapter_number] = extended_chapter
                self._chapter_cache_by_id[chapter.chapter_id] = extended_chapter

                # Load pages for this chapter!!
                self._comic_page_cache[chapter.chapter_number] = {}
                comic_page_cache_chapter: Dict[int, ComicPageExtended] = self._comic_page_cache[chapter.chapter_number]

                for page in pages:

                    # Check for errors...
                    if page.page_number is None:
                        print(f'WARNING: PAGE WITH NULL NUMBER {page.page_id}')
                    elif page.page_number in comic_page_cache_chapter:
                        print(f"WARNING: We already loaded this page!! [chapter:{chapter.chapter_number},"
                              f"page:{page.page_number}]")
                    else:

                        print(f'About to load page [ch: {chapter.chapter_number}, pg: {page.page_number}]', end='\t')
                        comic_page_cache_chapter[page.page_number] = ComicPageExtended(page, extended_chapter)

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

    def get_chapter_by_number(self, chapter_num) -> ComicChapterExtended:
        if chapter_num in self._chapter_cache_by_number:
            return self._chapter_cache_by_number[chapter_num]
        else:
            return None

    def get_chapter_by_id(self, chapter_id) -> ComicChapterExtended:
        if chapter_id in self._chapter_cache_by_id:
            return self._chapter_cache_by_id[chapter_id]
        else:
            return None

# TODO: Have this return a number for number of items loaded
    def refresh(self) -> None:
        self.load()

    def get_comic_page(self, chapter_number, page_number) -> ComicPageExtended:
        if chapter_number is None or page_number is None:
            print(f'Invalid information for retrieving comic page from cache! [ch:{chapter_number},pg:{page_number}]')

        return self._comic_page_cache[chapter_number][page_number]

    def get_first_chapter(self) -> ComicChapterExtended | None:
        """
        :return: The first chronological chapter in the entire comic
        """
        return_chapter: ComicChapterExtended | None = None
        for chapter_num in self._chapter_cache_by_number.keys():
            if return_chapter is None or chapter_num < return_chapter.comic_chapter.chapter_number:
                return_chapter = self._chapter_cache_by_number.get(chapter_num)
        return return_chapter

    def get_last_chapter(self) -> ComicChapterExtended | None:
        """
        :return: The first chronological chapter in the entire comic
        """
        return_chapter: ComicChapterExtended | None = None
        for chapter_num in self._chapter_cache_by_number.keys():
            if return_chapter is None or chapter_num > return_chapter.comic_chapter.chapter_number:
                return_chapter = self._chapter_cache_by_number.get(chapter_num)
        return return_chapter
