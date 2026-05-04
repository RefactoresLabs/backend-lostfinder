from unittest.mock import Mock
import pytest

from backend.app.presentation.controllers.login_controller import LoginController
from backend.app.presentation.schemas.http_request import HttpRequest

from backend.app.domain.exceptions.invalid_credentials_error import InvalidCredentialsError


def test_login_controller_success():

    use_case = Mock()
    use_case.execute.return_value = "fake_jwt_token"

    controller = LoginController(use_case)

    http_request = HttpRequest(
        body={
            "email": "link@email.com",
            "password": "123",
        }
    )

    http_response = controller.handle(http_request)

    assert http_response.status_code == 200
    assert http_response.body == {"token": "fake_jwt_token"}


def test_login_controller_raises_when_credentials_invalid():

    use_case = Mock()
    use_case.execute.side_effect = InvalidCredentialsError()

    controller = LoginController(use_case)

    http_request = HttpRequest(
        body={
            "email": "link@email.com",
            "password": "senha_errada",
        }
    )

    http_response = controller.handle(http_request)

    assert http_response.status_code == 401


def test_login_controller_with_field_missing():

    use_case = Mock()

    controller = LoginController(use_case)

    http_request = HttpRequest(
        body={
            "email": "link@email.com",
        }
    )

    http_response = controller.handle(http_request)

    expected_body = {"message": "Campos obrigatórios não informados", "code": "REQUIRED_FIELD_MISSING_ERROR"}

    assert http_response.status_code == 400 and http_response.body == expected_body


def test_login_controller_with_empty_field():

    use_case = Mock()

    controller = LoginController(use_case)

    http_request = HttpRequest(
        body={
            "email": "",
            "password": "123",
        }
    )

    http_response = controller.handle(http_request)

    assert http_response.status_code == 400
