from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface
from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError

from backend.app.application.dtos.get_user_account_details_input_dto import GetUserAccountDetailsInputDTO
from backend.app.application.dtos.get_user_account_details_output_dto import GetUserAccountDetailsOutputDTO


class GetUserAccountDetailsUseCase:

    """Representa o caso de uso de obter os detalhes de uma conta de usuário"""

    def __init__(self, user_repository: UserAccountRepositoryInterface) -> None:

        """Inicializa os atributos de instância de GetUserAccountDetailsUseCase

        Parameters
        ----------
        user_repository: UserAccountRepositoryInterface
            Repositório de conta de usuário para busca de dados
        
        """

        self.__repository = user_repository
    
    def execute(self, dto: GetUserAccountDetailsInputDTO) -> GetUserAccountDetailsOutputDTO:

        """Executa o fluxo de eventos do caso de uso

        Parameters
        ----------
        dto: GetUserAccountDetailsInputDTO
            Objeto de transferência de dados contendo ID da conta de usuário

        Returns
        -------
        GetUserAccountDetailsOutputDTO
            Objeto de transferência de dados contendo os dados da conta de usuário

        """

        user_account = self.__repository.get_user_account_by_id(dto.user_id)

        if not user_account:

            UserAccountDoesntExistError("Conta de usuário não encontrada")
        
        return GetUserAccountDetailsOutputDTO(
            user_account.id,
            user_account.name,
            user_account.email,
            user_account.phone,
            user_account.score,
        )