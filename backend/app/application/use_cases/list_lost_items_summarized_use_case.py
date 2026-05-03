from backend.app.application.interfaces.lost_item_query_service_interface import LostItemQueryServiceInterface
from backend.app.application.dtos.list_items_summarized_dto import ListItemsSummarizedDTO

class ListLostItemsSummarizedUseCase:

    """Representa um caso de uso de listar itens perdidos resumidamente"""

    def __init__(self, lost_item_query_service: LostItemQueryServiceInterface) -> None:

        """Inicializa os atributos de instância de ListLostItemsSummarizedUseCase

        Parameters
        ----------
        lost_item_query_service: LostItemQueryServiceInterface
            Serviço que lida com transações mais específicas de lost_item
        
    
        """

        self.__query_service = lost_item_query_service
    
    def execute(self) -> list[ListItemsSummarizedDTO]:

        """Executa o fluxo de eventos do caso de uso de listar itens perdidos resumidamente

        Returns
        -------
        list[ListItemsSummarizedDTO]
            Iterável contendo os DTOs com os dados resumidos dos itens perdidos
            
        """

        summarized_lost_items = self.__query_service.get_all_lost_items_summarized()

        return [
            ListItemsSummarizedDTO(
                lost_item["item_id"],
                lost_item["item_name"],
                lost_item["user_name"],
                lost_item["category_name"],
                lost_item["building_space_name"],
                lost_item["image_url"],
            )
            for lost_item in summarized_lost_items
        ]
        