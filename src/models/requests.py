

class CommentRequest:

    def __init__(self, request_dict: dict):
        self.body = request_dict.get('body')
