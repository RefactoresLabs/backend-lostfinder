from abc import ABC, abstractmethod
from typing import Any


class FoundItemQueryServiceInterface(ABC):

    """Interface do serviço de consulta de itens encontrados"""
    
    @abstractmethod
    def get_all_found_items_summarized(self) -> list[dict[str, Any]]: ...