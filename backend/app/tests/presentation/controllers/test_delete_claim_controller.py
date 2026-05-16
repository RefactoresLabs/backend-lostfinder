from backend.app.presentation.controllers.delete_claim_controller import DeleteClaimController
from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.domain.exceptions.claim_doesnt_exist_error import ClaimDoesntExistError

from unittest.mock import Mock


def test_delete_claim_controller_success():

    use_case = Mock()
    use_case.execute.return_value = True

    controller = DeleteClaimController(use_case)

    http_response = controller.handle(
        HttpRequest(params={"claim_id": 1})
    )

    assert http_response.status_code == 200
    assert http_response.body["message"] == "Negociação excluída com sucesso"


def test_delete_claim_controller_when_id_not_exists():

    use_case = Mock()
    use_case.execute.side_effect = ClaimDoesntExistError

    controller = DeleteClaimController(use_case)

    http_response = controller.handle(
        HttpRequest(params={"claim_id": 1})
    )

    assert http_response.status_code == 404
    assert http_response.body["code"] == "CLAIM_DOESNT_EXIST_ERROR"
