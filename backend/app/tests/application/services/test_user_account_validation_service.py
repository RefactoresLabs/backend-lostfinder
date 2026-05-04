from unittest.mock import Mock
import pytest

from backend.app.application.services.user_account_validation_service import UserAccountValidationService

from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.exceptions.email_exists_error import EmailExistsError

def test_service_success():

    fake_repository = Mock()

    fake_repository.get_user_account_by_email.return_value = None

    service = UserAccountValidationService(fake_repository)

    email = "link@email.com"

    returned_value = service.validate_email_exists(email)

    assert returned_value is None

def test_service_raises_when_email_exists():

    fake_repository = Mock()

    fake_repository.get_user_account_by_email.return_value = UserAccount(
        "link",
        "link@email.com",
        "hashed_password",
        "1234",
    )

    service = UserAccountValidationService(fake_repository)

    email = "link@email.com"

    with pytest.raises(EmailExistsError):
        
        service.validate_email_exists(email)