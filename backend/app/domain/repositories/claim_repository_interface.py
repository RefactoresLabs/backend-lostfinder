from abc import ABC, abstractmethod


from backend.app.domain.entities.claim import Claim


class ClaimRepositoryInterface(ABC):

    """Interface do repositório da entidade Claim"""

    @abstractmethod
    def create_new_claim(self, claim: Claim) -> Claim | None: ...

    @abstractmethod
    def update_claim(self, claim: Claim, claim_id: int) -> Claim: ...

    @abstractmethod
    def get_claim_by_id(self, claim_id: int) -> Claim | None: ...

    @abstractmethod
    def delete_claim(self, claim_id: int) -> bool: ...