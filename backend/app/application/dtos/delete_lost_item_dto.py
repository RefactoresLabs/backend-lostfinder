class DeleteLostItemDTO:

    """Objeto de transferência de dados para o caso de uso de exclusão de item perdido"""

    def __init__(self, item_id: int) -> None:

        """Inicializa os atributos de instância de DeleteLostItemDTO

        Parameters
        ----------
        item_id: int
            ID do item perdido a ser excluído

        """

        self.__item_id = item_id

    @property
    def item_id(self) -> int:

        """Obtém o ID do item perdido a ser excluído

        Returns
        -------
        int
            ID do item perdido

        """

        return self.__item_id
