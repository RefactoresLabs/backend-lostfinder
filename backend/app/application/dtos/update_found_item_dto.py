class UpdateFoundItemDTO:

    """Objeto de transferência de dados para o caso de uso de atualização de item encontrado"""

    def __init__(
        self,
        item_id: int,
        name: str,
        description: str,
        category_id: int,
        found_building_space_id: int,
        left_building_space_id: int,
        image_urls: list[str] = None,
    ) -> None:

        """Inicializa os atributos de instância de UpdateFoundItemDTO

        Parameters
        ----------
        item_id: int
            ID do item encontrado a ser atualizado

        name: str
            Nome do item encontrado

        description: str
            Descrição do item encontrado

        category_id: int
            ID da categoria do item

        found_building_space_id: int
            ID do espaço de prédio onde o item foi encontrado

        left_building_space_id: int
            ID do espaço de prédio onde o item foi deixado

        image_urls: list[str]
            Lista de URLs das imagens do item

        """

        self.__item_id = item_id
        self.__name = name
        self.__description = description
        self.__category_id = category_id
        self.__found_building_space_id = found_building_space_id
        self.__left_building_space_id = left_building_space_id
        self.__image_urls = image_urls or []

    @property
    def item_id(self) -> int:

        """Obtém o ID do item encontrado a ser atualizado

        Returns
        -------
        int
            ID do item encontrado

        """

        return self.__item_id

    @property
    def name(self) -> str:

        """Obtém o nome do item encontrado

        Returns
        -------
        str
            Nome do item

        """

        return self.__name

    @property
    def description(self) -> str:

        """Obtém a descrição do item encontrado

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
    def found_building_space_id(self) -> int:

        """Obtém o ID do espaço de prédio onde o item foi encontrado

        Returns
        -------
        int
            ID do espaço de prédio

        """

        return self.__found_building_space_id

    @property
    def left_building_space_id(self) -> int:

        """Obtém o ID do espaço de prédio onde o item foi deixado

        Returns
        -------
        int
            ID do espaço de prédio

        """

        return self.__left_building_space_id

    @property
    def image_urls(self) -> list[str]:

        """Obtém a lista de URLs das imagens do item

        Returns
        -------
        list[str]
            Lista de URLs

        """

        return self.__image_urls
