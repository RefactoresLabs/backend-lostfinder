from unittest.mock import Mock
import pytest

from backend.app.application.use_cases.create_found_item_use_case import CreateFoundItemUseCase
from backend.app.application.dtos.create_found_item_dto import CreateFoundItemDTO
from backend.app.domain.entities.category import Category
from backend.app.domain.entities.building_space import BuildingSpace
from backend.app.domain.entities.building import Building
from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.value_objects.localization import Localization


def test_create_found_item_use_case_success():
    fake_found_repo = Mock()
    fake_cat_repo = Mock()
    fake_space_repo = Mock()
    fake_user_repo = Mock()

    category = Category(id=1, name="Documentos")
    localization = Localization(cep="123", neighborhood="Bairro", street="Rua")
    building = Building(id=1, name="Prédio B", associated_localization=localization)
    space_found = BuildingSpace(id=1, name="Pátio", associated_building=building)
    space_left = BuildingSpace(id=2, name="Recepção", associated_building=building)
    user = UserAccount(id=1, name="User", email="test@test.com", password="pwd", phone="123")

    fake_cat_repo.get_category_by_id.return_value = category
    fake_space_repo.get_building_space_by_id.side_effect = [space_found, space_left]
    fake_user_repo.get_user_account_by_id.return_value = user

    created_item = Mock()
    created_item.id = 20
    created_item.name = "Carteira"
    created_item.description = "Carteira preta"
    created_item.category.name = "Documentos"
    created_item.approx_found_building_space.name = "Pátio"
    created_item.approx_left_building_space.name = "Recepção"
    fake_found_repo.create_new_found_item.return_value = created_item

    dto = CreateFoundItemDTO(
        name="Carteira",
        description="Carteira preta",
        image_urls=[],
        category_id=1,
        user_id=1,
        found_building_space_id=1,
        left_building_space_id=2
    )

    use_case = CreateFoundItemUseCase(
        fake_found_repo,
        fake_cat_repo,
        fake_space_repo,
        fake_user_repo
    )

    result = use_case.execute(dto)

    assert result["id"] == 20
    assert result["found_building_space"] == "Pátio"
    assert result["left_building_space"] == "Recepção"
    fake_found_repo.create_new_found_item.assert_called_once()
