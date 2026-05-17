class DeleteClaimDTO:

    """Objeto de transferência de dados para o caso de uso de exclusão de uma negociação"""

    def __init__(self, claim_id: int) -> None:

        """Inicializa os atributos de instância de DeleteClaimDTO

        Parameters
        ----------
        claim_id: int
            ID da negociação a ser excluída

        """

        self.__claim_id = claim_id

    @property
    def claim_id(self) -> int:

        """Obtém o ID da negociação a ser excluída

        Returns
        -------
        int
            ID da negociação

        """

        return self.__claim_id
