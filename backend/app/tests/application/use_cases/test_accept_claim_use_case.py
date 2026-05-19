from backend.app.application.use_cases.accept_claim_use_case import AcceptClaimUseCase
from backend.app.application.dtos.accept_claim_input_dto import AcceptClaimInputDTO

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


def test_accept_claim_use_case_success():

    claim_repository = Mock()

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

    claim = Claim(
        id=1,
        created_at=datetime.now(),
        claimant_user_account=claimant_user_account,
        associated_found_item=found_item,
        status=ClaimStatus("Pendente"),
        retrieval_code=None,
    )

    claim_repository.get_claim_by_id.return_value = claim
    claim_repository.check_retrieval_code_exists.return_value = False

    use_case = AcceptClaimUseCase(claim_repository)

    input_dto = AcceptClaimInputDTO(
        1, 1,
    )

    output_dto = use_case.execute(input_dto)

    assert output_dto.retrieval_code is not None