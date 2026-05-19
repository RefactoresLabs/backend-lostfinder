class AcceptClaimInputDTO:

    """Objeto de transferência de dados de entrada do caso de uso de aceitar uma negociação de recuperação de item"""

    def __init__(self, claim_id: int, user_id: int) -> None:

        """Inicializa os atributos de instância de AcceptClaimInputDTO

        Parameters
        ----------
        claim_id: int
            ID da negociação a ser aceita

        user_id: int
            ID da conta de usuário que aceitará a negociação

        """

        self.__claim_id = claim_id
        self.__user_id = user_id
    
    @property
    def claim_id(self) -> int:

        """Obtém o ID da negociação a ser aceita

        Returns
        -------
        int
            ID da negociação a ser aceita

        """

        return self.__claim_id

    @property
    def user_id(self) -> int:

        """Obtém o ID da conta de usuário que aceitará a negociação

        Returns
        -------
        int
            ID da conta de usuário que aceitará a negociação

        """

        return self.__user_id

        