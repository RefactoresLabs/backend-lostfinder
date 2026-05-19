from backend.app.domain.repositories.found_item_repository_interface import FoundItemRepositoryInterface
from backend.app.domain.repositories.category_repository_interface import CategoryRepositoryInterface
from backend.app.domain.repositories.building_space_repository_interface import BuildingSpaceRepositoryInterface

from backend.app.domain.entities.found_item import FoundItem
from backend.app.domain.value_objects.image import Image
from backend.app.domain.exceptions.category_doesnt_exist_error import CategoryDoesntExistError
from backend.app.domain.exceptions.building_space_doesnt_exist_error import BuildingSpaceDoesntExistError
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError

from backend.app.application.dtos.update_found_item_dto import UpdateFoundItemDTO


class UpdateFoundItemUseCase:

    """Caso de uso responsável pela atualização de um item encontrado"""

    def __init__(
        self,
        found_item_repository: FoundItemRepositoryInterface,
        category_repository: CategoryRepositoryInterface,
        building_space_repository: BuildingSpaceRepositoryInterface,
    ) -> None:

        """Inicializa os atributos de instância de UpdateFoundItemUseCase

        Parameters
        ----------
        found_item_repository: FoundItemRepositoryInterface
            Repositório do item encontrado para persistência dos dados

        category_repository: CategoryRepositoryInterface
            Repositório da categoria para busca dos dados

        building_space_repository: BuildingSpaceRepositoryInterface
            Repositório do espaço do prédio para busca dos dados

        """

        self.__found_item_repository = found_item_repository
        self.__category_repository = category_repository
        self.__building_space_repository = building_space_repository

    def execute(self, dto: UpdateFoundItemDTO) -> None:

        """Executa o fluxo de eventos do caso de uso atualizar item encontrado

        Parameters
        ----------
        dto: UpdateFoundItemDTO
            Objeto de transferência de dados com as informações do item encontrado a atualizar

        Raises
        ------
        ItemDoesntExistError
            Exceção levantada quando o item não é encontrado

        CategoryDoesntExistError
            Exceção levantada quando a categoria não é encontrada

        BuildingSpaceDoesntExistError
            Exceção levantada quando o espaço do prédio não é encontrado

        """

        found_item = self.__found_item_repository.get_found_item_by_id(dto.item_id)

        if found_item is None:

            raise ItemDoesntExistError("Item não encontrado")

        category = self.__category_repository.get_category_by_id(dto.category_id)

        if category is None:

            raise CategoryDoesntExistError("Categoria não encontrada")

        found_building_space = self.__building_space_repository.get_building_space_by_id(dto.found_building_space_id)

        if found_building_space is None:

            raise BuildingSpaceDoesntExistError("Espaço do prédio não encontrado")

        left_building_space = self.__building_space_repository.get_building_space_by_id(dto.left_building_space_id)

        if left_building_space is None:

            raise BuildingSpaceDoesntExistError("Espaço do prédio não encontrado")

        images = [Image(url=url) for url in dto.image_urls]

        updated_found_item = FoundItem(
            id=dto.item_id,
            name=dto.name,
            description=dto.description,
            images=images,
            category=category,
            associated_user_account=found_item.associated_user_account,
            found_building_space=found_building_space,
            left_building_space=left_building_space,
            registration_date=found_item.registration_date,
        )

        self.__found_item_repository.update_found_item(updated_found_item, dto.item_id)
