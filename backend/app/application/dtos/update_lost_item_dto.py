class UpdateLostItemDTO:

    """Objeto de transferência de dados para o caso de uso de atualização de item perdido"""

    def __init__(
        self,
        item_id: int,
        name: str,
        description: str,
        category_id: int,
        lost_building_space_id: int,
        image_urls: list[str] = None,
    ) -> None:

        """Inicializa os atributos de instância de UpdateLostItemDTO

        Parameters
        ----------
        item_id: int
            ID do item perdido a ser atualizado

        name: str
            Nome do item perdido

        description: str
            Descrição do item perdido

        category_id: int
            ID da categoria do item

        lost_building_space_id: int
            ID do espaço de prédio onde o item foi perdido

        image_urls: list[str]
            Lista de URLs das imagens do item

        """

        self.__item_id = item_id
        self.__name = name
        self.__description = description
        self.__category_id = category_id
        self.__lost_building_space_id = lost_building_space_id
        self.__image_urls = image_urls or []

    @property
    def item_id(self) -> int:

        """Obtém o ID do item perdido a ser atualizado

        Returns
        -------
        int
            ID do item perdido

        """

        return self.__item_id

    @property
    def name(self) -> str:

        """Obtém o nome do item perdido

        Returns
        -------
        str
            Nome do item

        """

        return self.__name

    @property
    def description(self) -> str:

        """Obtém a descrição do item perdido

        Returns
        -------
        str
            Descrição do item

        """

        return self.__description

    @property
    def category_id(self) -> int:

        """Obtém o ID da categoria do item

        Returns
        -------
        int
            ID da categoria

        """

        return self.__category_id

    @property
    def lost_building_space_id(self) -> int:

        """Obtém o ID do espaço de prédio onde o item foi perdido

        Returns
        -------
        int
            ID do espaço de prédio

        """

        return self.__lost_building_space_id

    @property
    def image_urls(self) -> list[str]:

        """Obtém a lista de URLs das imagens do item

        Returns
        -------
        list[str]
            Lista de URLs

        """

        return self.__image_urls
