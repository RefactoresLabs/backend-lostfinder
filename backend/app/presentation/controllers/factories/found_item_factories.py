from backend.app.application.use_cases.create_found_item_use_case import CreateFoundItemUseCase
from backend.app.application.use_cases.list_found_items_summarized_use_case import ListFoundItemsSummarizedUseCase
from backend.app.application.use_cases.get_found_item_details_use_case import GetFoundItemDetailsUseCase
from backend.app.application.use_cases.list_user_account_found_items_summarized_use_case import ListUserAccountFoundItemsSummarizedUseCase
from backend.app.application.use_cases.update_found_item_use_case import UpdateFoundItemUseCase
from backend.app.application.use_cases.delete_found_item_use_case import DeleteFoundItemUseCase

from backend.app.infrastructure.persistence.repositories.found_item_repository import FoundItemRepository
from backend.app.infrastructure.persistence.repositories.category_repository import CategoryRepository
from backend.app.infrastructure.persistence.repositories.building_space_repository import BuildingSpaceRepository
from backend.app.infrastructure.persistence.repositories.user_account_repository import UserAccountRepository
from backend.app.infrastructure.queries.found_item_query_service import FoundItemQueryService

from backend.app.presentation.controllers.create_found_item_controller import CreateFoundItemController
from backend.app.presentation.controllers.list_found_items_summarized_controller import ListFoundItemsSummarizedController
from backend.app.presentation.controllers.get_found_item_details_controller import GetFoundItemDetailsController
from backend.app.presentation.controllers.list_user_account_found_items_summarized_controller import ListUserAccountFoundItemsSummarizedController
from backend.app.presentation.controllers.update_found_item_controller import UpdateFoundItemController
from backend.app.presentation.controllers.delete_found_item_controller import DeleteFoundItemController

from sqlalchemy.orm import Session


def make_list_found_item_summarized_controller(session: Session):

    """Factory function que cria um objeto ListFoundItemsSummarizedController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    ListFoundItemsSummarizedController
        Ponto de acesso do endpoint com o caso de uso de listar itens encontrados resumidamente
        
    """

    query_service = FoundItemQueryService(session)

    use_case = ListFoundItemsSummarizedUseCase(query_service)

    return ListFoundItemsSummarizedController(use_case)

def make_create_found_item_controller(session: Session) -> CreateFoundItemController:

    """Factory function que cria um objeto CreateFoundItemController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco

    Returns
    -------
    CreateFoundItemController
        Ponto de acesso do endpoint com o caso de uso de registro de item encontrado

    """

    found_item_repository = FoundItemRepository(session)
    category_repository = CategoryRepository(session)
    building_space_repository = BuildingSpaceRepository(session)
    user_account_repository = UserAccountRepository(session)

    create_found_item_use_case = CreateFoundItemUseCase(
        found_item_repository=found_item_repository,
        category_repository=category_repository,
        building_space_repository=building_space_repository,
        user_account_repository=user_account_repository,
    )

    return CreateFoundItemController(create_found_item_use_case)

def make_get_found_item_details_controller(session: Session) -> GetFoundItemDetailsController:

    """Factory function que cria um objeto GetFoundItemDetailsController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    GetFoundItemDetailsController
        Ponto de acesso do endpoint com o caso de uso de obtenção de dados detalhados de um item encontrado
        
    """

    repository = FoundItemRepository(session)

    use_case = GetFoundItemDetailsUseCase(repository)

    return GetFoundItemDetailsController(use_case)

def make_list_user_account_found_item_summarized_controller(session: Session) -> ListUserAccountFoundItemsSummarizedUseCase:

    """Factory function que cria um objeto ListUserAccountFoundItemsSummarizedController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco

    Returns
    -------
    ListUserAccountFoundItemsSummarizedController
        Ponto de acesso do endpoint com o caso de uso de listar itens encontrados resumidamente de uma conta de usuário

    """

    query_service = FoundItemQueryService(session)

    repository = UserAccountRepository(session)

    use_case = ListUserAccountFoundItemsSummarizedUseCase(query_service, repository)

    return ListUserAccountFoundItemsSummarizedController(use_case)

def make_update_found_item_controller(session: Session) -> UpdateFoundItemController:

    """Factory function que cria um objeto UpdateFoundItemController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco

    Returns
    -------
    UpdateFoundItemController
        Ponto de acesso do endpoint com o caso de uso de atualização de item encontrado

    """

    found_item_repository = FoundItemRepository(session)
    category_repository = CategoryRepository(session)
    building_space_repository = BuildingSpaceRepository(session)

    use_case = UpdateFoundItemUseCase(
        found_item_repository=found_item_repository,
        category_repository=category_repository,
        building_space_repository=building_space_repository,
    )

    return UpdateFoundItemController(use_case)

def make_delete_found_item_controller(session: Session) -> DeleteFoundItemController:

    """Factory function que cria um objeto DeleteFoundItemController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco

    Returns
    -------
    DeleteFoundItemController
        Ponto de acesso do endpoint com o caso de uso de exclusão de item encontrado

    """

    repository = FoundItemRepository(session)

    use_case = DeleteFoundItemUseCase(repository)

    return DeleteFoundItemController(use_case)
