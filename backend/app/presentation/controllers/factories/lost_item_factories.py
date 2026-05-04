from backend.app.application.use_cases.list_lost_items_summarized_use_case import ListLostItemsSummarizedUseCase
from backend.app.application.use_cases.create_lost_item_use_case import CreateLostItemUseCase
from backend.app.application.use_cases.get_lost_item_details_use_case import GetLostItemDetailsUseCase
from backend.app.application.use_cases.list_user_account_lost_items_summarized_use_case import ListUserAccountLostItemsSummarizedUseCase

from backend.app.presentation.controllers.list_lost_items_summarized_controller import ListLostItemsSummarizedController
from backend.app.presentation.controllers.create_lost_item_controller import CreateLostItemController
from backend.app.presentation.controllers.get_lost_item_details_controller import GetLostItemDetailsController
from backend.app.presentation.controllers.list_user_account_lost_items_summarized_controller import ListUserAccountLostItemsSummarizedController

from backend.app.infrastructure.persistence.repositories.lost_item_repository import LostItemRepository
from backend.app.infrastructure.persistence.repositories.category_repository import CategoryRepository
from backend.app.infrastructure.persistence.repositories.building_space_repository import BuildingSpaceRepository
from backend.app.infrastructure.persistence.repositories.user_account_repository import UserAccountRepository
from backend.app.infrastructure.queries.lost_item_query_service import LostItemQueryService


from sqlalchemy.orm import Session


def make_list_lost_item_summarized_controller(session: Session):

    """Factory function que cria um objeto ListLostItemsSummarizedController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    ListLostItemsSummarizedController
        Ponto de acesso do endpoint com o caso de uso de listar itens perdidos resumidamente
        
    """

    query_service = LostItemQueryService(session)

    use_case = ListLostItemsSummarizedUseCase(query_service)

    return ListLostItemsSummarizedController(use_case)

    
def make_create_lost_item_controller(session: Session) -> CreateLostItemController:

    """Factory function que cria um objeto CreateLostItemController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    CreateLostItemController
        Ponto de acesso do endpoint com o caso de uso de registro de item perdido
        
    """

    lost_item_repository = LostItemRepository(session)
    category_repository = CategoryRepository(session)
    building_space_repository = BuildingSpaceRepository(session)
    user_account_repository = UserAccountRepository(session)

    create_lost_item_use_case = CreateLostItemUseCase(
        lost_item_repository=lost_item_repository,
        category_repository=category_repository,
        building_space_repository=building_space_repository,
        user_account_repository=user_account_repository,
    )

    return CreateLostItemController(create_lost_item_use_case)

def make_get_lost_item_details_controller(session: Session) -> GetLostItemDetailsController:

    """Factory function que cria um objeto GetLostItemDetailsController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    GetLostItemDetailsController
        Ponto de acesso do endpoint com o caso de uso de obtenção de dados detalhados de um item perdido
        
    """

    repository = LostItemRepository(session)

    use_case = GetLostItemDetailsUseCase(repository)

    return GetLostItemDetailsController(use_case)

def make_list_user_account_lost_item_summarized_controller(session: Session) -> ListUserAccountLostItemsSummarizedController:

    """Factory function que cria um objeto ListUserAccountLostItemsSummarizedController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    ListUserAccountLostItemsSummarizedController
        Ponto de acesso do endpoint com o caso de uso de listar itens perdidos resumidamente de uma conta de usuário
        
    """

    query_service = LostItemQueryService(session)

    repository = UserAccountRepository(session)

    use_case = ListUserAccountLostItemsSummarizedUseCase(query_service, repository)

    return ListUserAccountLostItemsSummarizedController(use_case)