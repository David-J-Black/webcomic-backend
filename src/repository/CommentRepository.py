from sqlalchemy import text
from models import Comment, CommentModel, Pagination
from app import database


class CommentRepository:

    @staticmethod
    def get_page_comments(page_id: int, pagination: Pagination) -> list[Comment]:
        query = text("select * from comment where status='A' and page_id=:page_id "
                     "order by create_dt limit :page_size offset :offset")
        variables = {"page_id": page_id, "page_size": pagination.page_size, "offset": pagination.get_offset()}
        comment_page: list[CommentModel] = database.session.execute(query, variables).fetchall()
        response: list[Comment] = []
        for comment in comment_page:
            response.append(Comment(comment))
        return response
