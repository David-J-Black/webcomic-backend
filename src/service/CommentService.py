from models import Pagination, Comment
from service import ChapterService
from repository import CommentRepository


class CommentService:

    def __init__(self,
                 chapter_service: ChapterService
                 ):
        self._chapter_service = chapter_service

    def get_comments(self,
                     chapter_number: int,
                     page_number: int,
                     pagination: Pagination
                     ) -> list[dict]:
        # Get the page id
        page_id: int = self._chapter_service.get_page_id(chapter_number, page_number)
        comments: list[Comment] = CommentRepository.get_page_comments(page_id, pagination)

        # Time to serialize the comments in a more friendly way for the frontend
        response = []

        for comment in comments:
            response.append(comment.to_dto())
        return response
