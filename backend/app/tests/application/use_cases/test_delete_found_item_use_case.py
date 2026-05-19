from unittest.mock import Mock
import pytest

from backend.app.application.use_cases.delete_found_item_use_case import DeleteFoundItemUseCase
from backend.app.application.dtos.delete_found_item_dto import DeleteFoundItemDTO
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError


def test_delete_found_item_use_case_success():
    fake_repo = Mock()
    fake_repo.delete_found_item.return_value = True

    dto = DeleteFoundItemDTO(item_id=1)

    use_case = DeleteFoundItemUseCase(fake_repo)

    use_case.execute(dto)

    fake_repo.delete_found_item.assert_called_once_with(1)


def test_delete_found_item_use_case_item_not_found():
    fake_repo = Mock()
    fake_repo.delete_found_item.return_value = False

    dto = DeleteFoundItemDTO(item_id=999)

    use_case = DeleteFoundItemUseCase(fake_repo)

    with pytest.raises(ItemDoesntExistError, match="Item não encontrado"):
        use_case.execute(dto)
