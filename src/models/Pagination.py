class Pagination:
    """
    Used to get 'pages of things' For example, we might not want to load 200 comments
    for someone loading a comic_page, so let's just load a page of 10 comments at a time...
    """

    # total number of elements in db
    total_size: int

    def __init__(self,
                 page_size: int = 10,
                 page_number: int = 0,
                 ):
        self.page_size = page_size
        self.page_number = page_number

    def get_offset(self):
        return self.page_size * self.page_number
