class ListItemsSummarizedInputDTO:

    """Objeto de transferência de dados de entrada dos casos de usos de listar itens resumidamente"""

    def __init__(self, filter_name: str | None=None, filter_category_id: int | None=None, sort_by: str="name", sort_option: str="asc") -> None:

        """Inicializa os atributos de instância de ListItemsSummarizedInputDTO

        Parameters
        ----------
        filter_name: str | None (Padrão: None)
            Nome dos itens a serem filtrados
        
        filter_category_id: str | None (Padrão: None)
            ID da categoria dos itens a serem filtrados
        
        sort_by: str (Padrão: name)
            Campo pelo qual os itens serão ordenados
        
        sort_option: str (Padrão: asc)
            Opção de ordenamento
        
        """

        self.__filter_name = filter_name
        self.__filter_category_id = filter_category_id
        self.__sort_by = sort_by
        self.__sort_option = sort_option
    
    @property
    def filter_name(self) -> str | None:

        """Obtém o nome dos itens a serem filtrados

        Returns
        -------
        str | None
            Nome dos itens a serem filtrados

        """

        return self.__filter_name
    
    @property
    def filter_category_id(self) -> int | None:

        """Obtém o ID da categoria dos itens a serem filtrados

        Returns
        -------
        int | None
            ID da categoria dos itens a serem filtrados

        """

        return self.__filter_category_id
    
    @property
    def sort_by(self) -> str:

        """Obtém o campo pelo qual os itens serão ordenados

        Returns
        -------
        str
            Campo pelo qual os itens serão ordenados

        """

        return self.__sort_by
    
    @property
    def sort_option(self) -> str:

        """Obtém a opção de ordenamento

        Returns
        -------
        str
            Opção de ordenamento

        """

        return self.__sort_option