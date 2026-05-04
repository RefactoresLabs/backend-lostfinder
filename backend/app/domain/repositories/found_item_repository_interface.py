from abc import ABC, abstractmethod


from backend.app.domain.entities.found_item import FoundItem


class FoundItemRepositoryInterface(ABC):

    """Interface do repositório da entidade FoundItem"""

    @abstractmethod
    def create_new_found_item(self, found_item: FoundItem) -> FoundItem | None: ...

    @abstractmethod
    def update_found_item(self, found_item: FoundItem, id: int) -> FoundItem: ...

    @abstractmethod
    def get_found_item_by_id(self, id: int) -> FoundItem | None: ...

    @abstractmethod
    def delete_found_item(self, id: int) -> bool: ...