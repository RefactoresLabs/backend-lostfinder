from backend.app.application.interfaces.found_item_query_service_interface import FoundItemQueryServiceInterface
from backend.app.application.dtos.list_user_account_items_summarized_input_dto import ListUserAccountItemsSummarizedInputDTO
from backend.app.application.dtos.list_items_summarized_dto import ListItemsSummarizedDTO

from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError


class ListUserAccountFoundItemsSummarizedUseCase:

    """Representa um caso de uso de listar os itens encontrados resumidos de uma conta de usuário específica"""

    def __init__(self, found_item_query_service: FoundItemQueryServiceInterface) -> None:

        """Inicializa os atributos de instância de ListUserAccountFoundItemsSummarizedUseCase

        Parameters
        ----------
        found_item_query_service: FoundItemQueryServiceInterface
            Serviço de consulta de itens encontrados
        
        
        """

        self.__query_service = found_item_query_service
    
    def execute(self, dto: ListUserAccountItemsSummarizedInputDTO) -> list[ListItemsSummarizedDTO]:

        """Executa o fluxo de eventos do caso de uso

        Parameters
        ----------
        dto: ListUserAccountItemsSummarizedInputDTO
            Objeto de transferência de dados contendo o ID do usuário cujos itens encontrados serão obtidos
        
        Returns
        -------
        list[ListItemsSummarizedDTO]
            Iterável de objetos de transferência de dados contento os dados dos itens encontrados associados a conta de usuário
        
        Raises
        ------
        UserAccountDoesntExistError
            Exceção levantada quando uma conta de usuário não for encontrada

        """

        found_items = self.__query_service.get_found_items_summarized_by_user_id(dto.user_id)

        if not found_items:

            raise UserAccountDoesntExistError("A conta de usuário não foi encontrada!")

        return [
            ListItemsSummarizedDTO(
                found_item["item_id"],
                found_item["item_name"],
                found_item["user_name"],
                found_item["category_name"],
                found_item["building_space_name"],
                found_item["image_url"],
            )
            for found_item in found_items
        ]

