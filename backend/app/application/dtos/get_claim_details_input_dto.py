class GetClaimDetailsInputDTO:

    """Objeto de transferência de dados para entrada dos casos de uso que recebem o ID de uma negociação"""

    def __init__(self, claim_id: int) -> None:

        """Inicializa os atributos de instância de GetClaimDetailsInputDTO

        Parameters
        ----------
        claim_id: int
            ID da negociação de recuperação

        """

        self.__claim_id = claim_id

    @property
    def claim_id(self) -> int:

        """Obtém o ID da negociação de recuperação

        Returns
        -------
        int
            ID da negociação

        """

        return self.__claim_id
