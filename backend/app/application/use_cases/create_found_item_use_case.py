from backend.app.domain.repositories.found_item_repository_interface import FoundItemRepositoryInterface
from backend.app.domain.repositories.category_repository_interface import CategoryRepositoryInterface
from backend.app.domain.repositories.building_space_repository_interface import BuildingSpaceRepositoryInterface
from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface
from backend.app.domain.entities.found_item import FoundItem
from backend.app.domain.value_objects.image import Image

from backend.app.application.dtos.create_found_item_dto import CreateFoundItemDTO


class CreateFoundItemUseCase:

    """Caso de uso responsável pelo registro de um item encontrado"""

    def __init__(
        self,
        found_item_repository: FoundItemRepositoryInterface,
        category_repository: CategoryRepositoryInterface,
        building_space_repository: BuildingSpaceRepositoryInterface,
        user_account_repository: UserAccountRepositoryInterface,
    ) -> None:

        """Inicializa os atributos de instância de CreateFoundItemUseCase

        Parameters
        ----------
        found_item_repository: FoundItemRepositoryInterface
            Repositório do item encontrado para persistência dos dados

        category_repository: CategoryRepositoryInterface
            Repositório da categoria para busca dos dados

        building_space_repository: BuildingSpaceRepositoryInterface
            Repositório do espaço do prédio para busca dos dados

        user_account_repository: UserAccountRepositoryInterface
            Repositório da conta de usuário para busca dos dados

        """

        self.__found_item_repository = found_item_repository
        self.__category_repository = category_repository
        self.__building_space_repository = building_space_repository
        self.__user_account_repository = user_account_repository

    def execute(self, dto: CreateFoundItemDTO) -> dict:

        """Executa o fluxo de eventos do caso de uso criar item encontrado

        Parameters
        ----------
        dto: CreateFoundItemDTO
            Objeto de transferência de dados com as informações do item encontrado

        Returns
        -------
        dict
            Dicionário com os dados do item encontrado registrado

        Raises
        ------
        ValueError
            Se a categoria, espaço do prédio ou conta de usuário não forem encontrados

        """

        category = self.__category_repository.get_category_by_id(dto.category_id)

        if category is None:

            raise ValueError("Categoria não encontrada")

        found_building_space = self.__building_space_repository.get_building_space_by_id(dto.found_building_space_id)

        if found_building_space is None:

            raise ValueError("Espaço do prédio onde o item foi encontrado não encontrado")

        left_building_space = self.__building_space_repository.get_building_space_by_id(dto.left_building_space_id)

        if left_building_space is None:

            raise ValueError("Espaço do prédio onde o item foi deixado não encontrado")

        user_account = self.__user_account_repository.get_user_account_by_id(dto.user_id)

        if user_account is None:

            raise ValueError("Conta de usuário não encontrada")

        images = [Image(url=url) for url in dto.image_urls]

        found_item = FoundItem(
            id=None,
            name=dto.name,
            description=dto.description,
            images=images,
            category=category,
            associated_user_account=user_account,
            approx_found_building_space=found_building_space,
            approx_left_building_space=left_building_space,
        )

        created_found_item = self.__found_item_repository.create_new_found_item(found_item)

        return {
            "id": created_found_item.id,
            "name": created_found_item.name,
            "description": created_found_item.description,
            "category": created_found_item.category.name,
            "found_building_space": created_found_item.approx_found_building_space.name,
            "left_building_space": created_found_item.approx_left_building_space.name,
        }
