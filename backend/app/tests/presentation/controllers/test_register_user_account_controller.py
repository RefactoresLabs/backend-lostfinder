from unittest.mock import Mock
import pytest

from backend.app.presentation.controllers.register_user_account_controller import RegisterUserAccountController
from backend.app.presentation.schemas.http_request import HttpRequest

from backend.app.domain.exceptions.email_exists_error import EmailExistsError


def test_controller_success():

    use_case = Mock()

    use_case.execute.return_value = None

    controller = RegisterUserAccountController(use_case)

    http_request = HttpRequest(
        body={
            "name": "link",
            "email": "link@email.com",
            "password": "123",
            "confirm_password": "123",
            "phone": "12345678"
        }
    )

    http_response = controller.handle(http_request)

    assert http_response.status_code == 201

def test_controller_raise_when_email_exists():

    use_case = Mock()

    use_case.execute.side_effect = EmailExistsError()

    controller = RegisterUserAccountController(use_case)

    http_request = HttpRequest(
        body={
            "name": "link",
            "email": "link@email.com",
            "password": "123",
            "confirm_password": "123",
            "phone": "12345678"
        }
    )

    http_response = controller.handle(http_request)

    assert http_response.status_code == 409

def test_controller_with_field_missing():

    use_case = Mock()

    use_case.execute.return_value = None

    controller = RegisterUserAccountController(use_case)

    http_request = HttpRequest(
        body={
            "email": "link@email.com",
            "password": "123",
            "confirm_password": "123",
            "phone": "12345678"
        }
    )

    http_response = controller.handle(http_request)

    excepted_body = {
        "message": "Campos obrigatórios não informados",
        "code": "REQUIRED_FIELD_MISSING_ERROR",
    }

    assert http_response.status_code == 400 and http_response.body == excepted_body

def test_controller_password_and_conf_password_dont_match():

    use_case = Mock()

    use_case.execute.return_value = None

    controller = RegisterUserAccountController(use_case)

    http_request = HttpRequest(
        body={
            "name": "link",
            "email": "link@email.com",
            "password": "123",
            "confirm_password": "1234",
            "phone": "12345678"
        }
    )

    http_response = controller.handle(http_request)

    excepted_body = {
        "message": "Senha e confirmar senha não correspondem",
        "code": "PASSWORD_MISMATCH_ERROR"
    }

    assert http_response.status_code == 400 and http_response.body == excepted_body