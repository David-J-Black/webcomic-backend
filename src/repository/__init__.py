from database import database
from .Repositories import Repository
from .commentRepository import CommentRepository


chapter_repository = Repository(database)
comment_repository = CommentRepository(database)