from unittest.mock import Mock
from backend.app.presentation.controllers.create_lost_item_controller import CreateLostItemController
from backend.app.presentation.schemas.http_request import HttpRequest


def test_create_lost_item_controller_success():
    use_case = Mock()
    use_case.execute.return_value = {"id": 1, "name": "Item"}
    
    controller = CreateLostItemController(use_case)
    
    http_request = HttpRequest(
        body={
            "name": "Chave",
            "description": "Perdida no bloco A",
            "category_id": 1,
            "lost_building_space_id": 10,
            "image_urls": ["http://image.com"]
        },
        params={"user_id": 1}
    )
    
    response = controller.handle(http_request)
    
    assert response.status_code == 201
    assert response.body["message"] == "Item perdido registrado com sucesso!"
    use_case.execute.assert_called_once()


def test_create_lost_item_controller_missing_fields():
    use_case = Mock()
    controller = CreateLostItemController(use_case)
    
    http_request = HttpRequest(
        body={
            "name": "Chave"
            # faltando outros campos
        },
        params={"user_id": 1}
    )
    
    response = controller.handle(http_request)
    
    assert response.status_code == 400
    assert response.body["message"] == "Campos obrigatórios não informados"
