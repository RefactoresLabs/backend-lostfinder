from backend.app.application.interfaces.claim_query_service_interface import ClaimQueryServiceInterface
from backend.app.application.dtos.list_user_account_items_summarized_input_dto import ListUserAccountItemsSummarizedInputDTO
from backend.app.application.dtos.list_created_claims_summarized_dto import ListCreatedClaimsSummarizedDTO

from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError
from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface


class ListMyCreatedClaimsUseCase:

    """Representa um caso de uso de listar as negociações criadas pelo usuário autenticado resumidamente"""

    def __init__(
        self,
        claim_query_service: ClaimQueryServiceInterface,
        user_account_repository: UserAccountRepositoryInterface,
    ) -> None:

        """Inicializa os atributos de instância de ListMyCreatedClaimsUseCase

        Parameters
        ----------
        claim_query_service: ClaimQueryServiceInterface
            Serviço de consulta de negociações

        user_account_repository: UserAccountRepositoryInterface
            Repositório de conta de usuários

        """

        self.__query_service = claim_query_service
        self.__user_account_repository = user_account_repository

    def execute(self, dto: ListUserAccountItemsSummarizedInputDTO) -> list[ListCreatedClaimsSummarizedDTO]:

        """Executa o fluxo de eventos do caso de uso

        Parameters
        ----------
        dto: ListUserAccountItemsSummarizedInputDTO
            Objeto de transferência de dados contendo o ID do usuário cujas negociações criadas serão obtidas

        Returns
        -------
        list[ListCreatedClaimsSummarizedDTO]
            Iterável de objetos de transferência de dados contendo os dados resumidos das negociações criadas

        Raises
        ------
        UserAccountDoesntExistError
            Exceção levantada quando uma conta de usuário não for encontrada

        """

        user_account = self.__user_account_repository.get_user_account_by_id(dto.user_id)

        if not user_account:

            raise UserAccountDoesntExistError("A conta de usuário não foi encontrada!")

        claims = self.__query_service.get_created_claims_summarized_by_user_id(dto.user_id)

        return [
            ListCreatedClaimsSummarizedDTO(
                claim["claim_id"],
                claim["claimant_user_name"],
                claim["found_item_id"],
                claim["found_item_name"],
            )
            for claim in claims
        ]