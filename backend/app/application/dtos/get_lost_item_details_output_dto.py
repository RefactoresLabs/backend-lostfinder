class GetLostItemDetailsOutputDTO:

    """Objeto de transferência de dados para saída dos casos de uso de obtenção dos dados detalhados de item perdido"""

    def __init__(
            self, 
            item_id: int,
            item_name: str,
            item_description: str,
            item_image_urls: list[str],
            item_category_name: str,
            user_name: str,
            user_email: str,
            user_phone: str,
            lost_building_space_name: str,
            lost_building_name: str,
            lost_localization_cep: str,
            lost_localization_neighborhood: str,
            lost_localization_street: str
            ) -> None:

        """Inicializa os atributos de instância de GetLostItemDetailsOutputDTO

        Parameters
        ----------
        item_id: int
            Identificador do item perdido
        
        item_name: str
            Nome do item perdido
        
        item_description: str
            Descrição do item perdido
        
        item_image_urls: list[str]
            Lista de URLs das imagens do item perdido
        
        item_category_name: str
            Nome da categoria do item perdido
        
        user_name: str
            Nome do usuário associado ao item perdido
        
        user_email: str
            E-mail do usuário associado ao item perdido
        
        user_phone: str
            Telefone do usuário associado ao item perdido
        
        lost_building_space_name: str
            Nome do espaço do prédio onde o item foi perdido
        
        lost_building_name: str
            Nome do prédio onde o item foi perdido
        
        lost_localization_cep: str
            CEP da localização onde o item foi perdido
        
        lost_localization_neighborhood: str
            Bairro da localização onde o item foi perdido
        
        lost_localization_street: str
            Rua da localização onde o item foi perdido
        """

        self.__item_id = item_id
        self.__item_name = item_name
        self.__item_description = item_description
        self.__item_image_urls = item_image_urls
        self.__item_category_name = item_category_name
        self.__user_name = user_name
        self.__user_email = user_email
        self.__user_phone = user_phone
        self.__lost_building_space_name = lost_building_space_name
        self.__lost_building_name = lost_building_name
        self.__lost_localization_cep = lost_localization_cep
        self.__lost_localization_neighborhood = lost_localization_neighborhood
        self.__lost_localization_street = lost_localization_street

    @property
    def item_id(self) -> int:

        """Obtém o identificador do item perdido

        Returns
        -------
        int
            Identificador do item perdido
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
    def item_description(self) -> str:

        """Obtém a descrição do item perdido

        Returns
        -------
        str
            Descrição do item perdido
        """

        return self.__item_description

    @property
    def item_image_urls(self) -> list[str]:

        """Obtém as URLs das imagens do item perdido

        Returns
        -------
        list[str]
            Lista de URLs das imagens do item perdido
        """

        return self.__item_image_urls

    @property
    def item_category_name(self) -> str:

        """Obtém o nome da categoria do item perdido

        Returns
        -------
        str
            Nome da categoria do item perdido
        """

        return self.__item_category_name

    @property
    def user_name(self) -> str:

        """Obtém o nome do usuário associado ao item perdido

        Returns
        -------
        str
            Nome do usuário
        """

        return self.__user_name

    @property
    def user_email(self) -> str:

        """Obtém o e-mail do usuário associado ao item perdido

        Returns
        -------
        str
            E-mail do usuário
        """

        return self.__user_email

    @property
    def user_phone(self) -> str:

        """Obtém o telefone do usuário associado ao item perdido

        Returns
        -------
        str
            Telefone do usuário
        """

        return self.__user_phone

    @property
    def lost_building_space_name(self) -> str:

        """Obtém o nome do espaço do prédio onde o item foi perdido

        Returns
        -------
        str
            Nome do espaço do prédio
        """

        return self.__lost_building_space_name

    @property
    def lost_building_name(self) -> str:

        """Obtém o nome do prédio onde o item foi perdido

        Returns
        -------
        str
            Nome do prédio
        """

        return self.__lost_building_name

    @property
    def lost_localization_cep(self) -> str:

        """Obtém o CEP da localização onde o item foi perdido

        Returns
        -------
        str
            CEP da localização
        """

        return self.__lost_localization_cep

    @property
    def lost_localization_neighborhood(self) -> str:

        """Obtém o bairro da localização onde o item foi perdido

        Returns
        -------
        str
            Bairro da localização
        """

        return self.__lost_localization_neighborhood

    @property
    def lost_localization_street(self) -> str:

        """Obtém a rua da localização onde o item foi perdido

        Returns
        -------
        str
            Rua da localização
        """

        return self.__lost_localization_street