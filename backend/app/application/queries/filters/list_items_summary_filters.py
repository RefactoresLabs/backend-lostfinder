class ListItemsSummaryFilters:

    """Representa um invólucro que agrega os filtros aplicados aos casos de uso de listar itens resumidamente"""

    def __init__(self, name: str, category_id: int) -> None:

        """Inicializa os atributos de instância de ListItemsSummaryFilters

        Parameters
        ----------
        name: str
            Nome dos itens a serem filtrados

        category_id: int
            ID da categoria do itens a serem filtrados

        """

        self.__name = name
        self.__category_id = category_id
    
    @property
    def name(self) -> str:

        """Obtém o nome dos itens a serem filtrados

        Returns
        -------
        str
            Nome dos itens a serem filtrados

        """

        return self.__name
    
    @property
    def category_id(self) -> int:

        """Obtém o ID da categoria do itens a serem filtrados

        Returns
        -------
        int
            ID da categoria do itens a serem filtrados

        """

        return self.__category_id