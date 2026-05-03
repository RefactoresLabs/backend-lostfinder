class GetItemDetailsInputDTO:

    """Objeto de transferência de dados para entrada dos casos de uso de obter os dados detalhados de item perdido e encontrado"""

    def __init__(self, id: int) -> None:

        """Inicializa os atributos de instância de GetItemDetailsInputDTO

        Parameters
        ----------
        id: int
            ID do item

        """

        self.__id = id
    
    @property
    def id(self) -> int:

        """Obtém o ID do item

        Returns
        -------
        int
            ID do item

        """