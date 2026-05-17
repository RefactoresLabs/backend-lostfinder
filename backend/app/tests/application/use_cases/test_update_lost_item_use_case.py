from unittest.mock import Mock
import pytest

from backend.app.application.use_cases.update_lost_item_use_case import UpdateLostItemUseCase
from backend.app.application.dtos.update_lost_item_dto import UpdateLostItemDTO
from backend.app.domain.entities.lost_item import LostItem
from backend.app.domain.entities.category import Category
from backend.app.domain.entities.building_space import BuildingSpace
from backend.app.domain.entities.building import Building
from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.value_objects.localization import Localization
from backend.app.domain.exceptions.category_doesnt_exist_error import CategoryDoesntExistError
from backend.app.domain.exceptions.building_space_doesnt_exist_error import BuildingSpaceDoesntExistError
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError


def test_update_lost_item_use_case_success():
    fake_lost_repo = Mock()
    fake_cat_repo = Mock()
    fake_space_repo = Mock()

    category = Category(id=1, name="Eletrônicos")
    localization = Localization(cep="123", neighborhood="Bairro", street="Rua")
    building = Building(id=1, name="Prédio A", associated_localization=localization)
    space = BuildingSpace(id=1, name="Sala 101", associated_building=building)
    user = UserAccount(id=1, name="User", email="test@test.com", password="pwd", phone="123")

    existing_item = LostItem(
        id=1,
        name="Chave antiga",
        description="Descrição antiga",
        images=[],
        category=category,
        associated_user_account=user,
        approx_lost_building_space=space,
    )

    fake_lost_repo.get_lost_item_by_id.return_value = existing_item
    fake_cat_repo.get_category_by_id.return_value = category
    fake_space_repo.get_building_space_by_id.return_value = space

    dto = UpdateLostItemDTO(
        item_id=1,
        name="Chave nova",
        description="Descrição nova",
        image_urls=["url1"],
        category_id=1,
        lost_building_space_id=1
    )

    use_case = UpdateLostItemUseCase(
        fake_lost_repo,
        fake_cat_repo,
        fake_space_repo
    )

    use_case.execute(dto)

    fake_lost_repo.update_lost_item.assert_called_once()


def test_update_lost_item_use_case_item_not_found():
    fake_lost_repo = Mock()
    fake_cat_repo = Mock()
    fake_space_repo = Mock()

    fake_lost_repo.get_lost_item_by_id.return_value = None

    dto = UpdateLostItemDTO(
        item_id=1,
        name="Chave",
        description="Chave de carro",
        image_urls=[],
        category_id=1,
        lost_building_space_id=1
    )

    use_case = UpdateLostItemUseCase(
        fake_lost_repo,
        fake_cat_repo,
        fake_space_repo
    )

    with pytest.raises(ItemDoesntExistError, match="Item não encontrado"):
        use_case.execute(dto)


def test_update_lost_item_use_case_category_not_found():
    fake_lost_repo = Mock()
    fake_cat_repo = Mock()
    fake_space_repo = Mock()

    category = Category(id=1, name="Eletrônicos")
    localization = Localization(cep="123", neighborhood="Bairro", street="Rua")
    building = Building(id=1, name="Prédio A", associated_localization=localization)
    space = BuildingSpace(id=1, name="Sala 101", associated_building=building)
    user = UserAccount(id=1, name="User", email="test@test.com", password="pwd", phone="123")

    existing_item = LostItem(
        id=1,
        name="Chave",
        description="Chave de carro",
        images=[],
        category=category,
        associated_user_account=user,
        approx_lost_building_space=space,
    )

    fake_lost_repo.get_lost_item_by_id.return_value = existing_item
    fake_cat_repo.get_category_by_id.return_value = None

    dto = UpdateLostItemDTO(
        item_id=1,
        name="Chave",
        description="Chave de carro",
        image_urls=[],
        category_id=999,
        lost_building_space_id=1
    )

    use_case = UpdateLostItemUseCase(
        fake_lost_repo,
        fake_cat_repo,
        fake_space_repo
    )

    with pytest.raises(CategoryDoesntExistError, match="Categoria não encontrada"):
        use_case.execute(dto)


def test_update_lost_item_use_case_building_space_not_found():
    fake_lost_repo = Mock()
    fake_cat_repo = Mock()
    fake_space_repo = Mock()

    category = Category(id=1, name="Eletrônicos")
    localization = Localization(cep="123", neighborhood="Bairro", street="Rua")
    building = Building(id=1, name="Prédio A", associated_localization=localization)
    space = BuildingSpace(id=1, name="Sala 101", associated_building=building)
    user = UserAccount(id=1, name="User", email="test@test.com", password="pwd", phone="123")

    existing_item = LostItem(
        id=1,
        name="Chave",
        description="Chave de carro",
        images=[],
        category=category,
        associated_user_account=user,
        approx_lost_building_space=space,
    )

    fake_lost_repo.get_lost_item_by_id.return_value = existing_item
    fake_cat_repo.get_category_by_id.return_value = category
    fake_space_repo.get_building_space_by_id.return_value = None

    dto = UpdateLostItemDTO(
        item_id=1,
        name="Chave",
        description="Chave de carro",
        image_urls=[],
        category_id=1,
        lost_building_space_id=999
    )

    use_case = UpdateLostItemUseCase(
        fake_lost_repo,
        fake_cat_repo,
        fake_space_repo
    )

    with pytest.raises(BuildingSpaceDoesntExistError, match="Espaço do prédio não encontrado"):
        use_case.execute(dto)
