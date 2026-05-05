from backend.app.application.interfaces.lost_item_query_service_interface import LostItemQueryServiceInterface
from backend.app.application.dtos.list_user_account_items_summarized_input_dto import ListUserAccountItemsSummarizedInputDTO
from backend.app.application.dtos.list_items_summarized_dto import ListItemsSummarizedDTO

from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError
from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface


class ListUserAccountLostItemsSummarizedUseCase:

    """Representa um caso de uso de listar os itens perdidos resumidos de uma conta de usuário específica"""

    def __init__(self, lost_item_query_service: LostItemQueryServiceInterface, user_account_repository: UserAccountRepositoryInterface) -> None:

        """Inicializa os atributos de instância de ListUserAccountLostItemsSummarizedUseCase

        Parameters
        ----------
        lost_item_query_service: LostItemQueryServiceInterface
            Serviço de consulta de itens perdidos
        
        user_repository: UserAccountRepositoryInterface
            Repositório de conta de usuários
        
        """

        self.__query_service = lost_item_query_service
        self.__user_account_repository = user_account_repository
    
    def execute(self, dto: ListUserAccountItemsSummarizedInputDTO) -> list[ListItemsSummarizedDTO]:

        """Executa o fluxo de eventos do caso de uso

        Parameters
        ----------
        dto: ListUserAccountItemsSummarizedInputDTO
            Objeto de transferência de dados contendo o ID do usuário cujos itens perdidos serão obtidos
        
        Returns
        -------
        list[ListItemsSummarizedDTO]
            Iterável de objetos de transferência de dados contento os dados dos itens perdidos associados a conta de usuário
        
        Raises
        ------
        UserAccountDoesntExistError
            Exceção levantada quando uma conta de usuário não for encontrada

        """

        user_account = self.__user_account_repository.get_user_account_by_id(dto.user_id)

        if not user_account:

            raise UserAccountDoesntExistError("A conta de usuário não foi encontrada!")

        lost_items = self.__query_service.get_lost_items_summarized_by_user_id(dto.user_id)

        return [
            ListItemsSummarizedDTO(
                lost_item["item_id"],
                lost_item["item_name"],
                lost_item["user_name"],
                lost_item["category_name"],
                lost_item["building_space_name"],
                lost_item["image_url"],
            )
            for lost_item in lost_items
        ]

