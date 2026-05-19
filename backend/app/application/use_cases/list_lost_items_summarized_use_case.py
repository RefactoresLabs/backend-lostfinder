from backend.app.application.interfaces.lost_item_query_service_interface import LostItemQueryServiceInterface
from backend.app.application.dtos.list_items_summarized_output_dto import ListItemsSummarizedOutputDTO
from backend.app.application.dtos.list_items_summarized_input_dto import ListItemsSummarizedInputDTO

from backend.app.application.queries.filters.list_items_summary_filters import ListItemsSummaryFilters
from backend.app.application.queries.sorts.list_items_summary_sort import ListItemsSummarySort
from backend.app.application.queries.sorts.enums.list_items_summary_sort_field import ListItemsSummarySortField
from backend.app.application.queries.sorts.enums.list_items_summary_sort_option import ListItemsSummarySortOption


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
    
    def execute(self, dto: ListItemsSummarizedInputDTO) -> list[ListItemsSummarizedOutputDTO]:

        """Executa o fluxo de eventos do caso de uso de listar itens perdidos resumidamente

        Parameters
        ----------
        dto: ListItemsSummarizedInputDTO
            Objeto de transferência de dados contendo dados de filtro e ordenamento

        Returns
        -------
        list[ListItemsSummarizedOutputDTO]
            Iterável contendo os DTOs com os dados resumidos dos itens perdidos
            
        """

        filters = ListItemsSummaryFilters(dto.filter_name, dto.filter_category_id)
        sort = ListItemsSummarySort(
            ListItemsSummarySortField(dto.sort_by), 
            ListItemsSummarySortOption(dto.sort_option),
        )

        summarized_lost_items = self.__query_service.get_all_lost_items_summarized(filters, sort)

        return [
            ListItemsSummarizedOutputDTO(
                lost_item["item_id"],
                lost_item["item_name"],
                lost_item["user_name"],
                lost_item["category_name"],
                lost_item["building_space_name"],
                lost_item["image_url"],
            )
            for lost_item in summarized_lost_items
        ]
        