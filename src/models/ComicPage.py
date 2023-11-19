from sqlalchemy import Date
from models import ComicPageModel, CommentModel
import uuid


class ComicPage:
    def __init__(self, model: ComicPageModel):
        self.page_id = model.page_id
        self.chapter_id = model.chapter_id
        self.page_number = model.page_number
        self.release_date = model.release_date
        self.description = model.description
        self.page_position = model.page_position
        self.image_name = model.image_name
        self.status = model.status
        self.create_dt = Date
        self.update_dt = Date


class Comment:
    """
    The things people leave on pages to hurt me
    """
    def __init__(self, model: CommentModel):
        self.comment_id = model.comment_id
        self.comment_guid = model.comment_guid
        self.page_id = model.page_id
        self.body = model.body
        self.owner = model.owner
        self.status = model.status
        self.create_dt = model.create_dt
        self.update_dt = model.create_dt
    #
    # def __init__(self, request: dict):
    #     self.comment_guid = uuid.uuid4()


    def to_dto(self) -> dict[str, any]:
        return {
            "comment_guid": self.comment_guid,
            "body": self.body,
            "author": self.owner,
            "create_dt": self.create_dt
        }


class ComicPageCached:
    """
    This is how a comic page is stored in the cash

    TODO: Make a constructor for this that takes in page comments
    """
    def __init__(self, comic_page: ComicPage,
                 comic_chapter_dict: dict):
        self.comic_page: ComicPage = comic_page
        self.comic_chapter = comic_chapter_dict

    def to_dto(self) -> dict[str, any]:
        """
        When we send comic page info to the frontend,
        the dto is the simplified versoin with only the
        stuff the frontend needs to know.
        :return:
        """
        return {
            "pageNumber": self.comic_page.page_number,
            "chapter": self.comic_chapter,
            "releaseDate": self.comic_page.release_date,
            "description": self.comic_page.description,
        }
