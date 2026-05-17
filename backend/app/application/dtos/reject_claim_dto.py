class RejectClaimDTO:

    """Objeto de transferência de dados do caso de uso de rejeitar uma negociação de recuperação de item"""

    def __init__(self, claim_id: int, user_id: int) -> None:

        """Inicializa os atributos de instância de RejectClaimDTO

        Parameters
        ----------
        claim_id: int
            ID da negociação a ser rejeitada

        user_id: int
            ID da conta de usuário que rejeitará a negociação

        """

        self.__claim_id = claim_id
        self.__user_id = user_id
    
    @property
    def claim_id(self) -> int:

        """Obtém o ID da negociação a ser rejeitada

        Returns
        -------
        int
            ID da negociação a ser rejeitada

        """

        return self.__claim_id

    @property
    def user_id(self) -> int:

        """Obtém o ID da conta de usuário que rejeitará a negociação

        Returns
        -------
        int
            ID da conta de usuário que rejeitará a negociação

        """

        return self.__user_id

        