from abc import ABC, abstractmethod
from typing import Any


class LostItemQueryServiceInterface(ABC):

    """Interface do serviço de consulta de itens perdidos"""

    @abstractmethod
    def get_all_lost_items_summarized(self) -> list[dict[str, Any]]: ...

    @abstractmethod
    def get_lost_items_summarized_by_user_id(self, user_id: int) -> list[dict[str, Any]]: ...