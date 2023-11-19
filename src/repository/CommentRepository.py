from sqlalchemy import text
from models import CommentModel, Pagination, Comment
from flask_sqlalchemy import SQLAlchemy


class CommentRepository:

    def __init__(self, database: SQLAlchemy):
        self._db = database

    def get_page_comments(self, page_id: int, pagination: Pagination) -> list[Comment]:
        """
        Get a page of comments for the given page
        """
        query = text("select * from comment where status='A' and page_id=:page_id "
                     "order by create_dt limit :page_size offset :offset")
        variables = {"page_id": page_id, "page_size": pagination.page_size, "offset": pagination.get_offset()}
        comment_page: list[CommentModel] = self._db.session.execute(query, variables).fetchall()
        response: list[Comment] = []
        for comment in comment_page:
            response.append(Comment(comment))
        return response

    def save_comment(self, comment: CommentModel) -> CommentModel:
        self._db.session.add(comment)
        self._db.session.commit()
        return comment