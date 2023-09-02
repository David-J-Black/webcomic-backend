from datetime import datetime
from typing import List, Dict

from app import database


class ComicPage(database.Model):
    page_id = database.Column(database.Integer, primary_key=True)
    chapter_id = database.Column(database.Integer)
    page_number = database.Column(database.Integer)
    release_date = database.Column(database.Date, default=datetime.utcnow())
    description = database.Column(database.String)
    page_position = database.Column(database.String(1))
    image_name = database.Column(database.String(30))
    # image_data: bytes
    status = database.Column(database.String(1))
    created_at = database.Column(database.Date, default=datetime.utcnow())
    updated_at = database.Column(database.Date, default=datetime.utcnow())

    def __repr__(self):
        return f'<Page: ChapterID{self.chapter_id}: Page Number;{self.page_number}>'



class ComicChapter(database.Model):
    chapter_id = database.Column(database.Integer, primary_key=True)
    chapter_number = database.Column(database.Integer)
    title = database.Column(database.String)
    release_date = database.Column(database.Date)
    description = database.Column(database.String)
    created_at = database.Column(database.Date)
    updated_at = database.Column(database.Date)

    def __repr__(self):
        return f'<Page: ChapterID{self.chapter_id}: Page Number;{self.page_number}>'


class ComicChapterExtended:

    page_count: int
    start_page_number: int
    end_page_number: int
    pages: list[ComicPage]
    previous_chapter: Dict[str, any] = None
    next_chapter: Dict[str, any] = None

    def __init__(self, comic_chapter: ComicChapter, pages: list[ComicPage]):
        self.comic_chapter = comic_chapter
        self.set_page_info(pages)

    def set_page_info(self, pages: list[ComicPage]) -> None:
        self.page_count = len(pages)
        if pages:
            self.start_page_number = pages[0].page_number
            self.end_page_number = pages[-1].page_number
        else:
            self.start_page_number = 0
            self.end_page_number = 0
        self.pages = pages

    def connect_neighbors(self, previous_chapter, next_chapter):
        self.previous_chapter = previous_chapter
        self.next_chapter = next_chapter

    def to_dto_no_neighbors(self) -> Dict[str, any]:
        return {
            "number": self.comic_chapter.chapter_number,
            "title": self.comic_chapter.title,
            "releaseDate": self.comic_chapter.release_date,
            "description": self.comic_chapter.description,
            "firstPage": self.start_page_number,
            "lastPage": self.end_page_number,
            "pageCount": len(self.pages)
    }

    def to_dto(self) -> Dict[str, any]:
        return {
            "number": self.comic_chapter.chapter_number,
            "title": self.comic_chapter.title,
            "releaseDate": self.comic_chapter.release_date,
            "description": self.comic_chapter.description,
            "firstPage": self.start_page_number,
            "lastPage": self.end_page_number,
            "previousChapter": self.previous_chapter,
            "nextChapter": self.next_chapter,
            "pageCount": len(self.pages)
        }

