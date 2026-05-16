from backend.app.presentation.controllers.create_claim_controller import CreateClaimController
from backend.app.presentation.schemas.http_request import HttpRequest


from unittest.mock import Mock


def test_create_claim_controller_success():

    use_case = Mock()

    controller = CreateClaimController(use_case)

    http_request = HttpRequest(
        {"user_id": 1},
        {"found_item_id": 1}
    )

    http_response = controller.handle(http_request)

    assert use_case.execute.assert_called_once