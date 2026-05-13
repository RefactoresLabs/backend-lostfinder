from backend.app.infrastructure.persistence.repositories.building_repository import BuildingRepository
from backend.app.infrastructure.external.maps.nominatim_geocode_adapter import NominatimGeocodeAdapter

from backend.app.application.use_cases.get_building_coordinates_use_case import GetBuildingCoordinatesUseCase
from backend.app.application.use_cases.list_buildings_use_case import ListBuildingsUseCase

from backend.app.presentation.controllers.list_buildings_controller import ListBuildingsController
from backend.app.presentation.controllers.get_building_coordinates_controller import GetBuildingCoordinatesController


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

def make_get_building_coordinates_controller(session: Session) -> GetBuildingCoordinatesController:

    """Factory function que cria um objeto GetBuildingCoordinatesController

    Parameters
    ----------
    session: Session
        Sessão usada para transações com o banco de dados
    
    Returns
    -------
    GetBuildingCoordinatesController
        Ponto de acesso do endpoint com o caso de uso de obter coordenadas do prédio
    
    """

    building_repository = BuildingRepository(session)
    geocode_service = NominatimGeocodeAdapter()

    get_building_coordinates_use_case = GetBuildingCoordinatesUseCase(
        building_repository=building_repository,
        geocode_service=geocode_service,
    )

    return GetBuildingCoordinatesController(get_building_coordinates_use_case)
