from abc import ABC, abstractmethod
from typing import Any


class LostItemQueryServiceInterface(ABC):

    @abstractmethod
    def get_all_lost_items_summarized(self) -> list[dict[str, Any]]: ...