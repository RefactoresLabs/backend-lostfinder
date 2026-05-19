from backend.app.application.dtos.get_user_account_details_output_dto import GetUserAccountDetailsOutputDTO

from backend.app.presentation.controllers.get_user_account_details_controller import GetUserAccountDetailsController
from backend.app.presentation.schemas.http_request import HttpRequest


from unittest.mock import Mock


def test_get_user_account_details_controller_success():

    use_case = Mock()

    use_case.execute.return_value = GetUserAccountDetailsOutputDTO(
        1,
        "Link",
        "link@gmail.com",
        "12345678",
        10,
    )

    controller = GetUserAccountDetailsController(use_case)

    http_request = HttpRequest(params={"user_id": 1})

    http_response = controller.handle(http_request)

    assert http_response.status_code == 200
    assert http_response.body["name"] == "Link"