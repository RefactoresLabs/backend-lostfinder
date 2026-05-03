from backend.app.domain.repositories.lost_item_repository_interface import LostItemRepositoryInterface
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError


from backend.app.application.dtos.get_item_details_input_dto import GetItemDetailsInputDTO
from backend.app.application.dtos.get_lost_item_details_output_dto import GetLostItemDetailsOutputDTO


class GetLostItemDetailsUseCase:

    """Representa um caso de uso de obter os detalhes de um item perdido"""

    def __init__(self, repository: LostItemRepositoryInterface) -> None:

        """Inicializa os atributos de instância de GetLostItemDetaislUseCase

        Parameters
        ----------
        repository: LostItemRepositoryInterface
            Repositório de itens perdidos para busca dos dados

        """

        self.__repository = repository
    
    def execute(self, dto: GetItemDetailsInputDTO) -> GetLostItemDetailsOutputDTO:

        """Executa o fluxo de eventos do caso de uso de obter os dados do item perdido detalhado

        Parameters
        ----------
        dto: GetItemDetailsInputDTO
            Objeto de transferência de dados contendo o ID do item perdido a ser detalhado
        
        Returns
        -------
        GetLostItemDetailsOutputDTO
            Objeto de transferência de dados com os dados detalhados do item perdido

        Raises
        ------
        ItemDoesntExistError
            Exceção levantada quando um item não foi encontrado
            
        """

        lost_item = self.__repository.get_lost_item_by_id(dto.id)

        if not lost_item:

            raise ItemDoesntExistError("Item não encontrado")

        return GetLostItemDetailsOutputDTO(
            lost_item.id,
            lost_item.name,
            lost_item.description,
            list(
                map(
                    lambda x: x.url, lost_item.images
                )
            ),
            lost_item.category.name,
            lost_item.associated_user_account.name,
            lost_item.associated_user_account.email,
            lost_item.associated_user_account.phone,
            lost_item.approx_lost_building_space.name,
            lost_item.approx_lost_building_space.associated_building.name,
            lost_item.approx_lost_building_space.associated_building.localization.cep,
            lost_item.approx_lost_building_space.associated_building.localization.neighborhood,
            lost_item.approx_lost_building_space.associated_building.localization.street,
        )