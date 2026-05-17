from backend.app.presentation.controllers.accept_claim_controller import AcceptClaimController
from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse

from backend.app.application.dtos.accept_claim_output_dto import AcceptClaimOutputDTO


from unittest.mock import Mock


def test_accept_claim_controller_success():

    use_case = Mock()

    use_case.execute.return_value = AcceptClaimOutputDTO(
        retrieval_code="12A34B56C7",
    )

    controller = AcceptClaimController(use_case)

    http_request = HttpRequest(
        params={
            "claim_id": 1,
            "user_id": 1,
        }
    )

    http_response = controller.handle(http_request)

    assert http_response.status_code == 200
    assert len(http_response.body["retrieval_code"]) == 10