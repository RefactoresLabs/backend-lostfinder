from backend.app.application.use_cases.login_use_case import LoginUseCase

from backend.app.infrastructure.persistence.repositories.user_account_repository import UserAccountRepository
from backend.app.infrastructure.security.bcrypt_hasher import BcryptHasher
from backend.app.infrastructure.security.jwt_token_generator import JwtTokenGenerator

from backend.app.presentation.controllers.login_controller import LoginController

from sqlalchemy.orm import Session


def make_login_controller(session: Session) -> LoginController:

    """Factory function que cria um objeto LoginController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco

    Returns
    -------
    LoginController
        Ponto de acesso do endpoint com o caso de uso de autenticação

    """

    user_account_repository = UserAccountRepository(session)

    login_use_case = LoginUseCase(
        repository=user_account_repository,
        hasher=BcryptHasher(),
        token_generator=JwtTokenGenerator(),
    )

    return LoginController(login_use_case)
