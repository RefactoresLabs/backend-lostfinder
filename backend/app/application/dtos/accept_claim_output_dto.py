class AcceptClaimOutputDTO:

    """Objeto de transferência de dados de saída do caso de uso de aceitar uma negociação de recuperação de item"""

    def __init__(self, retrieval_code: str) -> None:

        """Inicializa os atributos de instância de AcceptClaimOutputDTO

        Parameters
        ----------
        retrieval_code: str
            Código de recuperação da negociação aceita

        """

        self.__retrieval_code = retrieval_code
    
    @property
    def retrieval_code(self) -> str:

        """Obtém o código de recuperação da negociação aceita

        Returns
        -------
        str
            Código de recuperação da negociação aceita

        """

        return self.__retrieval_code