from unittest.mock import Mock
import pytest

from backend.app.application.use_cases.update_found_item_use_case import UpdateFoundItemUseCase
from backend.app.application.dtos.update_found_item_dto import UpdateFoundItemDTO
from backend.app.domain.entities.found_item import FoundItem
from backend.app.domain.entities.category import Category
from backend.app.domain.entities.building_space import BuildingSpace
from backend.app.domain.entities.building import Building
from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.value_objects.localization import Localization
from backend.app.domain.exceptions.category_doesnt_exist_error import CategoryDoesntExistError
from backend.app.domain.exceptions.building_space_doesnt_exist_error import BuildingSpaceDoesntExistError
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError


def test_update_found_item_use_case_success():
    fake_found_repo = Mock()
    fake_cat_repo = Mock()
    fake_space_repo = Mock()

    category = Category(id=1, name="Eletrônicos")
    localization = Localization(cep="123", neighborhood="Bairro", street="Rua")
    building = Building(id=1, name="Prédio A", associated_localization=localization)
    found_space = BuildingSpace(id=1, name="Sala 101", associated_building=building)
    left_space = BuildingSpace(id=2, name="Sala 102", associated_building=building)
    user = UserAccount(id=1, name="User", email="test@test.com", password="pwd", phone="123", score=20)

    existing_item = FoundItem(
        id=1,
        name="Chave antiga",
        description="Descrição antiga",
        images=[],
        category=category,
        associated_user_account=user,
        found_building_space=found_space,
        left_building_space=left_space,
    )

    fake_found_repo.get_found_item_by_id.return_value = existing_item
    fake_cat_repo.get_category_by_id.return_value = category
    fake_space_repo.get_building_space_by_id.side_effect = lambda id: found_space if id == 1 else left_space

    dto = UpdateFoundItemDTO(
        item_id=1,
        name="Chave nova",
        description="Descrição nova",
        image_urls=["url1"],
        category_id=1,
        found_building_space_id=1,
        left_building_space_id=2
    )

    use_case = UpdateFoundItemUseCase(
        fake_found_repo,
        fake_cat_repo,
        fake_space_repo
    )

    use_case.execute(dto)

    fake_found_repo.update_found_item.assert_called_once()


def test_update_found_item_use_case_item_not_found():
    fake_found_repo = Mock()
    fake_cat_repo = Mock()
    fake_space_repo = Mock()

    fake_found_repo.get_found_item_by_id.return_value = None

    dto = UpdateFoundItemDTO(
        item_id=1,
        name="Chave",
        description="Chave de carro",
        image_urls=[],
        category_id=1,
        found_building_space_id=1,
        left_building_space_id=2
    )

    use_case = UpdateFoundItemUseCase(
        fake_found_repo,
        fake_cat_repo,
        fake_space_repo
    )

    with pytest.raises(ItemDoesntExistError, match="Item não encontrado"):
        use_case.execute(dto)


def test_update_found_item_use_case_category_not_found():
    fake_found_repo = Mock()
    fake_cat_repo = Mock()
    fake_space_repo = Mock()

    category = Category(id=1, name="Eletrônicos")
    localization = Localization(cep="123", neighborhood="Bairro", street="Rua")
    building = Building(id=1, name="Prédio A", associated_localization=localization)
    found_space = BuildingSpace(id=1, name="Sala 101", associated_building=building)
    left_space = BuildingSpace(id=2, name="Sala 102", associated_building=building)
    user = UserAccount(id=1, name="User", email="test@test.com", password="pwd", phone="123", score=20)

    existing_item = FoundItem(
        id=1,
        name="Chave",
        description="Chave de carro",
        images=[],
        category=category,
        associated_user_account=user,
        found_building_space=found_space,
        left_building_space=left_space,
    )

    fake_found_repo.get_found_item_by_id.return_value = existing_item
    fake_cat_repo.get_category_by_id.return_value = None

    dto = UpdateFoundItemDTO(
        item_id=1,
        name="Chave",
        description="Chave de carro",
        image_urls=[],
        category_id=999,
        found_building_space_id=1,
        left_building_space_id=2
    )

    use_case = UpdateFoundItemUseCase(
        fake_found_repo,
        fake_cat_repo,
        fake_space_repo
    )

    with pytest.raises(CategoryDoesntExistError, match="Categoria não encontrada"):
        use_case.execute(dto)


def test_update_found_item_use_case_found_building_space_not_found():
    fake_found_repo = Mock()
    fake_cat_repo = Mock()
    fake_space_repo = Mock()

    category = Category(id=1, name="Eletrônicos")
    localization = Localization(cep="123", neighborhood="Bairro", street="Rua")
    building = Building(id=1, name="Prédio A", associated_localization=localization)
    found_space = BuildingSpace(id=1, name="Sala 101", associated_building=building)
    left_space = BuildingSpace(id=2, name="Sala 102", associated_building=building)
    user = UserAccount(id=1, name="User", email="test@test.com", password="pwd", phone="123", score=20)

    existing_item = FoundItem(
        id=1,
        name="Chave",
        description="Chave de carro",
        images=[],
        category=category,
        associated_user_account=user,
        found_building_space=found_space,
        left_building_space=left_space,
    )

    fake_found_repo.get_found_item_by_id.return_value = existing_item
    fake_cat_repo.get_category_by_id.return_value = category
    fake_space_repo.get_building_space_by_id.return_value = None

    dto = UpdateFoundItemDTO(
        item_id=1,
        name="Chave",
        description="Chave de carro",
        image_urls=[],
        category_id=1,
        found_building_space_id=999,
        left_building_space_id=2
    )

    use_case = UpdateFoundItemUseCase(
        fake_found_repo,
        fake_cat_repo,
        fake_space_repo
    )

    with pytest.raises(BuildingSpaceDoesntExistError, match="Espaço do prédio não encontrado"):
        use_case.execute(dto)


def test_update_found_item_use_case_left_building_space_not_found():
    fake_found_repo = Mock()
    fake_cat_repo = Mock()
    fake_space_repo = Mock()

    category = Category(id=1, name="Eletrônicos")
    localization = Localization(cep="123", neighborhood="Bairro", street="Rua")
    building = Building(id=1, name="Prédio A", associated_localization=localization)
    found_space = BuildingSpace(id=1, name="Sala 101", associated_building=building)
    left_space = BuildingSpace(id=2, name="Sala 102", associated_building=building)
    user = UserAccount(id=1, name="User", email="test@test.com", password="pwd", phone="123", score=20)

    existing_item = FoundItem(
        id=1,
        name="Chave",
        description="Chave de carro",
        images=[],
        category=category,
        associated_user_account=user,
        found_building_space=found_space,
        left_building_space=left_space,
    )

    fake_found_repo.get_found_item_by_id.return_value = existing_item
    fake_cat_repo.get_category_by_id.return_value = category
    fake_space_repo.get_building_space_by_id.side_effect = lambda id: found_space if id == 1 else None

    dto = UpdateFoundItemDTO(
        item_id=1,
        name="Chave",
        description="Chave de carro",
        image_urls=[],
        category_id=1,
        found_building_space_id=1,
        left_building_space_id=999
    )

    use_case = UpdateFoundItemUseCase(
        fake_found_repo,
        fake_cat_repo,
        fake_space_repo
    )

    with pytest.raises(BuildingSpaceDoesntExistError, match="Espaço do prédio não encontrado"):
        use_case.execute(dto)
