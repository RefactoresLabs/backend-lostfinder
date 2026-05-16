from backend.app.presentation.controllers.create_claim_controller import CreateClaimController

from backend.app.application.use_cases.create_claim_use_case import CreateClaimUseCase

from backend.app.infrastructure.persistence.repositories.claim_repository import ClaimRepository
from backend.app.infrastructure.persistence.repositories.found_item_repository import FoundItemRepository
from backend.app.infrastructure.persistence.repositories.user_account_repository import UserAccountRepository


from sqlalchemy.orm import Session


def make_create_claim_controller(session: Session) -> CreateClaimController:

    """Factory funciona que cria um objeto CreateClaimController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    CreateClaimController
        Ponto de acesso entre o endpoint e o caso de uso de criar uma negociação de recuperação de item

    """

    user_account_repository = UserAccountRepository(session)
    found_item_repository = FoundItemRepository(session)
    claim_repository = ClaimRepository(session)

    use_case = CreateClaimUseCase(
        claim_repository,
        found_item_repository,
        user_account_repository,
    )

    return CreateClaimController(use_case)

