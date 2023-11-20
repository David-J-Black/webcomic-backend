from typing import List

from models import Pagination


class Serializable:
    """
    Intended for any entity that leaves the API
    """
    def to_dto(self) -> dict[str, any]:
        raise NotImplementedError('Hey bitch, it looks like you need to overide to_dto() in a class!')


class SerializableList:
    """
    Intended for any list of entities that leave the API
    """

    def __init__(self,
                 list_of_serializables: List[Serializable],
                 pagination: Pagination
                 ):
        self.list: List[Serializable] = list_of_serializables
        self.pagination: Pagination = pagination

    def to_dto(self) -> dict[str, any]:
        response_list: list[dict] = []

        for entity in self.list:
            response_list.append(entity.to_dto())

        return {
            'data': response_list,
            'pagination': self.pagination.to_dto()
        }
