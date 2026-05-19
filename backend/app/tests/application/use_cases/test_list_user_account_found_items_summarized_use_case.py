from unittest.mock import Mock

from backend.app.application.dtos.list_items_summarized_dto import ListItemsSummarizedDTO
from backend.app.application.dtos.list_user_account_items_summarized_input_dto import ListUserAccountItemsSummarizedInputDTO
from backend.app.application.use_cases.list_user_account_found_items_summarized_use_case import ListUserAccountFoundItemsSummarizedUseCase

from backend.app.domain.entities.user_account import UserAccount


def test_list_found_items_use_case_success():

    query_service = Mock()
    user_repository = Mock()

    user_repository.get_user_account_by_id.return_value = UserAccount(
        1,
        "link",
        "link@email.com",
        "1234",
        "12345678",
        10,
    )

    query_service.get_found_items_summarized_by_user_id.return_value = [
        {
            "item_id": 1,
            "item_name": "Lápis",
            "user_name": "Link",
            "category_name": "Material",
            "building_space_name": "sala 1",
            "image_url": "./storage/image1.png",
        },
        {
            "item_id": 2,
            "item_name": "Caneta",
            "user_name": "Mario",
            "category_name": "Material",
            "building_space_name": "sala 2",
            "image_url": None,
        },
    ]

    use_case = ListUserAccountFoundItemsSummarizedUseCase(query_service, user_repository)

    input_dto = ListUserAccountItemsSummarizedInputDTO(
        user_id=1
    )

    dtos: list[ListItemsSummarizedDTO] = use_case.execute(input_dto)

    assert dtos[0].item_name == "Lápis"
    assert dtos[1].image_url is None