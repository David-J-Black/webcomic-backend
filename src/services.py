# Initialize Services
from database import database
from repository import Repository
from service import ChapterCache, ChapterService, CommentService, AdminService

chapter_repository = Repository(database)
chapter_cache: ChapterCache = ChapterCache(chapter_repository)
chapter_service: ChapterService = ChapterService(chapter_repository, chapter_cache)
admin_service = AdminService()
comment_service = CommentService(chapter_service)