from backend.app.domain.repositories.building_space_repository_interface import BuildingSpaceRepositoryInterface
from backend.app.domain.repositories.building_repository_interface import BuildingRepositoryInterface
from backend.app.domain.exceptions.building_doesnt_exist_error import BuildingDoesntExistError

from backend.app.application.dtos.list_building_spaces_input_dto import ListBuildingSpacesInputDTO
from backend.app.application.dtos.list_building_spaces_output_dto import ListBuildingSpacesOutputDTO

class ListBuildingSpacesUseCase:

    """Representa um caso de uso de listar espaços de um prédio"""

    def __init__(self, building_space_repository: BuildingSpaceRepositoryInterface, building_repository: BuildingRepositoryInterface) -> None:

        """Inicializa os atributos de instância de ListBuildingSpacesUseCase

        Parameters
        ----------
        building_space_repository: BuildingSpaceRepositoryInterface
            Repositório de espaço de prédio para busca de dados
        
        building_repository: BuildingRepositoryInterface
            Repositório de prédio para checar sua existência

        """

        self.__building_space_repository = building_space_repository
        self.__building_repository = building_repository
    
    def execute(self, dto: ListBuildingSpacesInputDTO) -> list[ListBuildingSpacesOutputDTO]:

        """Executa o fluxo de eventos do caso de uso

        Parameters
        ----------
        dto: ListBuildingSpacesInputDTO
            Objeto de transferência de dados contendo o ID do prédio associado aos espaços
        
        Returns
        -------
        list[ListBuildingSpacesOutputDTO]
            Objetos de transferência de dados com os dados dos espaços do prédio
        
        Raises
        ------
        BuildingDoesntExistError
            Levantado quando o prédio não é encontrado

        """

        building = self.__building_repository.get_buildind_by_id(dto.building_id)

        if not building:

            raise BuildingDoesntExistError("Prédio não encontrado")

        building_spaces = self.__building_space_repository.get_building_spaces_by_building_id(dto.building_id)

        return [
            ListBuildingSpacesOutputDTO(
                building_space.id,
                building_space.name
            )
            for building_space in building_spaces
        ]