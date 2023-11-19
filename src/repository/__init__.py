from database import database
from .ComicChapterRepository import ComicChapterRepository
from .ComicPageRepository import ComicPageRepository
from .CommentRepository import CommentRepository

page_repository = ComicPageRepository(database)
chapter_repository = ComicChapterRepository(database)
comment_repository = CommentRepository(database)
