from backend.app.presentation.controllers.list_user_account_found_items_summarized_controller import ListUserAccountFoundItemsSummarizedController
from backend.app.presentation.schemas.http_request import HttpRequest

from backend.app.application.dtos.list_items_summarized_dto import ListItemsSummarizedDTO

from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError


from unittest.mock import Mock


def test_list_user_account_found_items_summarized_controller_success():

    use_case = Mock()

    use_case.execute.return_value = [
        ListItemsSummarizedDTO(
            item_id=1,
            item_name="Lápis",
            user_name="Link",
            category_name="Material",
            building_space_name="sala 1",
            image_url="./storage/image1.png"
        ),
        ListItemsSummarizedDTO(
            item_id=2,
            item_name="Caneta",
            user_name="Mario",
            category_name="Material",
            building_space_name="sala 2",
            image_url=None
        ),
    ]

    http_request = HttpRequest(params={"user_id": 1})

    controller = ListUserAccountFoundItemsSummarizedController(use_case)

    http_response = controller.handle(http_request)

    assert http_response.status_code == 200
    assert http_response.body[0]["user"]["name"] == "Link"

def test_list_user_account_found_items_summarized_controller_user_not_found():

    use_case = Mock()

    use_case.execute.side_effect = UserAccountDoesntExistError

    http_request = HttpRequest(params={"user_id": 1})

    controller = ListUserAccountFoundItemsSummarizedController(use_case)

    http_response = controller.handle(http_request)

    assert http_response.status_code == 404
    assert http_response.body["code"] == "USER_ACCOUNT_DOESNT_EXIST_ERROR"