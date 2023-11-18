from enum import Enum


class SystemCode(Enum):
    STANDARD = 500,
    NOT_FOUND = 404,
    UNAUTHORIZED = 403


class SystemException(Exception):

    def __init(self, message: str, code: SystemCode):
        super().__init__(str)
        self.code = code
