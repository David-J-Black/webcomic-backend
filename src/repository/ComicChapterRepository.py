from typing import List
from flask_sqlalchemy import SQLAlchemy
from models.ChapterComponents import ComicChapterModel
from sqlalchemy import text, TextClause


class ComicChapterRepository:

    def __init__(self, database: SQLAlchemy):
        self.db = database

    def get_chapter(self, chapter_num: int) -> ComicChapterModel:
        query: TextClause = text("select * from comic_chapter where chapter_number = :chapter_num and status = 'A'")
        comic_chapter: ComicChapterModel = self.db.session.execute(query, {"chapter_num": chapter_num}).fetchone()
        return comic_chapter

    def get_all_chapters(self) -> list[ComicChapterModel]:
        """
        :return: Every Active chapter in the comic
        """
        query: TextClause = text("select * from comic_chapter where status = 'A'")
        comic_chapters: List[ComicChapterModel] = self.db.session.execute(query).fetchall()
        return comic_chapters
