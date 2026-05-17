from backend.app.presentation.controllers.finish_claim_controller import FinishClaimController
from backend.app.presentation.schemas.http_request import HttpRequest


from unittest.mock import Mock


def test_finish_claim_controller_success():

    use_case = Mock()

    controller = FinishClaimController(use_case)

    http_request = HttpRequest(
        params={
            "claim_id": 1,
            "user_id": 1,
        },
        body={
            "retrieval_code": "12A34B56C7",
        }
    )

    http_response = controller.handle(http_request)

    assert use_case.execute.assert_called_once