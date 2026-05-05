class ListItemsSummarizedDTO:

    """Objeto de transferência de dados para os casos de uso de listar itens resumidamente (perdidos ou encontrados), associados ou não a uma conta de usuário"""

    def __init__(self, item_id: int, item_name: str, user_name: str, category_name: str, building_space_name: str, image_url: str) -> None:

        """Inicializa os atributos de instância de ListItemsSummarizedDTO

        Parameters
        ----------
        item_id: int
            ID do item

        item_name: str
            Nome do item
        
        user_name: str
            Nome completo do usuário associado ao item
        
        category_name: str
            Nome da categoria que o item pertence
        
        building_space_name: str
            Nome do espaço do prédio que o item foi perdido (item perdido) ou que foi encontrado (item encontrado)
        
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

        """Obtém o ID do item

        Returns
        -------
        int
            ID do item

        """

        return self.__item_id
    
    @property
    def item_name(self) -> str:

        """Obtém o nome do item

        Returns
        -------
        str
            Nome do item

        """

        return self.__item_name
    
    @property
    def user_name(self) -> str:

        """Obtém o nome completo do usuário associado do item

        Returns
        -------
        str
            Nome completo do usuário associado do item

        """

        return self.__user_name
    
    @property
    def category_name(self) -> str:

        """Obtém o nome da categoria do item

        Returns
        -------
        str
            Nome da categoria do item

        """

        return self.__category_name
    
    @property
    def building_space_name(self) -> str:

        """Obtém o nome do espaço do prédio do item

        Returns
        -------
        str
            Nome do espaço do prédio do item

        """

        return self.__building_space_name

    @property
    def image_url(self) -> str:

        """Obtém a URL da primeira imagem do item

        Returns
        -------
        str
            URL da primeira imagem do item

        """

        return self.__image_url