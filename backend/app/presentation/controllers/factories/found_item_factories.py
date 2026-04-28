from backend.app.application.use_cases.create_found_item_use_case import CreateFoundItemUseCase

from backend.app.infrastructure.persistence.repositories.found_item_repository import FoundItemRepository
from backend.app.infrastructure.persistence.repositories.category_repository import CategoryRepository
from backend.app.infrastructure.persistence.repositories.building_space_repository import BuildingSpaceRepository
from backend.app.infrastructure.persistence.repositories.user_account_repository import UserAccountRepository

from backend.app.presentation.controllers.create_found_item_controller import CreateFoundItemController

from sqlalchemy.orm import Session


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
