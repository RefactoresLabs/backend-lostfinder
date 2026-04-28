from backend.app.domain.repositories.lost_item_repository_interface import LostItemRepositoryInterface
from backend.app.domain.repositories.category_repository_interface import CategoryRepositoryInterface
from backend.app.domain.repositories.building_space_repository_interface import BuildingSpaceRepositoryInterface
from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface
from backend.app.domain.entities.lost_item import LostItem
from backend.app.domain.value_objects.image import Image

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

    def execute(self, dto: CreateLostItemDTO) -> dict:

        """Executa o fluxo de eventos do caso de uso criar item perdido

        Parameters
        ----------
        dto: CreateLostItemDTO
            Objeto de transferência de dados com as informações do item perdido

        Returns
        -------
        dict
            Dicionário com os dados do item perdido registrado

        Raises
        ------
        ValueError
            Se a categoria, espaço do prédio ou conta de usuário não forem encontrados

        """

        category = self.__category_repository.get_category_by_id(dto.category_id)

        if category is None:

            raise ValueError("Categoria não encontrada")

        building_space = self.__building_space_repository.get_building_space_by_id(dto.lost_building_space_id)

        if building_space is None:

            raise ValueError("Espaço do prédio não encontrado")

        user_account = self.__user_account_repository.get_user_account_by_id(dto.user_id)

        if user_account is None:

            raise ValueError("Conta de usuário não encontrada")

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

        created_lost_item = self.__lost_item_repository.create_new_lost_item(lost_item)

        return {
            "id": created_lost_item.id,
            "name": created_lost_item.name,
            "description": created_lost_item.description,
            "category": created_lost_item.category.name,
            "lost_building_space": created_lost_item.approx_lost_building_space.name,
        }
