class ListBuildingSpacesInputDTO:

    """Objeto de transferência de dados da entrada do caso de uso de listar espaços de um prédio"""

    def __init__(self, building_id: int) -> None:

        """Inicializa os atributos de instância de ListBuildingSpacesInputDTO

        Parameters
        ----------
        building_id: int
            ID do prédio cujos espaços serão obtidos

        """

        self.__building_id = building_id
    
    @property
    def building_id(self) -> int:

        """Obtém o ID do prédio cujos espaços serão obtidos

        Returns
        -------
        int
            ID do prédio associado aos espaços

        """

        return self.__building_id