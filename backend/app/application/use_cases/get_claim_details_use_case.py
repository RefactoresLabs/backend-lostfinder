from backend.app.domain.repositories.claim_repository_interface import ClaimRepositoryInterface
from backend.app.domain.exceptions.claim_doesnt_exist_error import ClaimDoesntExistError
from backend.app.application.dtos.get_claim_details_input_dto import GetClaimDetailsInputDTO
from backend.app.application.dtos.get_claim_details_output_dto import GetClaimDetailsOutputDTO


class GetClaimDetailsUseCase:

    """Representa um caso de uso de obter os detalhes de uma negociação de recuperação"""

    def __init__(self, repository: ClaimRepositoryInterface) -> None:

        """Inicializa os atributos de instância de GetClaimDetailsUseCase

        Parameters
        ----------
        repository: ClaimRepositoryInterface
            Repositório de negociações para busca dos dados

        """

        self.__repository = repository

    def execute(self, dto: GetClaimDetailsInputDTO) -> GetClaimDetailsOutputDTO:

        """Executa o fluxo de eventos do caso de uso de obter os dados da negociação detalhada

        Parameters
        ----------
        dto: GetClaimDetailsInputDTO
            Objeto de transferência de dados contendo o ID da negociação a ser detalhada
        
        Returns
        -------
        GetClaimDetailsOutputDTO
            Objeto de transferência de dados com os dados detalhados da negociação

        Raises
        ------
        ClaimDoesntExistError
            Exceção levantada quando uma negociação não foi encontrada
            
        """

        claim = self.__repository.get_claim_by_id(dto.claim_id)

        if not claim:
            raise ClaimDoesntExistError("Negociação não encontrada")

        return GetClaimDetailsOutputDTO(
            claim.id,
            claim.status.name,
            claim.claimant_user_account.name,
            claim.claimant_user_account.phone,
            claim.associated_found_item.id,
            claim.associated_found_item.name,
            claim.created_at.isoformat(),
            claim.retrieval_code if claim.retrieval_code else ""
        )
