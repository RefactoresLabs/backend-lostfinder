class GetFoundItemDetailsOutputDTO:

    """Objeto de transferência de dados para saída dos casos de uso de obtenção dos dados detalhados de item encontrado"""

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
            found_building_space_name: str,
            found_building_name: str,
            found_localization_cep: str,
            found_localization_neighborhood: str,
            found_localization_street: str,
            left_building_space_name: str,
            left_building_name: str,
            left_localization_cep: str,
            left_localization_neighborhood: str,
            left_localization_street: str,
            ) -> None:

        """Inicializa os atributos de instância de GetFoundItemDetailsOutputDTO

        Parameters
        ----------
        item_id: int
            Identificador do item encontrado
        
        item_name: str
            Nome do item encontrado
        
        item_description: str
            Descrição do item encontrado
        
        item_image_urls: list[str]
            Lista de URLs das imagens do item encontrado
        
        item_category_name: str
            Nome da categoria do item encontrado
        
        user_name: str
            Nome do usuário associado ao item encontrado
        
        user_email: str
            E-mail do usuário associado ao item encontrado
        
        user_phone: str
            Telefone do usuário associado ao item encontrado
        
        found_building_space_name: str
            Nome do espaço do prédio onde o item foi encontrado
        
        found_building_name: str
            Nome do prédio onde o item foi encontrado
        
        found_localization_cep: str
            CEP da localização onde o item foi encontrado
        
        found_localization_neighborhood: str
            Bairro da localização onde o item foi encontrado
        
        found_localization_street: str
            Rua da localização onde o item foi encontrado
        
        left_building_space_name: str
            Nome do espaço do prédio onde o item foi deixado
        
        left_building_name: str
            Nome do prédio onde o item foi deixado
        
        left_localization_cep: str
            CEP da localização onde o item foi deixado
        
        left_localization_neighborhood: str
            Bairro da localização onde o item foi deixado
        
        left_localization_street: str
            Rua da localização onde o item foi deixado
        """

        self.__item_id = item_id
        self.__item_name = item_name
        self.__item_description = item_description
        self.__item_image_urls = item_image_urls
        self.__item_category_name = item_category_name
        self.__user_name = user_name
        self.__user_email = user_email
        self.__user_phone = user_phone
        self.__found_building_space_name = found_building_space_name
        self.__found_building_name = found_building_name
        self.__found_localization_cep = found_localization_cep
        self.__found_localization_neighborhood = found_localization_neighborhood
        self.__found_localization_street = found_localization_street
        self.__left_building_space_name = left_building_space_name
        self.__left_building_name = left_building_name
        self.__left_localization_cep = left_localization_cep
        self.__left_localization_neighborhood = left_localization_neighborhood
        self.__left_localization_street = left_localization_street

    @property
    def item_id(self) -> int:

        """Obtém o identificador do item encontrado

        Returns
        -------
        int
            Identificador do item encontrado
        """

        return self.__item_id

    @property
    def item_name(self) -> str:

        """Obtém o nome do item encontrado

        Returns
        -------
        str
            Nome do item encontrado
        """

        return self.__item_name

    @property
    def item_description(self) -> str:

        """Obtém a descrição do item encontrado

        Returns
        -------
        str
            Descrição do item encontrado
        """

        return self.__item_description

    @property
    def item_image_urls(self) -> list[str]:

        """Obtém as URLs das imagens do item encontrado

        Returns
        -------
        list[str]
            Lista de URLs das imagens do item encontrado
        """

        return self.__item_image_urls

    @property
    def item_category_name(self) -> str:

        """Obtém o nome da categoria do item encontrado

        Returns
        -------
        str
            Nome da categoria do item encontrado
        """

        return self.__item_category_name

    @property
    def user_name(self) -> str:

        """Obtém o nome do usuário associado ao item encontrado

        Returns
        -------
        str
            Nome do usuário
        """

        return self.__user_name

    @property
    def user_email(self) -> str:

        """Obtém o e-mail do usuário associado ao item encontrado

        Returns
        -------
        str
            E-mail do usuário
        """

        return self.__user_email

    @property
    def user_phone(self) -> str:

        """Obtém o telefone do usuário associado ao item encontrado

        Returns
        -------
        str
            Telefone do usuário
        """

        return self.__user_phone

    @property
    def found_building_space_name(self) -> str:

        """Obtém o nome do espaço do prédio onde o item foi encontrado

        Returns
        -------
        str
            Nome do espaço do prédio
        """

        return self.__found_building_space_name

    @property
    def found_building_name(self) -> str:

        """Obtém o nome do prédio onde o item foi encontrado

        Returns
        -------
        str
            Nome do prédio
        """

        return self.__found_building_name

    @property
    def found_localization_cep(self) -> str:

        """Obtém o CEP da localização onde o item foi encontrado

        Returns
        -------
        str
            CEP da localização
        """

        return self.__found_localization_cep

    @property
    def found_localization_neighborhood(self) -> str:

        """Obtém o bairro da localização onde o item foi encontrado

        Returns
        -------
        str
            Bairro da localização
        """

        return self.__found_localization_neighborhood

    @property
    def found_localization_street(self) -> str:

        """Obtém a rua da localização onde o item foi encontrado

        Returns
        -------
        str
            Rua da localização
        """

        return self.__found_localization_street

    @property
    def left_building_space_name(self) -> str:

        """Obtém o nome do espaço do prédio onde o item foi deixado

        Returns
        -------
        str
            Nome do espaço do prédio
        """

        return self.__left_building_space_name

    @property
    def left_building_name(self) -> str:

        """Obtém o nome do prédio onde o item foi deixado

        Returns
        -------
        str
            Nome do prédio
        """

        return self.__left_building_name

    @property
    def left_localization_cep(self) -> str:

        """Obtém o CEP da localização onde o item foi deixado

        Returns
        -------
        str
            CEP da localização
        """

        return self.__left_localization_cep

    @property
    def left_localization_neighborhood(self) -> str:

        """Obtém o bairro da localização onde o item foi deixado

        Returns
        -------
        str
            Bairro da localização
        """

        return self.__left_localization_neighborhood

    @property
    def left_localization_street(self) -> str:

        """Obtém a rua da localização onde o item foi deixado

        Returns
        -------
        str
            Rua da localização
        """

        return self.__left_localization_street