from .ChapterService import ChapterService
from .CommentService import CommentService
from .Authentication import admin_secure
from .PageService import PageService

chapter_service = ChapterService()
page_service = PageService()
comment_service = CommentService()