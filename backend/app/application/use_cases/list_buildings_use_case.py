from backend.app.domain.repositories.building_repository_interface import BuildingRepositoryInterface

from backend.app.application.dtos.list_buildings_dto import ListBuildingsDTO


class ListBuildingsUseCase:

    """Representa um caso de uso de listar prédios"""

    def __init__(self, building_repository: BuildingRepositoryInterface) -> None:

        """Inicializa os atributos de instância de ListBuildingsUseCase

        Parameters
        ----------
        building_repository: BuildingRepositoryInterface
            Repositório de prédios para buscar dados

        """

        self.__repository = building_repository
    
    def execute(self) -> list[ListBuildingsDTO]:

        """Executa o fluxo de eventos do caso de uso

        Returns
        -------
        list[ListBuildingsDTO]
            Objeto de transferência de dados com os dados do prédio

        """

        buildings = self.__repository.get_all_buildings()

        return [
            ListBuildingsDTO(
                building.id,
                building.name,
            )
            for building in buildings
        ]