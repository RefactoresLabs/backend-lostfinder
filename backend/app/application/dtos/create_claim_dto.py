class CreateClaimDTO:

    """Objeto de transferência de dados para o caso de uso de criar uma negociação de recuperação de item"""

    def __init__(self, found_item_id: int, user_id: int) -> None:

        """Inicializa os atributos de instância de CreateClaimDTO

        Parameters
        ----------
        found_item_id: int
            ID do item encontrado associado a negociação
        
        user_id: int
            ID da conta de usuário que irá criar a negociação

        """

        self.__found_item_id = found_item_id
        self.__user_id = user_id
    
    @property
    def found_item_id(self) -> int:

        """Obtém o ID do item encontrado associado a negociação

        Returns
        -------
        int
            ID do item encontrado associado a negociação

        """

        return self.__found_item_id

    @property
    def user_id(self) -> int:

        """Obtém o ID da conta de usuário que irá criar a negociação

        Returns
        -------
        int
            ID da conta de usuário que irá criar a negociação

        """

        return self.__user_id