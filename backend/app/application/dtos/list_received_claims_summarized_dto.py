class ListReceivedClaimsSummarizedDTO:

    """Objeto de transferência de dados para o caso de uso de listar negociações recebidas resumidamente"""

    def __init__(
        self,
        claim_id: int,
        found_item_id: int,
        found_item_name: str,
        found_item_owner_name: str,
    ) -> None:

        """Inicializa os atributos de instância de ListReceivedClaimsSummarizedDTO

        Parameters
        ----------
        claim_id: int
            ID da negociação

        found_item_id: int
            ID do item encontrado associado à negociação

        found_item_name: str
            Nome do item encontrado associado à negociação

        found_item_owner_name: str
            Nome do dono do item encontrado

        """

        self.__claim_id = claim_id
        self.__found_item_id = found_item_id
        self.__found_item_name = found_item_name
        self.__found_item_owner_name = found_item_owner_name

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

    @property
    def found_item_owner_name(self) -> str:

        """Obtém o nome do dono do item encontrado

        Returns
        -------
        str
            Nome do dono do item encontrado

        """

        return self.__found_item_owner_name