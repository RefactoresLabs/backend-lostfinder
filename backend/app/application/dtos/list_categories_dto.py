class ListCategoriesDTO:

    """Objeto de transferência de dados do caso de uso de Listar Categorias"""

    def __init__(self, id: int, name: str) -> None:

        """Inicializa os atributos de instância de ListCategoriesDTO

        Parameters
        ----------
        id: int
            ID da categoria

        name: str
            Nome da categoria

        """

        self.__id = id
        self.__name = name
    
    @property
    def id(self) -> int:

        """Obtém o ID da categoria

        Returns
        -------
        int
            ID da categoria

        """

        return self.__id

    @property
    def name(self) -> str:

        """Obtém o nome da categoria

        Returns
        -------
        str
            Nome da categoria

        """

        return self.__name