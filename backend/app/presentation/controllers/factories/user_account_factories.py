from backend.app.application.services.user_account_validation_service import UserAccountValidationService
from backend.app.application.use_cases.register_user_account_use_case import RegisterUserAccountUseCase

from backend.app.infrastructure.persistence.repositories.user_account_repository import UserAccountRepository
from backend.app.infrastructure.security.bcrypt_hasher import BcryptHasher
from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder

from backend.app.presentation.controllers.register_user_account_controller import RegisterUserAccountController

from sqlalchemy.orm import Session

def make_register_user_account_controller(session: Session) -> RegisterUserAccountController:

    """Factory function que cria um objeto RegisterUserAccountController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    RegisterUserAccountController
        Ponto de acesso do endpoint com o caso de uso de registro de conta de usuário
        
    """

    user_account_repository = UserAccountRepository(session)

    register_user_account_use_case = RegisterUserAccountUseCase(
          user_account_repository,
          BcryptHasher(),
          UserAccountValidationService(user_account_repository)
    )

    return RegisterUserAccountController(register_user_account_use_case)

