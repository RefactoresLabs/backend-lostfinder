class DeleteFoundItemDTO:

    """Objeto de transferência de dados para o caso de uso de exclusão de item encontrado"""

    def __init__(self, item_id: int) -> None:

        """Inicializa os atributos de instância de DeleteFoundItemDTO

        Parameters
        ----------
        item_id: int
            ID do item encontrado a ser excluído

        """

        self.__item_id = item_id

    @property
    def item_id(self) -> int:

        """Obtém o ID do item encontrado a ser excluído

        Returns
        -------
        int
            ID do item encontrado

        """

        return self.__item_id
