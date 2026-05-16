from backend.app.application.use_cases.get_claim_details_use_case import GetClaimDetailsUseCase
from backend.app.application.use_cases.delete_claim_use_case import DeleteClaimUseCase
from backend.app.infrastructure.persistence.repositories.claim_repository import ClaimRepository
from backend.app.presentation.controllers.get_claim_details_controller import GetClaimDetailsController
from backend.app.presentation.controllers.delete_claim_controller import DeleteClaimController
from sqlalchemy.orm import Session


def make_get_claim_details_controller(session: Session) -> GetClaimDetailsController:

    """Factory function que cria um objeto GetClaimDetailsController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    GetClaimDetailsController
        Ponto de acesso do endpoint com o caso de uso de obtenção de dados detalhados de uma negociação
        
    """

    repository = ClaimRepository(session)
    use_case = GetClaimDetailsUseCase(repository)

    return GetClaimDetailsController(use_case)


def make_delete_claim_controller(session: Session) -> DeleteClaimController:

    """Factory function que cria um objeto DeleteClaimController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    DeleteClaimController
        Ponto de acesso do endpoint com o caso de uso de exclusão de uma negociação
        
    """

    repository = ClaimRepository(session)
    use_case = DeleteClaimUseCase(repository)

    return DeleteClaimController(use_case)
