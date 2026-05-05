from backend.app.application.interfaces.found_item_query_service_interface import FoundItemQueryServiceInterface
from backend.app.application.dtos.list_items_summarized_dto import ListItemsSummarizedDTO

class ListFoundItemsSummarizedUseCase:

    """Representa um caso de uso de listar itens encontrados resumidamente"""

    def __init__(self, found_item_query_service: FoundItemQueryServiceInterface) -> None:

        """Inicializa os atributos de instância de ListFoundItemsSummarizedUseCase

        Parameters
        ----------
        found_item_query_service: FoundItemQueryServiceInterface
            Serviço que lida com transações mais específicas de found_item
        
    
        """

        self.__query_service = found_item_query_service
    
    def execute(self) -> list[ListItemsSummarizedDTO]:

        """Executa o fluxo de eventos do caso de uso de listar itens encontrados resumidamente

        Returns
        -------
        list[ListItemsSummarizedDTO]
            Iterável contendo os DTOs com os dados resumidos dos itens encontrados
            
        """

        summarized_found_items = self.__query_service.get_all_found_items_summarized()

        return [
            ListItemsSummarizedDTO(
                found_item["item_id"],
                found_item["item_name"],
                found_item["user_name"],
                found_item["category_name"],
                found_item["building_space_name"],
                found_item["image_url"],
            )
            for found_item in summarized_found_items
        ]
        