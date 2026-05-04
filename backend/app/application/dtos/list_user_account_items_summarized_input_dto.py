class ListUserAccountItemsSummarizedInputDTO:

    """Objeto de transferência de dados para entrada dos casos de uso de listar itens encontrados e itens perdidos resumidos de uma conta de usuário específica"""

    def __init__(self, user_id: int) -> None:

        """Inicializa os atributos de instância de ListUserAccountItemsSummarizedInputDTO

        Parameters
        ----------
        user_id: int
            ID da conta de usuário cujos itens estão associados

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