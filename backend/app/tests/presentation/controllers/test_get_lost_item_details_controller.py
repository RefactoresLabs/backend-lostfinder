from backend.app.presentation.controllers.get_lost_item_details_controller import GetLostItemDetailsController

from backend.app.presentation.schemas.http_request import HttpRequest

from backend.app.application.dtos.get_lost_item_details_output_dto import GetLostItemDetailsOutputDTO

from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError


from unittest.mock import Mock


def test_get_lost_item_details_controller_success():

    use_case = Mock()

    use_case.execute.return_value = GetLostItemDetailsOutputDTO(
        item_id=1,
        item_name="Caneta",
        item_description="Caneta preta",
        item_category_name="Material escolar",
        item_image_urls=[
            "/static/image1.png"
        ],
        user_name="Link",
        user_email="link@email.com",
        user_phone="1234",
        lost_building_space_name="sala 1",
        lost_building_name="predio 1",
        lost_localization_cep="11111",
        lost_localization_neighborhood="bairro 1",
        lost_localization_street="rua 1",
    )

    controller = GetLostItemDetailsController(use_case)

    http_response = controller.handle(
        HttpRequest(params={"item_id": 1})
    )

    assert http_response.status_code == 200
    assert http_response.body["name"] == "Caneta"
    assert http_response.body["lost_building_space"]["building"]["localization"]["cep"] == "11111"

def test_get_lost_item_details_controller_when_id_not_exists():

    use_case = Mock()

    use_case.execute.side_effect = ItemDoesntExistError

    controller = GetLostItemDetailsController(use_case)

    http_response = controller.handle(
        HttpRequest({"item_id": 1})
    )

    assert http_response.status_code == 404