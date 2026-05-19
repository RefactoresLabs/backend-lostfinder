class FinishClaimDTO:

    """Objeto de transferência de dados do caso de uso de finalizar uma negociação de recuperação de item"""

    def __init__(self, claim_id: int, user_id: int, retrieval_code: str) -> None:

        """Inicializa os atributos de instância de FinishClaimDTO

        Parameters
        ----------
        claim_id: int
            ID da negociação a ser finalizada
        
        user_id: int
            ID da conta de usuário que finalizará a negociação
        
        retrieval_code: str
            Código de recuperação do item

        """

        self.__claim_id = claim_id
        self.__user_id = user_id
        self.__retrieval_code = retrieval_code
    
    @property
    def claim_id(self) -> int:

        """Obtém o ID da negociação a ser finalizada

        Returns
        -------
        int
            ID da negociação a ser finalizada

        """

        return self.__claim_id

    @property
    def user_id(self) -> int:

        """Obtém o ID da conta de usuário que finalizará a negociação

        Returns
        -------
        int
            ID da conta de usuário que finalizará a negociação

        """

        return self.__user_id

    @property
    def retrieval_code(self) -> str:

        """Obtém o código de recuperação do item

        Returns
        -------
        str
            Código de recuperação do item

        """

        return self.__retrieval_code