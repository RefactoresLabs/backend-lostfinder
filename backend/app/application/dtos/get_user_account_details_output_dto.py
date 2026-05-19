class GetUserAccountDetailsOutputDTO:

    """Objeto de transferência de dados de saída do caso de uso de obter os detalhes de uma conta de usuário"""

    def __init__(
            self, 
            id: int,
            name: str,
            email: str,
            phone: str,
            score: int
        ) -> None:

        """Inicializa os atributos de instância de GetUserAccountDetailsOutputDTO

        Parameters
        ----------
        id: int
            ID da conta de usuário
        
        name: str
            Nome da conta de usuário
        
        email: str
            E-mail da conta de usuário
        
        phone: str
            Telefone da conta de usuário
        
        score: int
            Pontuação da conta de usuário

        """

        self.__id = id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__score = score

    @property
    def id(self) -> int:

        """Obtém o ID da conta de usuário

        Returns
        -------
        int
            ID da conta de usuário

        """

        return self.__id

    @property
    def name(self) -> str:

        """Obtém o nome da conta de usuário

        Returns
        -------
        str
            Nome da conta de usuário

        """

        return self.__name
    
    @property
    def email(self) -> str:

        """Obtém o e-mail da conta de usuário

        Returns
        -------
        str
            E-mail da conta de usuário

        """

        return self.__email
    
    @property
    def phone(self) -> str:

        """Obtém o telefone da conta de usuário

        Returns
        -------
        str
            Telefone da conta de usuário

        """

        return self.__phone
    
    @property
    def score(self) -> int:

        """Obtém a pontuação da conta de usuário

        Returns
        -------
        int
            Pontuação da conta de usuário

        """

        return self.__score