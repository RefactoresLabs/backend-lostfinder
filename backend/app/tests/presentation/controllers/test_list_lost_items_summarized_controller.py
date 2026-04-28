from unittest.mock import Mock


from backend.app.presentation.controllers.list_lost_items_summarized_controller import ListLostItemsSummarizedController
from backend.app.presentation.schemas.http_request import HttpRequest

from backend.app.application.dtos.list_lost_items_summarized_dto import ListLostItemsSummarizedDTO


def test_list_lost_items_controller_no_limit():

    use_case = Mock()

    use_case.execute.return_value = [
        ListLostItemsSummarizedDTO(
            item_id=1,
            item_name="Lápis",
            user_name="Link",
            category_name="Material",
            building_space_name="sala 1",
            image_url="./storage/image1.png"
        ),
        ListLostItemsSummarizedDTO(
            item_id=2,
            item_name="Caneta",
            user_name="Mario",
            category_name="Material",
            building_space_name="sala 2",
            image_url=None
        ),
    ]

    controller = ListLostItemsSummarizedController(use_case)

    http_request = HttpRequest(
        params={}
    )

    http_response = controller.handle(http_request)

    assert http_response.status_code == 200
    assert len(http_response.body) == 2
    assert http_response.body[1]["name"] == "Caneta"

def test_list_lost_items_controller_limit():

    use_case = Mock()

    use_case.execute.return_value = [
        ListLostItemsSummarizedDTO(
            item_id=1,
            item_name="Lápis",
            user_name="Link",
            category_name="Material",
            building_space_name="sala 1",
            image_url="./storage/image1.png"
        ),
        ListLostItemsSummarizedDTO(
            item_id=2,
            item_name="Caneta",
            user_name="Mario",
            category_name="Material",
            building_space_name="sala 2",
            image_url=None
        ),
    ]

    controller = ListLostItemsSummarizedController(use_case)

    http_request = HttpRequest(
        params={"limit": 1}
    )

    http_response = controller.handle(http_request)

    assert http_response.status_code == 200
    assert len(http_response.body) == 1
    assert http_response.body[0]["name"] == "Lápis"

def test_list_lost_items_controller_negative_limit():

    use_case = Mock()

    use_case.execute.return_value = [
        ListLostItemsSummarizedDTO(
            item_id=1,
            item_name="Lápis",
            user_name="Link",
            category_name="Material",
            building_space_name="sala 1",
            image_url="./storage/image1.png"
        ),
        ListLostItemsSummarizedDTO(
            item_id=2,
            item_name="Caneta",
            user_name="Mario",
            category_name="Material",
            building_space_name="sala 2",
            image_url=None
        ),
    ]

    controller = ListLostItemsSummarizedController(use_case)

    http_request = HttpRequest(
        params={"limit": -1}
    )

    http_response = controller.handle(http_request)

    assert http_response.status_code == 400
    assert http_response.body["message"] == "O campo 'limit' não pode ser negativo!"