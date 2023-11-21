from models.models import ComicChapterModel
from models.ComicPage import ComicPage


# This is so much boiler plating! This fucking sucks!


class ComicChapter:
    """
    The bare minimum comic information stored in the comic_chapter row
    """
    def __init__(self, model: ComicChapterModel):
        self.chapter_id = model.chapter_id
        self.chapter_number = model.chapter_number
        self.title = model.title
        self.release_date = model.release_date
        self.description = model.description
        self.created_at = model.created_at
        self.updated_at = model.updated_at


class ComicChapterCached:
    page_count: int
    start_page_number: int
    end_page_number: int
    pages: list[ComicPage]
    previous_chapter: dict[str, any] = None
    next_chapter: dict[str, any] = None

    def __init__(self, comic_chapter: ComicChapter, pages: list[ComicPage]):
        self.simple_chapter: ComicChapter = comic_chapter
        self.page_count = len(pages)
        if pages:
            self.start_page_number = pages[0].page_number
            self.end_page_number = pages[-1].page_number
        else:
            self.start_page_number = 0
            self.end_page_number = 0

        # Set the chapter number in the pages (pages are raw from DB usually!
        for page in pages:
            page.chapter_number = self.simple_chapter.chapter_number

        self.pages: list[ComicPage] = pages

    def connect_neighbors(self, previous_chapter, next_chapter):
        self.previous_chapter = previous_chapter
        self.next_chapter = next_chapter

    def to_dto_no_neighbors(self) -> dict[str, any]:
        return {
            "number": self.simple_chapter.chapter_number,
            "title": self.simple_chapter.title,
            "releaseDate": self.simple_chapter.release_date,
            "description": self.simple_chapter.description,
            "firstPage": self.start_page_number,
            "lastPage": self.end_page_number,
            "pageCount": len(self.pages)
        }

    def to_dto(self) -> dict[str, any]:
        return {
            "number": self.simple_chapter.chapter_number,
            "title": self.simple_chapter.title,
            "releaseDate": self.simple_chapter.release_date,
            "description": self.simple_chapter.description,
            "firstPage": self.start_page_number,
            "lastPage": self.end_page_number,
            "previousChapter": self.previous_chapter,
            "nextChapter": self.next_chapter,
            "pageCount": len(self.pages)
        }


class TableOfContentsChapter:
    """
    The objects that make up the table of contents
    """
    def __init__(self, comic_chapter: ComicChapterCached):
        self.chapter_number: int = comic_chapter.simple_chapter.chapter_number
        self.description: str = comic_chapter.simple_chapter.description
        self.pages: list[ComicPage] = comic_chapter.pages
        self.title: str = comic_chapter.simple_chapter.title

    def to_dto(self) -> dict[str, any]:
        dto_pages: list[dict] = []
        keys = self.pages
        for page in self.pages:
            dto_page = {
                'pageNumber': page.page_number,
                'releaseDate': page.release_date,
                'description': page.description,
            }
            dto_pages.append(dto_page)

        return {
            'title': self.title,
            'chapterNumber': self.chapter_number,
            'description': self.description,
            'pages': dto_pages
        }
# ===== Elements of a page =====
# self.page_id = model.page_id
# self.chapter_id = model.chapter_id
# self.page_number = model.page_number
# self.release_date = model.release_date
# self.description = model.description
# self.page_position = model.page_position
# self.image_name = model.image_name
# # image_data: bytes
# self.status = model.status
# self.created_at = model.created_at
# self.updated_at = model.updated_at