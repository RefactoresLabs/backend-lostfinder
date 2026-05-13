class ListBuildingsDTO:

    """Objeto de transferência de dados do caso de uso de listar prédios"""

    def __init__(self, id: int, name: str) -> None:

        """Inicializa os atributos de instância de ListBuildingsDTO

        Parameters
        ----------
        id: int
            ID do prédio
        
        name: str
            Nome do prédio

        """

        self.__id = id
        self.__name = name
    
    @property
    def id(self) -> int:

        """Obtém o ID do prédio

        Returns
        -------
        int
            ID do prédio

        """
        
        return self.__id
    
    @property
    def name(self) -> str:

        """Obtém o nome do prédio

        Returns
        -------
        str
            Nome do prédio

        """

        return self.__name