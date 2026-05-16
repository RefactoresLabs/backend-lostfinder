from backend.app.presentation.controllers.list_buildings_controller import ListBuildingsController

from backend.app.application.dtos.list_buildings_dto import ListBuildingsDTO


from unittest.mock import Mock


def test_list_buildings_success():

    use_case = Mock()

    use_case.execute.return_value = [
        ListBuildingsDTO(1, "Prédio 1"),
        ListBuildingsDTO(2, "Prédio 2"),
    ]

    controller = ListBuildingsController(use_case)

    http_response = controller.handle()

    assert http_response.status_code == 200
    assert len(http_response.body) == 2
    assert http_response.body[1]["name"] == "Prédio 2"