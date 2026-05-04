class Category:

    """Representa a entidade categoria que pode estar associada a um item"""

    def __init__(self, id: int, name: str) -> None:

        """Inicializa os atributos de instância de Category

        Parameters
        ----------
        id: int
            Identificador da categoria

        name: str
            Nome da categoria

        """

        self.__id = id
        self.__name = name
    
    @property
    def id(self) -> int:

        """Obtém o identificador da categoria

        Returns
        -------
        int
            Identificador da categoria
        
        """

        return self.__id
    
    @property
    def name(self) -> str:

        """Obtém o nome do item

        Returns
        -------
        str
            Nome do item

        """

        return self.__name