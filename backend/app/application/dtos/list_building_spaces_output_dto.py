class ListBuildingSpacesOutputDTO:

    """Objeto de transferência de dados da saída do caso de uso de listar espaços de um prédio"""

    def __init__(self, id: int, name: str) -> None:

        """Inicializa os atributos de instância de ListBuildingSpacesOutputDTO

        Parameters
        ----------
        id: int
            ID do espaço do prédio
        
        name: str
            Nome do espaço do prédio

        """

        self.__id = id
        self.__name = name
    
    @property
    def id(self) -> int:

        """Obtém o ID do espaço do prédio

        Returns
        -------
        int
            ID do espaço do prédio

        """

        return self.__id

    @property
    def name(self) -> int:

        """Obtém o nome do espaço do prédio

        Returns
        -------
        int
            Nome do espaço do prédio

        """

        return self.__name