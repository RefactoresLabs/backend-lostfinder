from backend.app.application.use_cases.get_claim_details_use_case import GetClaimDetailsUseCase
from backend.app.application.use_cases.delete_claim_use_case import DeleteClaimUseCase
from backend.app.application.use_cases.create_claim_use_case import CreateClaimUseCase
from backend.app.application.use_cases.accept_claim_use_case import AcceptClaimUseCase
from backend.app.application.use_cases.finish_claim_use_case import FinishClaimUseCase
from backend.app.application.use_cases.reject_claim_use_case import RejectClaimUseCase
from backend.app.application.use_cases.list_my_created_claims_use_case import ListMyCreatedClaimsUseCase
from backend.app.application.use_cases.list_my_received_claims_use_case import ListMyReceivedClaimsUseCase

from backend.app.infrastructure.persistence.repositories.claim_repository import ClaimRepository
from backend.app.infrastructure.persistence.repositories.found_item_repository import FoundItemRepository
from backend.app.infrastructure.persistence.repositories.user_account_repository import UserAccountRepository
from backend.app.infrastructure.queries.claim_query_service import ClaimQueryService

from backend.app.presentation.controllers.get_claim_details_controller import GetClaimDetailsController
from backend.app.presentation.controllers.delete_claim_controller import DeleteClaimController
from backend.app.presentation.controllers.create_claim_controller import CreateClaimController
from backend.app.presentation.controllers.accept_claim_controller import AcceptClaimController
from backend.app.presentation.controllers.finish_claim_controller import FinishClaimController
from backend.app.presentation.controllers.reject_claim_controller import RejectClaimController
from backend.app.presentation.controllers.list_my_created_claims_controller import ListMyCreatedClaimsController
from backend.app.presentation.controllers.list_my_received_claims_controller import ListMyReceivedClaimsController


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


def make_create_claim_controller(session: Session) -> CreateClaimController:

    """Factory function que cria um objeto CreateClaimController

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

def make_accept_claim_controller(session: Session) -> AcceptClaimController:

    """Factory function que cria um objeto AcceptClaimController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    AcceptClaimController
        Ponto de acesso entre o endpoint e o caso de uso de aceitar uma negociação de recuperação de item

    """

    repository = ClaimRepository(session)

    use_case = AcceptClaimUseCase(repository)

    return AcceptClaimController(use_case)

def make_finish_claim_controller(session: Session) -> FinishClaimController:

    """Function factory que cria um objeto FinishClaimController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações do banco

    Returns
    -------
    FinishClaimController
        Ponto de acesso entre o endpoint e o caso de uso de finalizar uma negociação de recuperação de item

    """

    repository = ClaimRepository(session)

    use_case = FinishClaimUseCase(repository)

    return FinishClaimController(use_case)

def make_reject_claim_controller(session: Session) -> RejectClaimController:

    """Factory function que cria um objeto RejectClaimController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    RejectClaimController
        Ponto de acesso entre o endpoint e o caso de uso de rejeitar uma negociação de recuperação de item

    """

    repository = ClaimRepository(session)

    use_case = RejectClaimUseCase(repository)

    return RejectClaimController(use_case)


def make_list_my_created_claims_controller(session: Session) -> ListMyCreatedClaimsController:

    """Factory function que cria um objeto ListMyCreatedClaimsController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco

    Returns
    -------
    ListMyCreatedClaimsController
        Ponto de acesso entre o endpoint e o caso de uso de listar negociações criadas pelo usuário autenticado

    """

    query_service = ClaimQueryService(session)
    user_account_repository = UserAccountRepository(session)

    use_case = ListMyCreatedClaimsUseCase(query_service, user_account_repository)

    return ListMyCreatedClaimsController(use_case)


def make_list_my_received_claims_controller(session: Session) -> ListMyReceivedClaimsController:

    """Factory function que cria um objeto ListMyReceivedClaimsController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco

    Returns
    -------
    ListMyReceivedClaimsController
        Ponto de acesso entre o endpoint e o caso de uso de listar negociações recebidas pelo usuário autenticado

    """

    query_service = ClaimQueryService(session)
    user_account_repository = UserAccountRepository(session)

    use_case = ListMyReceivedClaimsUseCase(query_service, user_account_repository)

    return ListMyReceivedClaimsController(use_case)