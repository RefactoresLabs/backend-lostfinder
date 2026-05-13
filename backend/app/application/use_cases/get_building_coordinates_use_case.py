from backend.app.domain.repositories.building_repository_interface import BuildingRepositoryInterface
from backend.app.application.interfaces.geocode_service_interface import GeocodeServiceInterface


class GetBuildingCoordinatesUseCase:

    """Caso de uso responsável por obter as coordenadas geográficas de um prédio"""

    def __init__(
        self,
        building_repository: BuildingRepositoryInterface,
        geocode_service: GeocodeServiceInterface,
    ) -> None:

        """Inicializa os atributos de instância de GetBuildingCoordinatesUseCase

        Parameters
        ----------
        building_repository: BuildingRepositoryInterface
            Repositório do prédio para busca dos dados

        geocode_service: GeocodeServiceInterface
            Serviço de geocodificação para obter coordenadas

        """

        self.__building_repository = building_repository
        self.__geocode_service = geocode_service

    def execute(self, building_id: int) -> dict:

        """Executa o fluxo de eventos do caso de uso obter coordenadas do prédio

        Parameters
        ----------
        building_id: int
            Identificador do prédio a ser buscado

        Returns
        -------
        dict
            Dicionário com os dados do prédio e suas coordenadas geográficas

        Raises
        ------
        ValueError
            Se o prédio não for encontrado

        RuntimeError
            Se as coordenadas não puderem ser obtidas pelo serviço de geocodificação

        """

        building = self.__building_repository.get_building_by_id(building_id)

        if building is None:

            raise ValueError("Prédio não encontrado")

        localization = building.localization

        coordinates = self.__geocode_service.get_coordinates(
            street=localization.street,
            neighborhood=localization.neighborhood,
            cep=localization.cep,
        )

        if coordinates is None:

            raise RuntimeError("Não foi possível obter as coordenadas do prédio")

        return {
            "building_id": building.id,
            "building_name": building.name,
            "latitude": coordinates["latitude"],
            "longitude": coordinates["longitude"],
        }
