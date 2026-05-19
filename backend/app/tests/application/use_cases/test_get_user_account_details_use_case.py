from backend.app.application.use_cases.get_user_account_details_use_case import GetUserAccountDetailsUseCase
from backend.app.application.dtos.get_user_account_details_input_dto import GetUserAccountDetailsInputDTO

from backend.app.domain.entities.user_account import UserAccount


from unittest.mock import Mock


def test_get_user_account_details_use_case_success():

    repository = Mock()

    repository.get_user_account_by_id.return_value = UserAccount(
        id=1,
        name="Link",
        email="link@gmail.com",
        password="1234",
        phone="12345678",
        score=10,
    )

    input_dto = GetUserAccountDetailsInputDTO(1)

    use_case = GetUserAccountDetailsUseCase(repository)

    output_dto = use_case.execute(input_dto)

    assert output_dto.name == "Link"
    assert output_dto.score == 10