class ListCreatedClaimsSummarizedDTO:

    """Objeto de transferência de dados para o caso de uso de listar negociações criadas resumidamente"""

    def __init__(
        self,
        claim_id: int,
        claimant_user_name: str,
        found_item_id: int,
        found_item_name: str,
    ) -> None:

        """Inicializa os atributos de instância de ListCreatedClaimsSummarizedDTO

        Parameters
        ----------
        claim_id: int
            ID da negociação

        claimant_user_name: str
            Nome do usuário que realizou a negociação

        found_item_id: int
            ID do item encontrado associado à negociação

        found_item_name: str
            Nome do item encontrado associado à negociação

        """

        self.__claim_id = claim_id
        self.__claimant_user_name = claimant_user_name
        self.__found_item_id = found_item_id
        self.__found_item_name = found_item_name

    @property
    def claim_id(self) -> int:

        """Obtém o ID da negociação

        Returns
        -------
        int
            ID da negociação

        """

        return self.__claim_id

    @property
    def claimant_user_name(self) -> str:

        """Obtém o nome do usuário que realizou a negociação

        Returns
        -------
        str
            Nome do usuário claimant

        """

        return self.__claimant_user_name

    @property
    def found_item_id(self) -> int:

        """Obtém o ID do item encontrado associado

        Returns
        -------
        int
            ID do item encontrado

        """

        return self.__found_item_id

    @property
    def found_item_name(self) -> str:

        """Obtém o nome do item encontrado associado

        Returns
        -------
        str
            Nome do item encontrado

        """

        return self.__found_item_name