from backend.app.infrastructure.persistence.repositories.building_space_repository import BuildingSpaceRepository
from backend.app.infrastructure.persistence.repositories.building_repository import BuildingRepository

from backend.app.application.use_cases.list_building_spaces_use_case import ListBuildingSpacesUseCase

from backend.app.presentation.controllers.list_building_spaces_controller import ListBuildingSpacesController


from sqlalchemy.orm import Session


def make_list_building_spaces_controller(session: Session) -> ListBuildingSpacesController:

    """Function factory que cria um objeto ListBuildingSpacesController

    Parameters
    ----------
    session: Session
        Sessão usada nas transações com o banco de dados
    
    Returns
    -------
    ListBuildingSpacesController
        Ponto de acesso entre o endpoint e o caso de uso de listar espaços de um prédio

    """

    building_space_repository = BuildingSpaceRepository(session)
    building_repository = BuildingRepository(session)

    use_case = ListBuildingSpacesUseCase(
        building_space_repository, 
        building_repository
    )

    return ListBuildingSpacesController(use_case)

