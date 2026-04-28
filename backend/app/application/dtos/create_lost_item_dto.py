class CreateLostItemDTO:

    """Objeto de transferência de dados para o registro de item perdido"""

    def __init__(self, name: str, description: str, image_urls: list[str], category_id: int, user_id: int, lost_building_space_id: int) -> None:

        """Inicializa os atributos de instância de CreateLostItemDTO

        Parameters
        ----------
        name: str
            Nome do item perdido

        description: str
            Descrição do item perdido

        image_urls: list[str]
            Lista de URLs das imagens do item

        category_id: int
            Identificador da categoria do item

        user_id: int
            Identificador da conta de usuário que registrou o item

        lost_building_space_id: int
            Identificador do espaço do prédio onde o item foi perdido

        """

        self.__name = name
        self.__description = description
        self.__image_urls = list(image_urls)
        self.__category_id = category_id
        self.__user_id = user_id
        self.__lost_building_space_id = lost_building_space_id

    @property
    def name(self) -> str:

        """Obtém o nome do item perdido

        Returns
        -------
        str
            Nome do item perdido

        """

        return self.__name

    @property
    def description(self) -> str:

        """Obtém a descrição do item perdido

        Returns
        -------
        str
            Descrição do item perdido

        """

        return self.__description

    @property
    def image_urls(self) -> list[str]:

        """Obtém a lista de URLs das imagens do item

        Returns
        -------
        list[str]
            Lista de URLs das imagens do item

        """

        return list(self.__image_urls)

    @property
    def category_id(self) -> int:

        """Obtém o identificador da categoria do item

        Returns
        -------
        int
            Identificador da categoria do item

        """

        return self.__category_id

    @property
    def user_id(self) -> int:

        """Obtém o identificador da conta de usuário

        Returns
        -------
        int
            Identificador da conta de usuário

        """

        return self.__user_id

    @property
    def lost_building_space_id(self) -> int:

        """Obtém o identificador do espaço do prédio onde o item foi perdido

        Returns
        -------
        int
            Identificador do espaço do prédio

        """

        return self.__lost_building_space_id
