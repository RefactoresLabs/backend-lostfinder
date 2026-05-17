from backend.app.presentation.controllers.update_found_item_controller import UpdateFoundItemController
from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError
from backend.app.domain.exceptions.category_doesnt_exist_error import CategoryDoesntExistError
from backend.app.domain.exceptions.building_space_doesnt_exist_error import BuildingSpaceDoesntExistError

from unittest.mock import Mock


def test_update_found_item_controller_success():
    use_case = Mock()
    use_case.execute.return_value = None

    controller = UpdateFoundItemController(use_case)

    http_response = controller.handle(
        HttpRequest(
            params={"item_id": 1},
            body={
                "name": "Chave",
                "description": "Chave de carro",
                "category_id": 1,
                "found_building_space_id": 1,
                "left_building_space_id": 2
            }
        )
    )

    assert http_response.status_code == 200
    assert http_response.body["message"] == "Item encontrado atualizado com sucesso"


def test_update_found_item_controller_missing_required_fields():
    use_case = Mock()

    controller = UpdateFoundItemController(use_case)

    http_response = controller.handle(
        HttpRequest(
            params={"item_id": 1},
            body={"name": "Chave"}
        )
    )

    assert http_response.status_code == 400
    assert http_response.body["code"] == "REQUIRED_FIELD_MISSING_ERROR"


def test_update_found_item_controller_empty_field():
    use_case = Mock()

    controller = UpdateFoundItemController(use_case)

    http_response = controller.handle(
        HttpRequest(
            params={"item_id": 1},
            body={
                "name": "",
                "description": "Chave de carro",
                "category_id": 1,
                "found_building_space_id": 1,
                "left_building_space_id": 2
            }
        )
    )

    assert http_response.status_code == 400
    assert http_response.body["code"] == "EMPTY_FIELD_ERROR"


def test_update_found_item_controller_item_not_found():
    use_case = Mock()
    use_case.execute.side_effect = ItemDoesntExistError("Item não encontrado")

    controller = UpdateFoundItemController(use_case)

    http_response = controller.handle(
        HttpRequest(
            params={"item_id": 999},
            body={
                "name": "Chave",
                "description": "Chave de carro",
                "category_id": 1,
                "found_building_space_id": 1,
                "left_building_space_id": 2
            }
        )
    )

    assert http_response.status_code == 404
    assert http_response.body["code"] == "ITEM_DOESNT_EXIST_ERROR"


def test_update_found_item_controller_category_not_found():
    use_case = Mock()
    use_case.execute.side_effect = CategoryDoesntExistError("Categoria não encontrada")

    controller = UpdateFoundItemController(use_case)

    http_response = controller.handle(
        HttpRequest(
            params={"item_id": 1},
            body={
                "name": "Chave",
                "description": "Chave de carro",
                "category_id": 999,
                "found_building_space_id": 1,
                "left_building_space_id": 2
            }
        )
    )

    assert http_response.status_code == 400
    assert http_response.body["code"] == "CATEGORY_DOESNT_EXIST_ERROR"


def test_update_found_item_controller_building_space_not_found():
    use_case = Mock()
    use_case.execute.side_effect = BuildingSpaceDoesntExistError("Espaço do prédio não encontrado")

    controller = UpdateFoundItemController(use_case)

    http_response = controller.handle(
        HttpRequest(
            params={"item_id": 1},
            body={
                "name": "Chave",
                "description": "Chave de carro",
                "category_id": 1,
                "found_building_space_id": 999,
                "left_building_space_id": 2
            }
        )
    )

    assert http_response.status_code == 400
    assert http_response.body["code"] == "BUILDING_SPACE_DOESNT_EXIST_ERROR"
