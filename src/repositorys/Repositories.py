from typing import List

from models.ChapterComponents import ComicPageModel, ComicChapterModel, ComicPage
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, TextClause


class Repository:

    def __init__(self, database: SQLAlchemy):
        self.db = database

    def get_comic_page_legacy(self, page_id: int) -> ComicPageModel:
        query = f"select * from comic_page where page_id = {page_id} and status = 'A'"
        comic_page = self.db.session.execute(query).fetchone()
        return ComicPageModel(comic_page.__dict__)

    def get_comic_page(self, chapter_id: int, page_number: int) -> ComicPageModel:
        """
        Retrieve a comic page using chapter number and page number
        :return:
        """
        query = text(
            f"select * from comic_page where page_number = {page_number} and chapter_id = {chapter_id} "
            f"and status = 'A'")
        comic_page = self.db.session.execute(query).fetchone()
        return comic_page

    def save_comic_page(self, comic_page: ComicPageModel):
        self.db.session.add(comic_page)
        self.db.session.commit()
        return comic_page

    def get_chapter(self, chapter_num: int) -> ComicChapterModel:
        query: TextClause = text(f"select * from comic_chapter where chapter_number = {chapter_num} and status = 'A'")
        comic_chapter: ComicChapterModel = self.db.session.execute(query).fetchone()
        return comic_chapter

    def get_all_chapters(self) -> list[ComicChapterModel]:
        query: TextClause = text(f"select * from comic_chapter where status = 'A'")
        comic_chapters: List[ComicChapterModel] = self.db.session.execute(query).fetchall()
        return comic_chapters

    def get_all_chapter_pages_wo_image(self, chapter_id: int) -> list[ComicPage]:
        """
        Get all the pages of a chapter w/o images in order
        :param chapter_id: Id of the chapter
        """
        query = text(f"select * from comic_page where chapter_id = {chapter_id} and status = 'A'" +
                     f" order by page_number asc")
        comic_pages: list[ComicPageModel] = self.db.session.execute(query).fetchall()
        response: list[ComicPage] = []
        for page in comic_pages:
            response.append(ComicPage(page))

        return response
