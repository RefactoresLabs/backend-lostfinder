class GetUserAccountDetailsInputDTO:

    """Objeto de transferência de dados de entrada do caso de uso de obter os detalhes de uma conta de usuário"""

    def __init__(self, user_id: int) -> None:

        """Inicializa os atributos de instância de GetUserAccountDetailsInputDTO

        Parameters
        ----------
        user_id: int
            ID da conta de usuário

        """

        self.__user_id = user_id

    @property
    def user_id(self) -> int:

        """Obtém o ID da conta de usuário

        Returns
        -------
        int
            ID da conta de usuário

        """

        return self.__user_id