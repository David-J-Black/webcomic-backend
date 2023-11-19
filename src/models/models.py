from datetime import datetime
from database import database


class ComicPageModel(database.Model):
    """
    A page as it is directly pulled from the DB
        David: I was noticing that these SQL alchemy classes behave very weirdly when compared to
    """
    page_id = database.Column(database.Integer, primary_key=True)
    chapter_id = database.Column(database.Integer)
    page_number = database.Column(database.Integer)
    release_date = database.Column(database.Date, default=datetime.utcnow())
    description = database.Column(database.String)
    page_position = database.Column(database.String(1))
    image_name = database.Column(database.String(30))
    status = database.Column(database.String(1))
    create_dt = database.Column(database.Date, default=datetime.utcnow())
    update_dt = database.Column(database.Date, default=datetime.utcnow())

    def __repr__(self):
        return f'<Page: ChapterID{self.chapter_id}: Page Number;{self.page_number}>'


class CommentModel(database.Model):
    __tablename__ = "comment"
    comment_id = database.Column(database.Integer, primary_key=True)
    comment_guid = database.Column(database.String(40))
    page_id = database.Column(database.Integer)
    body = database.Column(database.String)
    author = database.Column(database.String)
    status = database.Column(database.String(1))
    create_dt = database.Column(database.Date, default=datetime.utcnow())
    update_dt = database.Column(database.Date, default=datetime.utcnow())
    def __repr__(self):
        return f'<Comment: comment_id{self.comment_id}: Page ID;{self.page_id}>'



class ComicChapterModel(database.Model):
    """
    The bare minimum comic information stored in the comic_chapter row
    """
    chapter_id = database.Column(database.Integer, primary_key=True)
    chapter_number = database.Column(database.Integer)
    title = database.Column(database.String)
    release_date = database.Column(database.Date)
    description = database.Column(database.String)
    created_at = database.Column(database.Date)
    updated_at = database.Column(database.Date)

    def __repr__(self):
        return f'<Page: ChapterID{self.chapter_id}: Page Number;{self.page_number}>'


