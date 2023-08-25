from typing import List

from src.models.ChapterComponents import ComicPage, ComicChapter
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text


class ChapterRepository:

    def __init__(self, database: SQLAlchemy):
        self.db = database
        print('test2')

    def get_comic_page_legacy(self, page_id: int) -> ComicPage:
        query = f"select * from comic_page where page_id = {page_id} and status = 'A'"
        comic_page = self.db.session.execute(query).fetchone()
        return comic_page

    def get_comic_page(self, chapter_id: int, page_number: int) -> ComicPage:
        """
        Retrieve a comic page using chapter number and page number
        :return:
        """
        query = text(
            f"select * from comic_page where page_number = {page_number} and chapter_id = {chapter_id} "
            f"and status = 'A'")
        comic_page = self.db.session.execute(query).fetchone()
        return comic_page

    def save_comic_page(self, comic_page: ComicPage):
        self.db.session.add(comic_page)
        self.db.session.commit()
        return comic_page

    def get_chapter(self, chapter_num: int) -> ComicChapter:
        query = text(f"select * from comic_chapter where chapter_number = {chapter_num} and status = 'A'")
        comic_chapter = self.db.session.execute(query).fetchone()
        return comic_chapter

    def get_all_chapters(self) -> list[ComicChapter]:
        query = text(f"select * from comic_chapter where status = 'A'")
        comic_chapters: List[ComicChapter] = self.db.session.execute(query).fetchall()
        return comic_chapters

    def get_all_chapter_pages_wo_image(self, chapter_id: int) -> list[ComicPage]:
        """
        Get all the pages of a chapter w/o images in order
        :param chapter_id: Id of the chapter
        """
        query = text(f"select * from comic_page where chapter_id = {chapter_id} and status = 'A'" +
                     f" order by page_number asc")
        comic_page = self.db.session.execute(query).fetchall()
        return comic_page
