from unittest.mock import Mock


from backend.app.application.use_cases.get_lost_item_details_use_case import GetLostItemDetailsUseCase
from backend.app.application.dtos.get_item_details_input_dto import GetItemDetailsInputDTO

from backend.app.domain.entities.lost_item import LostItem
from backend.app.domain.entities.category import Category
from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.entities.building import Building
from backend.app.domain.entities.building_space import BuildingSpace

from backend.app.domain.value_objects.image import Image
from backend.app.domain.value_objects.localization import Localization


def test_get_lost_item_success():

    repo = Mock()

    repo.get_lost_item_by_id.return_value = LostItem(
        id=1,
        name="Caneta",
        description="Caneta preta",
        images=[
            Image("/static/Image1.png")
        ],
        associated_user_account=UserAccount(
            id=1,
            name="Link",
            email="link@email.com",
            password="1234",
            phone="1234",
            score=20
        ),
        category=Category(
            id=1,
            name="Material escolar",
        ),
        approx_lost_building_space=BuildingSpace(
            id=1,
            name="sala 1",
            associated_building=Building(
                id=1,
                name="Predio 1",
                associated_localization=Localization(
                    cep="11111",
                    neighborhood="Bairro 1",
                    street="Rua 1",
                )
            )
        )
    )

    use_case = GetLostItemDetailsUseCase(repo)

    input_dto = GetItemDetailsInputDTO(
        id=1
    )

    output_dto = use_case.execute(input_dto)

    assert output_dto.item_name == "Caneta"
    assert output_dto.lost_localization_cep == "11111"

