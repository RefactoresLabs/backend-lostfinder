from backend.app.presentation.controllers.delete_lost_item_controller import DeleteLostItemController
from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError

from unittest.mock import Mock


def test_delete_lost_item_controller_success():
    use_case = Mock()
    use_case.execute.return_value = True

    controller = DeleteLostItemController(use_case)

    http_response = controller.handle(
        HttpRequest(params={"item_id": 1})
    )

    assert http_response.status_code == 200
    assert http_response.body["message"] == "Item perdido excluido com sucesso"


def test_delete_lost_item_controller_when_id_not_exists():
    use_case = Mock()
    use_case.execute.side_effect = ItemDoesntExistError("Item não encontrado")

    controller = DeleteLostItemController(use_case)

    http_response = controller.handle(
        HttpRequest(params={"item_id": 999})
    )

    assert http_response.status_code == 404
    assert http_response.body["code"] == "ITEM_DOESNT_EXIST_ERROR"
