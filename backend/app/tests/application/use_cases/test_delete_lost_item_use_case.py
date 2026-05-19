from unittest.mock import Mock
import pytest

from backend.app.application.use_cases.delete_lost_item_use_case import DeleteLostItemUseCase
from backend.app.application.dtos.delete_lost_item_dto import DeleteLostItemDTO
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError


def test_delete_lost_item_use_case_success():
    fake_repo = Mock()
    fake_repo.delete_lost_item.return_value = True

    dto = DeleteLostItemDTO(item_id=1)

    use_case = DeleteLostItemUseCase(fake_repo)

    use_case.execute(dto)

    fake_repo.delete_lost_item.assert_called_once_with(1)


def test_delete_lost_item_use_case_item_not_found():
    fake_repo = Mock()
    fake_repo.delete_lost_item.return_value = False

    dto = DeleteLostItemDTO(item_id=999)

    use_case = DeleteLostItemUseCase(fake_repo)

    with pytest.raises(ItemDoesntExistError, match="Item não encontrado"):
        use_case.execute(dto)
