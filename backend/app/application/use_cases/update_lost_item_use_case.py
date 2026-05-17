from backend.app.domain.repositories.lost_item_repository_interface import LostItemRepositoryInterface
from backend.app.domain.repositories.category_repository_interface import CategoryRepositoryInterface
from backend.app.domain.repositories.building_space_repository_interface import BuildingSpaceRepositoryInterface

from backend.app.domain.entities.lost_item import LostItem
from backend.app.domain.value_objects.image import Image
from backend.app.domain.exceptions.category_doesnt_exist_error import CategoryDoesntExistError
from backend.app.domain.exceptions.building_space_doesnt_exist_error import BuildingSpaceDoesntExistError
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError

from backend.app.application.dtos.update_lost_item_dto import UpdateLostItemDTO


class UpdateLostItemUseCase:

    """Caso de uso responsável pela atualização de um item perdido"""

    def __init__(
        self,
        lost_item_repository: LostItemRepositoryInterface,
        category_repository: CategoryRepositoryInterface,
        building_space_repository: BuildingSpaceRepositoryInterface,
    ) -> None:

        """Inicializa os atributos de instância de UpdateLostItemUseCase

        Parameters
        ----------
        lost_item_repository: LostItemRepositoryInterface
            Repositório do item perdido para persistência dos dados

        category_repository: CategoryRepositoryInterface
            Repositório da categoria para busca dos dados

        building_space_repository: BuildingSpaceRepositoryInterface
            Repositório do espaço do prédio para busca dos dados

        """

        self.__lost_item_repository = lost_item_repository
        self.__category_repository = category_repository
        self.__building_space_repository = building_space_repository

    def execute(self, dto: UpdateLostItemDTO) -> None:

        """Executa o fluxo de eventos do caso de uso atualizar item perdido

        Parameters
        ----------
        dto: UpdateLostItemDTO
            Objeto de transferência de dados com as informações do item perdido a atualizar

        Raises
        ------
        ItemDoesntExistError
            Exceção levantada quando o item não é encontrado

        CategoryDoesntExistError
            Exceção levantada quando a categoria não é encontrada

        BuildingSpaceDoesntExistError
            Exceção levantada quando o espaço do prédio não é encontrado

        """

        lost_item = self.__lost_item_repository.get_lost_item_by_id(dto.item_id)

        if lost_item is None:

            raise ItemDoesntExistError("Item não encontrado")

        category = self.__category_repository.get_category_by_id(dto.category_id)

        if category is None:

            raise CategoryDoesntExistError("Categoria não encontrada")

        building_space = self.__building_space_repository.get_building_space_by_id(dto.lost_building_space_id)

        if building_space is None:

            raise BuildingSpaceDoesntExistError("Espaço do prédio não encontrado")

        images = [Image(url=url) for url in dto.image_urls]

        updated_lost_item = LostItem(
            id=dto.item_id,
            name=dto.name,
            description=dto.description,
            images=images,
            category=category,
            associated_user_account=lost_item.associated_user_account,
            approx_lost_building_space=building_space,
            registration_date=lost_item.registration_date,
        )

        self.__lost_item_repository.update_lost_item(updated_lost_item, dto.item_id)
