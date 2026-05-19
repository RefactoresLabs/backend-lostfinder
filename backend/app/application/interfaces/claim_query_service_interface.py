from abc import ABC, abstractmethod
from typing import Any


class ClaimQueryServiceInterface(ABC):

    """Interface do serviço de consulta de negociações"""

    @abstractmethod
    def get_created_claims_summarized_by_user_id(self, user_id: int) -> list[dict[str, Any]]: ...

    @abstractmethod
    def get_received_claims_summarized_by_user_id(self, user_id: int) -> list[dict[str, Any]]: ...