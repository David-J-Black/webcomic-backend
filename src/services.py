from service import ChapterCache, ChapterService, CommentService, AdminService
from repository import chapter_repository

chapter_cache: ChapterCache = ChapterCache()
chapter_service: ChapterService = ChapterService(chapter_repository, chapter_cache)
admin_service = AdminService()
comment_service = CommentService(chapter_service)