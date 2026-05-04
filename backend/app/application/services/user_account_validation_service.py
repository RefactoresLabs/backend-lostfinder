from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface
from backend.app.domain.exceptions.email_exists_error import EmailExistsError

class UserAccountValidationService:

    """Lida com validações e regras reutilizáveis da validação de usuário"""

    def __init__(self, repository: UserAccountRepositoryInterface) -> None:

        """Inicializa os atributos de instância de UserAccountValidationService

        Parameters
        ----------
        repository: UserAccountRepositoryInterface
            Repositório da conta de usuário para persistência dos dados
        
        """

        self.__repository = repository

    def validate_email_exists(self, email: str) -> None:

        """Valida se um e-mail já existe no banco

        Parameters
        ----------
        email: str
            E-mail a ser validado
        
        Raises
        ------
        EmailExistsError
            Exceção levantada quando um e-mail já existe no banco

        """
        
        user_account = self.__repository.get_user_account_by_email(email)
    
        if user_account:

            raise EmailExistsError(f"Já existe uma conta de usuário com o e-mail {email} no sistema!")