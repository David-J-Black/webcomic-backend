import uuid

from logger import log
from models import Pagination, CommentModel, SystemException, SystemCode
from models.Comment import Comment
from repository import comment_repository
import service
import repository


class CommentService:
    """
    The guy that handles all of our tasks involving comments
    """

    def get_comments(self,
                     chapter_number: int,
                     page_number: int,
                     pagination: Pagination
                     ) -> list[dict]:
        # Get the page id
        page_id: int = service.chapter_service.get_page_id(chapter_number, page_number)
        comments: list[CommentModel] = repository.comment_repository.get_page_comments(page_id, pagination)

        # Time to serialize the comments in a more friendly way for the frontend
        response = []

        for comment in comments:
            response.append(comment.to_dto())
        return response

    def post_comment(self,
                     chapter_number: int,
                     page_number: int,
                     comment_request: dict) -> CommentModel:
        """
        Takes a comic DTO and converts it and saves it to the repository
        :return:
        """
        try:
            log.info(f'Processing Request to Post Comment [ch#:{chapter_number}, pg#:{page_number} comment{comment_request}]:...')

            # Validate chapter...
            chapter = service.chapter_service.get_chapter_extended(chapter_number)

            if chapter is None:
                raise SystemException('This isn\'t a fucking chapter!', SystemCode.INVALID_DATA.value() )

            # Validate page...
            page = service.page_service.get_comic_page(chapter_number, page_number)

            if page is None:
                raise SystemException('This isn\'t a fucking chapter!', SystemCode.INVALID_DATA.value() )

            comment = Comment(comment_request)
            comment.comment_guid = str(uuid.uuid4())
            comment.page_id = page.comic_page.page_id

            # TODO: Check comment for shitty language...

            # Turn comment into model...
            comment_model = comment.to_model()

            # Post Comment
            return comment_repository.save_comment(comment_model)
        except SystemException as se:
            raise se
        except Exception as e:
            log.error(f'Could not post comment!![{comment_request}]: {e}')
            raise e