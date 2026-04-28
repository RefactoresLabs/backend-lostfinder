from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface
from backend.app.domain.entities.user_account import UserAccount

from backend.app.application.services.user_account_validation_service import UserAccountValidationService
from backend.app.application.dtos.register_user_account_dto import RegisterUserAccountDTO
from backend.app.application.interfaces.password_hasher import PasswordHasher
from backend.app.application.exceptions.passwords_dont_match_error import PasswordsDontMatchError

class RegisterUserAccountUseCase:

    def __init__(self, repository: UserAccountRepositoryInterface, hasher: PasswordHasher, user_account_validation_service: UserAccountValidationService) -> None:

        """Inicializa os atributos de instância de RegisterUserAccountUseCase

        Parameters
        ----------
        repository: UserAccountRepositoryInterface
            Repositório da conta de usuário para persistência dos dados
        
        hasher: PasswordHasher
            Algoritmo de hash usado para ocultar a senha
        
        user_account_validation_service: UserAccountValidationService
            Serviço de validação da conta de usuário
        
        """

        self.__repository = repository
        self.__hasher = hasher
        self.__user_account_validation_service = user_account_validation_service
    
    def execute(self, dto: RegisterUserAccountDTO) -> None:

        """Executa o fluxo de eventos do caso de uso registrar usuário, a partir dos dados do DTO

        Parameters
        ----------
        dto: RegisterUserAccountDTO
            Objeto de transferência de dados contendo os dados a serem registrados

        """

        self.__user_account_validation_service.validate_email_exists(dto.email)
        
        hashed_password = self.__hasher.hash(dto.password)

        _ = self.__repository.create_new_user_account(
            UserAccount(
                None,
                dto.name,
                dto.email,
                hashed_password,
                dto.phone,
            )
        )