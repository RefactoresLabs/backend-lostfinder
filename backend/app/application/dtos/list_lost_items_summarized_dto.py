class ListLostItemsSummarizedDTO:

    """Objeto de transferência de dados do caso de uso de listar itens perdidos resumidamente"""

    def __init__(self, item_id: int, item_name: str, user_name: str, category_name: str, building_space_name: str, image_url: str) -> None:

        """Inicializa os atributos de instância de ListLostItemsSummarizedDTO

        Parameters
        ----------
        item_id: int
            ID do item perdido

        item_name: str
            Nome do item perdido
        
        user_name: str
            Nome completo do usuário associado ao item perdido
        
        category_name: str
            Nome da categoria que o item perdido pertence
        
        building_space_name: str
            Nome do espaço do prédio que o item foi perdido (aproximado)
        
        image_url: str
            URL da primeira imagem associada ao item

        """

        self.__item_id = item_id
        self.__item_name = item_name
        self.__user_name = user_name
        self.__category_name = category_name
        self.__building_space_name = building_space_name
        self.__image_url = image_url
    
    @property
    def item_id(self) -> int:

        """Obtém o ID do item perdido

        Returns
        -------
        int
            ID do item perdido

        """

        return self.__item_id
    
    @property
    def item_name(self) -> str:

        """Obtém o nome do item perdido

        Returns
        -------
        str
            Nome do item perdido

        """

        return self.__item_name
    
    @property
    def user_name(self) -> str:

        """Obtém o nome completo do usuário associado do item perdido

        Returns
        -------
        str
            Nome completo do usuário associado do item perdido

        """

        return self.__user_name
    
    @property
    def category_name(self) -> str:

        """Obtém o nome da categoria do item perdido

        Returns
        -------
        str
            Nome da categoria do item perdido

        """

        return self.__category_name
    
    @property
    def building_space_name(self) -> str:

        """Obtém o nome do espaço do prédio do item perdido

        Returns
        -------
        str
            Nome do espaço do prédio do item perdido

        """

        return self.__building_space_name

    @property
    def image_url(self) -> str:

        """Obtém a URL da primeira imagem do item perdido

        Returns
        -------
        str
            URL da primeira imagem do item perdido

        """

        return self.__image_url