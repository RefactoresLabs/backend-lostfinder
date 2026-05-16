from unittest.mock import Mock
import pytest

from backend.app.application.use_cases.login_use_case import LoginUseCase
from backend.app.application.dtos.login_dto import LoginDTO

from backend.app.domain.exceptions.invalid_credentials_error import InvalidCredentialsError
from backend.app.domain.entities.user_account import UserAccount


def test_login_success():

    fake_repository = Mock()
    fake_hasher = Mock()
    fake_token_generator = Mock()

    fake_repository.get_user_account_by_email.return_value = UserAccount(
        name="link",
        email="link@email.com",
        password="hashed_password",
        phone="12345678",
        id=1,
    )

    fake_hasher.verify.return_value = True
    fake_token_generator.generate.return_value = "fake_jwt_token"

    dto = LoginDTO(email="link@email.com", password="123")

    use_case = LoginUseCase(fake_repository, fake_hasher, fake_token_generator)

    token = use_case.execute(dto)

    assert token == "fake_jwt_token"
    fake_token_generator.generate.assert_called_once()


def test_login_raises_when_email_not_found():

    fake_repository = Mock()
    fake_hasher = Mock()
    fake_token_generator = Mock()

    fake_repository.get_user_account_by_email.return_value = None

    dto = LoginDTO(email="naoexiste@email.com", password="123")

    use_case = LoginUseCase(fake_repository, fake_hasher, fake_token_generator)

    with pytest.raises(InvalidCredentialsError):

        use_case.execute(dto)


def test_login_raises_when_password_is_wrong():

    fake_repository = Mock()
    fake_hasher = Mock()
    fake_token_generator = Mock()

    fake_repository.get_user_account_by_email.return_value = UserAccount(
        name="link",
        email="link@email.com",
        password="hashed_password",
        phone="12345678",
        id=1,
    )

    fake_hasher.verify.return_value = False

    dto = LoginDTO(email="link@email.com", password="senha_errada")

    use_case = LoginUseCase(fake_repository, fake_hasher, fake_token_generator)

    with pytest.raises(InvalidCredentialsError):

        use_case.execute(dto)
