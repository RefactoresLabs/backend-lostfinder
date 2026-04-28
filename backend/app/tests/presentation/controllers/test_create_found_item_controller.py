from unittest.mock import Mock
from backend.app.presentation.controllers.create_found_item_controller import CreateFoundItemController
from backend.app.presentation.schemas.http_request import HttpRequest


def test_create_found_item_controller_success():
    use_case = Mock()
    use_case.execute.return_value = {"id": 1, "name": "Item"}
    
    controller = CreateFoundItemController(use_case)
    
    http_request = HttpRequest(
        body={
            "name": "Celular",
            "description": "Achado no refeitório",
            "category_id": 2,
            "found_building_space_id": 5,
            "left_building_space_id": 1
        },
        params={"user_id": 1}
    )
    
    response = controller.handle(http_request)
    
    assert response.status_code == 201
    assert response.body["message"] == "Item encontrado registrado com sucesso!"
    use_case.execute.assert_called_once()


def test_create_found_item_controller_not_found_error():
    use_case = Mock()
    use_case.execute.side_effect = ValueError("Categoria não encontrada")
    
    controller = CreateFoundItemController(use_case)
    
    http_request = HttpRequest(
        body={
            "name": "Celular",
            "description": "Achado no refeitório",
            "category_id": 999,
            "found_building_space_id": 5,
            "left_building_space_id": 1
        },
        params={"user_id": 1}
    )
    
    response = controller.handle(http_request)
    
    assert response.status_code == 404
    assert response.body["message"] == "Categoria não encontrada"
