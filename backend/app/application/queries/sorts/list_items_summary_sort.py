from backend.app.application.queries.sorts.enums.list_items_summary_sort_field import ListItemsSummarySortField
from backend.app.application.queries.sorts.enums.list_items_summary_sort_option import ListItemsSummarySortOption


class ListItemsSummarySort:

    """Representa um invólucro que agrega as características de um ordenamento dos casos de uso de listar itens resumidos"""

    def __init__(self, sort_field: ListItemsSummarySortField, sort_option: ListItemsSummarySortOption) -> None:

        """Inicializa os atributos de instância de ListItemsSummarySort

        Parameters
        ----------
        sort_field: ListItemsSummarySortField
            Campo pelo qual os itens serão ordenados
        
        sort_option: ListItemsSummarySortOption
            Opção de ordenamento (crescente ou descrescente)

        """

        self.__sort_field = sort_field
        self.__sort_option = sort_option
    
    @property
    def sort_field(self) -> ListItemsSummarySortField:

        """Obtém o campo pelo qual os itens serão ordenados

        Returns
        -------
        ListItemsSummarySortField
            Campo pelo qual os itens serão ordenados

        """

        return self.__sort_field

    @property
    def sort_option(self) -> ListItemsSummarySortOption:

        """Obtém a opção de ordenamento

        Parameters
        ----------
        sort_option: ListItemsSummarySortOption
            Opção de ordenamento
        
        """

        return self.__sort_option