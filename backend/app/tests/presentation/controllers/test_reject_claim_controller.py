from backend.app.presentation.controllers.reject_claim_controller import RejectClaimController
from backend.app.presentation.schemas.http_request import HttpRequest


from unittest.mock import Mock


def test_accept_claim_controller_success():

    use_case = Mock()

    controller = RejectClaimController(use_case)

    http_request = HttpRequest(
        params={
            "claim_id": 1,
            "user_id": 1,
        }
    )

    http_response = controller.handle(http_request)

    assert use_case.execute.assert_called_once