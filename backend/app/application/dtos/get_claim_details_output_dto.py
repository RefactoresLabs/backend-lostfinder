class GetClaimDetailsOutputDTO:

    """Objeto de transferência de dados para saída dos casos de uso de obtenção dos dados detalhados de uma negociação de recuperação"""

    def __init__(
        self,
        claim_id: int,
        status_name: str,
        claimant_user_name: str,
        claimant_user_phone: str,
        associated_found_item_id: int,
        associated_found_item_name: str,
        created_at: str,
        retrieval_code: str
    ) -> None:

        """Inicializa os atributos de instância de GetClaimDetailsOutputDTO

        Parameters
        ----------
        claim_id: int
            ID da negociação
        
        status_name: str
            Nome do status da negociação
        
        claimant_user_name: str
            Nome do usuário que criou a negociação
        
        claimant_user_phone: str
            Telefone do usuário que criou a negociação
        
        associated_found_item_id: int
            ID do item encontrado associado à negociação
        
        associated_found_item_name: str
            Nome do item encontrado associado à negociação
        
        created_at: str
            Data e hora em que a negociação foi criada
        
        retrieval_code: str
            Código de recuperação da negociação

        """

        self.__claim_id = claim_id
        self.__status_name = status_name
        self.__claimant_user_name = claimant_user_name
        self.__claimant_user_phone = claimant_user_phone
        self.__associated_found_item_id = associated_found_item_id
        self.__associated_found_item_name = associated_found_item_name
        self.__created_at = created_at
        self.__retrieval_code = retrieval_code

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
    def status_name(self) -> str:

        """Obtém o nome do status da negociação

        Returns
        -------
        str
            Nome do status

        """

        return self.__status_name

    @property
    def claimant_user_name(self) -> str:

        """Obtém o nome do usuário que criou a negociação

        Returns
        -------
        str
            Nome do usuário

        """

        return self.__claimant_user_name

    @property
    def claimant_user_phone(self) -> str:

        """Obtém o telefone do usuário que criou a negociação

        Returns
        -------
        str
            Telefone do usuário

        """

        return self.__claimant_user_phone

    @property
    def associated_found_item_id(self) -> int:

        """Obtém o ID do item encontrado associado à negociação

        Returns
        -------
        int
            ID do item encontrado

        """

        return self.__associated_found_item_id

    @property
    def associated_found_item_name(self) -> str:

        """Obtém o nome do item encontrado associado à negociação

        Returns
        -------
        str
            Nome do item encontrado

        """

        return self.__associated_found_item_name

    @property
    def created_at(self) -> str:

        """Obtém a data e hora da criação da negociação

        Returns
        -------
        str
            Data e hora em formato ISO

        """

        return self.__created_at
    
    @property
    def retrieval_code(self) -> str:

        """Obtém o código de recuperação da negociação

        Returns
        -------
        str
            Código de recuperação da negociação

        """

        return self.__retrieval_code
