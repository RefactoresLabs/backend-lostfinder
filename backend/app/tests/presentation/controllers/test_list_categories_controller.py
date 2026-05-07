from backend.app.presentation.controllers.list_categories_controller import ListCategoriesController

from backend.app.application.dtos.list_categories_dto import ListCategoriesDTO

from unittest.mock import Mock


def test_list_categories_success():

    use_case = Mock()

    use_case.execute.return_value = [
        ListCategoriesDTO(1, "Material Escolar"),
        ListCategoriesDTO(2, "Documento"),
    ]

    controller = ListCategoriesController(use_case)

    http_response = controller.handle()

    assert http_response.status_code == 200
    assert len(http_response.body) == 2
    assert http_response.body[1]["name"] == "Documento"