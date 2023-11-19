from logger import log
from models import Pagination, Comment, SystemException, SystemCode
import service
import repository


class CommentService:

    def get_comments(self,
                     chapter_number: int,
                     page_number: int,
                     pagination: Pagination
                     ) -> list[dict]:
        # Get the page id
        page_id: int = service.chapter_service.get_page_id(chapter_number, page_number)
        comments: list[Comment] = repository.comment_repository.get_page_comments(page_id, pagination)

        # Time to serialize the comments in a more friendly way for the frontend
        response = []

        for comment in comments:
            response.append(comment.to_dto())
        return response

    def post_comments(selfself,
                      chapter_number: int,
                      page_number: int,
                      comment_body: dict ):
        log.info(f'Going to post comment')

        chapter = service.chapter_service.get_chapter_extended(chapter_number)

        if chapter is None:
            raise SystemException('This isn\'t a fucking chapter!', SystemCode.INVALID_DATA.value() )

        page = service.page_service.get_comic_page(chapter_number, page_number)

        if page is None:
            raise SystemException('This isn\'t a fucking chapter!', SystemCode.INVALID_DATA.value() )

