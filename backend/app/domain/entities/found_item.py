from backend.app.domain.entities.item import Item
from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.entities.category import Category
from backend.app.domain.value_objects.image import Image
from backend.app.domain.entities.building_space import BuildingSpace


from datetime import date

class FoundItem(Item):

    """Representa a entidade item perdido da regra de negócio"""

    def __init__(self, id: int, name: str, description: str, images: list[Image], category: Category, associated_user_account: UserAccount, approx_found_building_space: BuildingSpace, approx_left_building_space: BuildingSpace, registration_date: date | None=None) -> None:

        """Inicaliza os atributos de instância de FoundItem

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
        
        approx_found_building_space: BuildingSpace
            Espaço do prédio em que, aproximadamente ou exatamente, o item foi encontrado
        
        approx_left_building_space: BuildingSpace
            Espaço do prédio em que o item foi deixado
        
        registration_date: date (Padrão: None)
            Data de registro do item
        
        """

        super().__init__(id, name, description, images, category, associated_user_account, registration_date)
        self.__approx_found_building_space = approx_found_building_space
        self.__approx_left_building_space = approx_left_building_space
    
    @property
    def approx_found_building_space(self) -> BuildingSpace:

        """Espaço do prédio em que, aproximadamente ou exatamente, o item foi encontrado

        Returns
        -------
        BuildingSpace
            Espaço do prédio aproximado em que o item foi encontrado

        """

        return self.__approx_found_building_space
    
    @property
    def approx_left_building_space(self) -> BuildingSpace:

        """Espaço do prédio em que o item foi deixado

        Returns
        -------
        BuildingSpace
            Espaço do prédio em que o item foi deixado

        """

        return self.__approx_left_building_space