from backend.app.domain.repositories.found_item_repository_interface import FoundItemRepositoryInterface
from backend.app.domain.repositories.category_repository_interface import CategoryRepositoryInterface
from backend.app.domain.repositories.building_space_repository_interface import BuildingSpaceRepositoryInterface
from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface
from backend.app.domain.entities.found_item import FoundItem
from backend.app.domain.value_objects.image import Image
from backend.app.domain.exceptions.category_doesnt_exist_error import CategoryDoesntExistError
from backend.app.domain.exceptions.building_space_doesnt_exist_error import BuildingSpaceDoesntExistError
from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError

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

    def execute(self, dto: CreateFoundItemDTO) -> None:

        """Executa o fluxo de eventos do caso de uso criar item encontrado

        Parameters
        ----------
        dto: CreateFoundItemDTO
            Objeto de transferência de dados com as informações do item encontrado

        Raises
        ------
        CategoryDoesntExistError
            Exceção levantada quando a categoria não é encontrada
        
        BuildingSpaceDoesntExistError
            Exceção levantada quando o espaço do prédio não é encontrado
        
        UserAccountDoesntExistError
            Exceção levantada quando a conta de usuário não é encontrada
            
        """

        category = self.__category_repository.get_category_by_id(dto.category_id)

        if category is None:

            raise CategoryDoesntExistError("Categoria não encontrada")

        found_building_space = self.__building_space_repository.get_building_space_by_id(dto.found_building_space_id)

        if found_building_space is None:

            raise BuildingSpaceDoesntExistError("Espaço do prédio onde o item foi encontrado não encontrado")

        left_building_space = self.__building_space_repository.get_building_space_by_id(dto.left_building_space_id)

        if left_building_space is None:

            raise BuildingSpaceDoesntExistError("Espaço do prédio onde o item foi deixado não encontrado")

        user_account = self.__user_account_repository.get_user_account_by_id(dto.user_id)

        if user_account is None:

            raise UserAccountDoesntExistError("Conta de usuário não encontrada")

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

        _ = self.__found_item_repository.create_new_found_item(found_item)
