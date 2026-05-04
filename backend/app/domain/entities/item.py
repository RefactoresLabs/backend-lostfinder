from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.entities.category import Category
from backend.app.domain.value_objects.image import Image


from datetime import date


class Item:

    """Representa a entidade item da regra de negócio"""

    def __init__(self, id: int | None, name: str, description: str, images: list[Image], category: Category, associated_user_account: UserAccount, registration_date: date) -> None:

        """Inicaliza os atributos de instância de Item

        Parameters
        ----------
        id: int
            Identificador do item

        name: str
            Nome do item
        
        description: str
            Descrição do item
        
        images: list[Image]
            Imagens do item
        
        category: Category
            Categoria do item
        
        associated_user_account: UserAccount
            Conta de usuário que registrou o item
        
        registration_date: date
            Data de registro do item
        
        """

        self.__id = id
        self.__name = name
        self.__description = description
        self.__registration_date = registration_date
        self.__images = list(images)
        self.__category = category
        self.__associated_user_account = associated_user_account
    
    @property
    def id(self) -> int:

        """Obtém o identificador do item

        Returns
        -------

        int
            Identificador do item

        """

        return self.__id
    
    @property
    def name(self) -> str:

        """Obtém o nome do item

        Returns
        -------

        str
            Nome do item

        """

        return self.__name
    
    @property
    def description(self) -> str:

        """Obtém a descrição do item

        Returns
        -------

        str
            Descrição do item

        """

        return self.__description
    
    def registration_date(self) -> date:

        """Obtém a data de registro do item

        Returns
        -------

        date
            Data de registro do item

        """

        return self.__registration_date
    
    @property
    def images(self) -> list[Image]:

        """Obtém as imagens do item

        Returns
        -------

        list[Image]
            Imagens do item

        """

        return self.__images
    
    @property
    def category(self) -> Category:

        """Obtém a categoria do item

        Returns
        -------

        Category
            Categoria do item

        """

        return self.__category

    @property
    def associated_user_account(self) -> UserAccount:

        """Obtém a conta do usuário que registrou o item

        Returns
        -------

        UserAccount
            Conta de usuário que registrou o item

        """

        return self.__associated_user_account
    
    def _set_id(self, id: int) -> None:

        """Modifica o valor do atributo id do item uma única vez, caso ela seja None no estado atual

        Parameters
        ----------
        id: int
            Valor a ser definido no atribtuo id
        
        """

        if self.__id is not None:

            raise ValueError("Valor de ID já definido!")
        
        self.__id = id