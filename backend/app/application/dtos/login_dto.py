class LoginDTO:

    """Objeto de transferência de dados para a autenticação de conta de usuário"""

    def __init__(self, email: str, password: str) -> None:

        """Inicializa os atributos de instância de LoginDTO

        Parameters
        ----------
        email: str
            E-mail da conta de usuário

        password: str
            Senha da conta de usuário
        """

        self.__email = email
        self.__password = password

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
    def password(self) -> str:

        """Obtém a senha da conta de usuário

        Returns
        -------
        str
            Senha da conta de usuário

        """

        return self.__password
