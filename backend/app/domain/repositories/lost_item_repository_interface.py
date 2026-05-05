from abc import ABC, abstractmethod


from backend.app.domain.entities.lost_item import LostItem


class LostItemRepositoryInterface(ABC):

    """Interface do repositório da entidade LostItem"""

    @abstractmethod
    def create_new_lost_item(self, lost_item: LostItem) -> LostItem | None: ...

    @abstractmethod
    def update_lost_item(self, lost_item: LostItem, id: int) -> LostItem: ...

    @abstractmethod
    def get_lost_item_by_id(self, id: int) -> LostItem | None: ...

    @abstractmethod
    def delete_lost_item(self, id: int) -> bool: ...