from unittest.mock import Mock
import pytest

from backend.app.application.use_cases.create_lost_item_use_case import CreateLostItemUseCase
from backend.app.application.dtos.create_lost_item_dto import CreateLostItemDTO
from backend.app.domain.entities.lost_item import LostItem
from backend.app.domain.entities.category import Category
from backend.app.domain.entities.building_space import BuildingSpace
from backend.app.domain.entities.building import Building
from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.value_objects.localization import Localization


def test_create_lost_item_use_case_success():
    # Mocks
    fake_lost_repo = Mock()
    fake_cat_repo = Mock()
    fake_space_repo = Mock()
    fake_user_repo = Mock()

    # Data
    category = Category(id=1, name="Eletrônicos")
    localization = Localization(cep="123", neighborhood="Bairro", street="Rua")
    building = Building(id=1, name="Prédio A", associated_localization=localization)
    space = BuildingSpace(id=1, name="Sala 101", associated_building=building)
    user = UserAccount(id=1, name="User", email="test@test.com", password="pwd", phone="123")

    fake_cat_repo.get_category_by_id.return_value = category
    fake_space_repo.get_building_space_by_id.return_value = space
    fake_user_repo.get_user_account_by_id.return_value = user

    # Simular o retorno do repositório ao criar (com ID definido)
    created_item = Mock()
    created_item.id = 10
    created_item.name = "Chave"
    created_item.description = "Chave de carro"
    created_item.category.name = "Eletrônicos"
    created_item.approx_lost_building_space.name = "Sala 101"
    fake_lost_repo.create_new_lost_item.return_value = created_item

    dto = CreateLostItemDTO(
        name="Chave",
        description="Chave de carro",
        image_urls=["url1"],
        category_id=1,
        user_id=1,
        lost_building_space_id=1
    )

    use_case = CreateLostItemUseCase(
        fake_lost_repo,
        fake_cat_repo,
        fake_space_repo,
        fake_user_repo
    )

    result = use_case.execute(dto)

    assert result["id"] == 10
    assert result["name"] == "Chave"
    fake_lost_repo.create_new_lost_item.assert_called_once()


def test_create_lost_item_use_case_category_not_found():
    fake_lost_repo = Mock()
    fake_cat_repo = Mock()
    fake_space_repo = Mock()
    fake_user_repo = Mock()

    fake_cat_repo.get_category_by_id.return_value = None

    dto = CreateLostItemDTO(
        name="Chave",
        description="Chave de carro",
        image_urls=[],
        category_id=1,
        user_id=1,
        lost_building_space_id=1
    )

    use_case = CreateLostItemUseCase(
        fake_lost_repo,
        fake_cat_repo,
        fake_space_repo,
        fake_user_repo
    )

    with pytest.raises(ValueError, match="Categoria não encontrada"):
        use_case.execute(dto)
