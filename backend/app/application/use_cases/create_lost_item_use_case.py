from backend.app.domain.repositories.lost_item_repository_interface import LostItemRepositoryInterface
from backend.app.domain.repositories.category_repository_interface import CategoryRepositoryInterface
from backend.app.domain.repositories.building_space_repository_interface import BuildingSpaceRepositoryInterface
from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface
from backend.app.domain.entities.lost_item import LostItem
from backend.app.domain.value_objects.image import Image
from backend.app.domain.exceptions.category_doesnt_exist_error import CategoryDoesntExistError
from backend.app.domain.exceptions.building_space_doesnt_exist_error import BuildingSpaceDoesntExistError
from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError

from backend.app.application.dtos.create_lost_item_dto import CreateLostItemDTO


class CreateLostItemUseCase:

    """Caso de uso responsável pelo registro de um item perdido"""

    def __init__(
        self,
        lost_item_repository: LostItemRepositoryInterface,
        category_repository: CategoryRepositoryInterface,
        building_space_repository: BuildingSpaceRepositoryInterface,
        user_account_repository: UserAccountRepositoryInterface,
    ) -> None:

        """Inicializa os atributos de instância de CreateLostItemUseCase

        Parameters
        ----------
        lost_item_repository: LostItemRepositoryInterface
            Repositório do item perdido para persistência dos dados

        category_repository: CategoryRepositoryInterface
            Repositório da categoria para busca dos dados

        building_space_repository: BuildingSpaceRepositoryInterface
            Repositório do espaço do prédio para busca dos dados

        user_account_repository: UserAccountRepositoryInterface
            Repositório da conta de usuário para busca dos dados

        """

        self.__lost_item_repository = lost_item_repository
        self.__category_repository = category_repository
        self.__building_space_repository = building_space_repository
        self.__user_account_repository = user_account_repository

    def execute(self, dto: CreateLostItemDTO) -> None:

        """Executa o fluxo de eventos do caso de uso criar item perdido

        Parameters
        ----------
        dto: CreateLostItemDTO
            Objeto de transferência de dados com as informações do item perdido

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

        building_space = self.__building_space_repository.get_building_space_by_id(dto.lost_building_space_id)

        if building_space is None:

            raise BuildingSpaceDoesntExistError("Espaço do prédio não encontrado")

        user_account = self.__user_account_repository.get_user_account_by_id(dto.user_id)

        if user_account is None:

            raise UserAccountDoesntExistError("Conta de usuário não encontrada")

        images = [Image(url=url) for url in dto.image_urls]

        lost_item = LostItem(
            id=None,
            name=dto.name,
            description=dto.description,
            images=images,
            category=category,
            associated_user_account=user_account,
            approx_lost_building_space=building_space,
        )

        _ = self.__lost_item_repository.create_new_lost_item(lost_item)
