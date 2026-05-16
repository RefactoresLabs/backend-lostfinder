import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from backend.app.infrastructure.persistence.models.base import Base
from backend.app.domain.entities.user_account import UserAccount
from backend.app.infrastructure.persistence.models.user_account_model import UserAccountModel
from backend.app.infrastructure.persistence.repositories.user_account_repository import UserAccountRepository

@pytest.fixture
def session():

    """Simula uma sessão a um banco em memória
    """

    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()

def test_create_user_account(session):

    repo = UserAccountRepository(session)

    user = UserAccount(
        id=None,
        name="teste",
        email="teste@email.com",
        password="123",
        phone="551212345678"
    )

    repo.create_new_user_account(user)

    session.commit()

    result = (
        session.query(UserAccountModel)
        .filter_by(email="teste@email.com")
        .first()
    )

    assert result is not None
    assert result.name == "teste"
    assert result.email == "teste@email.com"

def test_create_user_account_with_existing_email(session):

    repo = UserAccountRepository(session)

    user = UserAccount(
        id=None,
        name="teste",
        email="teste@email.com",
        password="123",
        phone="551212345678"
    )

    user2 = UserAccount(
        id=None,
        name="teste2",
        email="teste@email.com",
        password="1234",
        phone="551212345679"
    )

    with pytest.raises(IntegrityError):

        repo.create_new_user_account(user)
        repo.create_new_user_account(user2)

        session.commit()
