from backend.app.presentation.controllers.list_building_spaces_controller import ListBuildingSpacesController
from backend.app.presentation.schemas.http_request import HttpRequest

from backend.app.application.dtos.list_building_spaces_output_dto import ListBuildingSpacesOutputDTO


from unittest.mock import Mock


def test_list_building_spaces_success():

    use_case = Mock()

    use_case.execute.return_value = [
        ListBuildingSpacesOutputDTO(1, "Sala 1"),
        ListBuildingSpacesOutputDTO(2, "Sala 2"),
        ListBuildingSpacesOutputDTO(3, "Sala 3"),
    ]

    http_request = HttpRequest(
        params={"building_id": 1},
    )

    controller = ListBuildingSpacesController(use_case)

    http_response = controller.handle(http_request)

    assert http_response.status_code == 200
    assert http_response.body[0]["name"] == "Sala 1"
    assert http_response.body[1]["name"] == "Sala 2"
    assert http_response.body[2]["name"] == "Sala 3"