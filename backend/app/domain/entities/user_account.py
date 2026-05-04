class UserAccount:

    """Representa a entidade conta de usuário da regra de negócio"""

    def __init__(self, id: int | None, name: str, email: str, password: str, phone: str) -> None:

        """Inicializa os atributos de instância de UserAccount

        Parameters
        ----------
        id: int | None
            Identificador da conta de usuário

        name: str
            Nome completo do usuário

        email: str
            E-mail do usuário

        password: str
            Senha do usuário

        phone: str
            Telefone do usuário

        id: int | None
            Identificador único da conta. Opcional (gerado pelo banco)
        """

        self.__id = id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__phone = phone
    
    @property
    def id(self) -> int | None:

        """Obtém o identificador da conta de usuário

        Returns
        -------
        int | None
            ID da conta ou None se ainda não persistida

        """

        return self.__id

    @property
    def name(self) -> str:

        """Obtém o nome completo do usuário

        Returns
        -------
        str
            Nome completo do usuário

        """

        return self.__name

    @property
    def email(self) -> str:

        """Obtém o e-mail do usuário

        Returns
        -------
        str
            E-mail do usuário
        
        """

        return self.__email

    @property
    def password(self) -> str:

        """Obtém a senha do usuário

        Returns
        -------
        str
            Senha do usuário
        
        """

        return self.__password

    @property
    def phone(self) -> str:

        """Obtém o telefone do usuário

        Returns
        -------
        str
            telefone do usuário
        
        """

        return self.__phone
    
    def _set_id(self, id: int) -> None:

        """Modifica o valor do atributo id da conta de usuário uma única vez, caso ela seja None no estado atual

        Parameters
        ----------
        id: int
            Valor a ser definido no atribtuo id
        
        """

        if self.__id is not None:

            raise ValueError("Valor de ID já definido!")
        
        self.__id = id