from unittest.mock import Mock

from backend.app.application.dtos.list_lost_items_summarized_dto import ListLostItemsSummarizedDTO
from backend.app.application.use_cases.list_lost_items_summarized_use_case import ListLostItemsSummarizedUseCase

def test_list_lost_items_use_case_success():

    query_service = Mock()

    query_service.get_all_lost_items_summarized.return_value = [
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

    use_case = ListLostItemsSummarizedUseCase(query_service)

    dtos: list[ListLostItemsSummarizedDTO] = use_case.execute()

    assert dtos[0].item_name == "Lápis"
    assert dtos[1].image_url is None