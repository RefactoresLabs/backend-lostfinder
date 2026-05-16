from unittest.mock import Mock
import pytest

from backend.app.application.use_cases.register_user_account_use_case import RegisterUserAccountUseCase
from backend.app.application.dtos.register_user_account_dto import RegisterUserAccountDTO

from backend.app.domain.exceptions.email_exists_error import EmailExistsError

def test_use_case_success():

    fake_repository = Mock()
    fake_user_account_validation_service = Mock()
    fake_hasher = Mock()

    fake_user_account_validation_service.validate_email_exists.return_value = None

    fake_hasher.hash.return_value = "hashed_password"

    dto = RegisterUserAccountDTO(
        "link",
        "link@email.com",
        "hashed_password",
        "1234"
    )

    use_case = RegisterUserAccountUseCase(
        fake_repository,
        fake_hasher,
        fake_user_account_validation_service,
    )

    use_case.execute(dto)

    fake_repository.create_new_user_account.assert_called_once()


def test_use_case_raises_when_email_exists():

    fake_repository = Mock()
    fake_user_account_validation_service = Mock()
    fake_hasher = Mock()

    fake_user_account_validation_service.validate_email_exists.side_effect = EmailExistsError()

    fake_hasher.hash.return_value = "hashed_password"

    dto = RegisterUserAccountDTO(
        "link",
        "link@email.com",
        "hashed_password",
        "1234"
    )

    use_case = RegisterUserAccountUseCase(
        fake_repository,
        fake_hasher,
        fake_user_account_validation_service,
    )

    with pytest.raises(EmailExistsError):

        use_case.execute(dto)





