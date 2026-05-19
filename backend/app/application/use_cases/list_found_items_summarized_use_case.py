from backend.app.application.interfaces.found_item_query_service_interface import FoundItemQueryServiceInterface
from backend.app.application.dtos.list_items_summarized_output_dto import ListItemsSummarizedOutputDTO
from backend.app.application.dtos.list_items_summarized_input_dto import ListItemsSummarizedInputDTO

from backend.app.application.queries.filters.list_items_summary_filters import ListItemsSummaryFilters
from backend.app.application.queries.sorts.list_items_summary_sort import ListItemsSummarySort
from backend.app.application.queries.sorts.enums.list_items_summary_sort_field import ListItemsSummarySortField
from backend.app.application.queries.sorts.enums.list_items_summary_sort_option import ListItemsSummarySortOption


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
    
    def execute(self, dto: ListItemsSummarizedInputDTO) -> list[ListItemsSummarizedOutputDTO]:

        """Executa o fluxo de eventos do caso de uso de listar itens encontrados resumidamente

        dto: ListItemsSummarizedInputDTO
            Objeto de transferência de dados contendo dados de filtro e ordenamento

        Returns
        -------
        list[ListItemsSummarizedOutputDTO]
            Iterável contendo os DTOs com os dados resumidos dos itens encontrados
            
        """

        filters = ListItemsSummaryFilters(dto.filter_name, dto.filter_category_id)
        sort = ListItemsSummarySort(
            ListItemsSummarySortField(dto.sort_by), 
            ListItemsSummarySortOption(dto.sort_option),
        )

        summarized_found_items = self.__query_service.get_all_found_items_summarized(filters, sort)

        return [
            ListItemsSummarizedOutputDTO(
                found_item["item_id"],
                found_item["item_name"],
                found_item["user_name"],
                found_item["category_name"],
                found_item["building_space_name"],
                found_item["image_url"],
            )
            for found_item in summarized_found_items
        ]
        