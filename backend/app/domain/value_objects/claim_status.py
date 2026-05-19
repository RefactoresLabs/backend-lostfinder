class ClaimStatus:

    """Representa o status de uma negociação de recuperação de item"""

    def __init__(self, name: str) -> None:

        """Inicializa os atributos de instância de ClaimStatus

        Parameters
        ----------
        name: str
            Nome do status

        """

        self.__name = name
    
    @property
    def name(self) -> str:

        """Obtém o nome do status

        Returns
        -------
        str
            Nome do status

        """

        return self.__name