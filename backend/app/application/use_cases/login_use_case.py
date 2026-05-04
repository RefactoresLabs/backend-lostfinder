from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface
from backend.app.domain.exceptions.invalid_credentials_error import InvalidCredentialsError

from backend.app.application.dtos.login_dto import LoginDTO
from backend.app.application.interfaces.password_hasher import PasswordHasher
from backend.app.application.interfaces.token_generator import TokenGenerator


class LoginUseCase:

    """Caso de uso responsável pela autenticação de uma conta de usuário"""

    def __init__(
        self,
        repository: UserAccountRepositoryInterface,
        hasher: PasswordHasher,
        token_generator: TokenGenerator,
    ) -> None:

        """Inicializa os atributos de instância de LoginUseCase

        Parameters
        ----------
        repository: UserAccountRepositoryInterface
            Repositório da conta de usuário para busca dos dados

        hasher: PasswordHasher
            Algoritmo de hash usado para verificar a senha

        token_generator: TokenGenerator
            Gerador de token de autenticação

        """

        self.__repository = repository
        self.__hasher = hasher
        self.__token_generator = token_generator

    def execute(self, dto: LoginDTO) -> str:

        """Executa o fluxo de autenticação e retorna o token JWT

        Parameters
        ----------
        dto: LoginDTO
            Objeto de transferência de dados com email e senha

        Returns
        -------
        str
            Token JWT gerado após autenticação bem-sucedida

        Raises
        ------
        InvalidCredentialsError
            Se o e-mail não for encontrado ou a senha estiver incorreta

        """

        user_account = self.__repository.get_user_account_by_email(dto.email)

        if user_account is None:
            raise InvalidCredentialsError()

        password_match = self.__hasher.verify(dto.password, user_account.password)

        if not password_match:
            raise InvalidCredentialsError()

        payload = {
            "user_id": user_account.id,
            "email": user_account.email,
        }

        return self.__token_generator.generate(payload)
