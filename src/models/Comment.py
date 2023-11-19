from models import CommentModel


class Comment:
    """
    Something a reader has said on the comic
    """

    def __init__(self, model: CommentModel | dict[str, any]):
        if isinstance(model, CommentModel):
            self.comment_id = model.comment_id
            self.comment_guid = model.comment_guid
            self.page_id = model.page_id
            self.body = model.body
            self.owner = model.owner
            self.status = model.status
            self.create_dt = model.create_dt
            self.update_dt = model.create_dt

        else:
            self.comment_guid = model.get('commentGuid')
            self.page_id = model.get('pageId')
            self.body = model.get('body')
            self.author = model.get('author')
            self.status = model.get('status')
            self.create_dt = model.get('createDt')
            self.update_dt = model.get('createDt')

    def to_dto(self) -> dict[str, any]:
        return {
            "commentGuid": self.comment_guid,
            "body": self.body,
            "author": self.owner,
            "createDt": self.create_dt
        }

    def to_model(self) -> CommentModel:
        model = CommentModel()

        model.comment_guid = self.comment_guid
        model.page_id = self.page_id
        model.body = self.body
        model.author = self.author
        model.status = self.status
        model.create_dt = self.create_dt
        model.update_dt = self.update_dt
        return model

