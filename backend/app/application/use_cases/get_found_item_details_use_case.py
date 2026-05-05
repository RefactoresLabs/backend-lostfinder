from backend.app.domain.repositories.found_item_repository_interface import FoundItemRepositoryInterface
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError

from backend.app.application.dtos.get_item_details_input_dto import GetItemDetailsInputDTO
from backend.app.application.dtos.get_found_item_details_output_dto import GetFoundItemDetailsOutputDTO


class GetFoundItemDetailsUseCase:

    """Representa um caso de uso de obter os detalhes de um item encontrado"""

    def __init__(self, repository: FoundItemRepositoryInterface) -> None:

        """Inicializa os atributos de instância de GetFoundItemDetaislUseCase

        Parameters
        ----------
        repository: FoundItemRepositoryInterface
            Repositório de itens encontrados para busca dos dados

        """

        self.__repository = repository
    
    def execute(self, dto: GetItemDetailsInputDTO) -> GetFoundItemDetailsOutputDTO:

        """Executa o fluxo de eventos do caso de uso de obter os dados do item encontrado detalhado

        Parameters
        ----------
        dto: GetItemDetailsInputDTO
            Objeto de transferência de dados contendo o ID do item encontrado a ser detalhado
        
        Returns
        -------
        GetFoundItemDetailsOutputDTO
            Objeto de transferência de dados com os dados detalhados do item encontrado

        Raises
        ------
        ItemDoesntExistError
            Exceção levantada quando um item não foi encontrado
            
        """

        found_item = self.__repository.get_found_item_by_id(dto.id)

        if not found_item:

            raise ItemDoesntExistError("Item não encontrado")

        return GetFoundItemDetailsOutputDTO(
            found_item.id,
            found_item.name,
            found_item.description,
            list(
                map(
                    lambda x: x.url, found_item.images
                )
            ),
            found_item.category.name,
            found_item.associated_user_account.name,
            found_item.associated_user_account.email,
            found_item.associated_user_account.phone,
            found_item.approx_found_building_space.name,
            found_item.approx_found_building_space.associated_building.name,
            found_item.approx_found_building_space.associated_building.localization.cep,
            found_item.approx_found_building_space.associated_building.localization.neighborhood,
            found_item.approx_found_building_space.associated_building.localization.street,
            found_item.approx_left_building_space.name,
            found_item.approx_left_building_space.associated_building.name,
            found_item.approx_left_building_space.associated_building.localization.cep,
            found_item.approx_left_building_space.associated_building.localization.neighborhood,
            found_item.approx_left_building_space.associated_building.localization.street,
        )