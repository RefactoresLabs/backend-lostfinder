from backend.app.application.use_cases.finish_claim_use_case import FinishClaimUseCase
from backend.app.application.dtos.finish_claim_dto import FinishClaimDTO

from backend.app.domain.entities.found_item import FoundItem
from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.entities.category import Category
from backend.app.domain.entities.building_space import BuildingSpace
from backend.app.domain.entities.building import Building
from backend.app.domain.entities.claim import Claim
from backend.app.domain.value_objects.localization import Localization
from backend.app.domain.value_objects.claim_status import ClaimStatus


from unittest.mock import Mock
from datetime import datetime


def test_finish_claim_use_case_success():

    repo = Mock()

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
    )

    claim = Claim(
        id=1,
        created_at=datetime.now(),
        claimant_user_account=claimant_user_account,
        associated_found_item=found_item,
        status=ClaimStatus("Aceita"),
        retrieval_code="12A34B56C7",
    )

    repo.get_claim_by_id.return_value = claim

    use_case = FinishClaimUseCase(repo)

    dto = FinishClaimDTO(1, 2, "12A34B56C7")

    use_case.execute(dto)

    assert repo.update_claim.assert_called_once