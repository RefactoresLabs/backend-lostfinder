from backend.app.infrastructure.persistence.repositories.building_repository import BuildingRepository

from backend.app.application.use_cases.list_buildings_use_case import ListBuildingsUseCase

from backend.app.presentation.controllers.list_buildings_controller import ListBuildingsController


from sqlalchemy.orm import Session


def make_list_buildings_controller(session: Session) -> ListBuildingsController:

    """Function factory que cria um objeto ListBuildingsController

    Parameters
    ----------
    session: Session
        Sessão usada para transações com o banco de dados
    
    Returns
    -------
    ListBuildingController
        Ponto de acesso entre o endpoint e o caso de uso de listar prédios

    """

    repository = BuildingRepository(session)

    use_case = ListBuildingsUseCase(repository)

    return ListBuildingsController(use_case)