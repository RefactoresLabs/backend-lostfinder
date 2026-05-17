from backend.app.application.use_cases.create_claim_use_case import CreateClaimUseCase
from backend.app.application.dtos.create_claim_dto import CreateClaimDTO

from backend.app.domain.entities.found_item import FoundItem
from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.entities.category import Category
from backend.app.domain.entities.building_space import BuildingSpace
from backend.app.domain.entities.building import Building
from backend.app.domain.value_objects.localization import Localization

from unittest.mock import Mock


def test_create_claim_use_case_success():

    user_account_repo = Mock()
    found_item_repo = Mock()
    claim_repo = Mock()

    localization = Localization(
        cep="1111",
        neighborhood="Bairro 1",
        street="Rua 1",
    )

    building = Building(
        id=1,
        name="Prédio 1",
        associated_localization=localization,
    )

    building_space = BuildingSpace(
        id=1,
        name="Sala 1",
        associated_building=building
    )

    found_item_user_account = UserAccount(
        id=1,
        name="Link",
        email="link@email.com",
        password="1234",
        phone="12345678",
        score=20,
    )

    category = Category(
        id=1,
        name="Acessório Pessoal"
    )

    found_item = FoundItem(
        id=2,
        name="Fone",
        description="Fone JBL branco",
        images=[],
        category=category,
        associated_user_account=found_item_user_account,
        approx_found_building_space=building_space,
        approx_left_building_space=building_space,
    )

    claimant_user_account = UserAccount(
        id=2,
        name="Mario",
        email="mario@email.com",
        password="1234",
        phone="12345678",
        score=30,
    )

    user_account_repo.get_user_account_by_id.return_value = claimant_user_account

    found_item_repo.get_found_item_by_id.return_value = found_item

    use_case = CreateClaimUseCase(
        claim_repo,
        found_item_repo,
        user_account_repo
    )

    dto = CreateClaimDTO(2, 2)

    use_case.execute(dto)

    assert claim_repo.create_new_claim.assert_called_once