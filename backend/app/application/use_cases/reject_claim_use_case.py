from backend.app.domain.repositories.claim_repository_interface import ClaimRepositoryInterface
from backend.app.domain.exceptions.claim_doesnt_exist_error import ClaimDoesntExistError
from backend.app.domain.exceptions.current_claim_status_error import CurrentClaimStatusError
from backend.app.domain.exceptions.user_account_doesnt_have_permission_error import UserAccountDoesntHavePermissionError

from backend.app.domain.entities.claim import Claim
from backend.app.domain.value_objects.claim_status import ClaimStatus

from backend.app.application.dtos.reject_claim_dto import RejectClaimDTO


class RejectClaimUseCase:

    """Representa um caso de uso de rejeitar uma negociação de recuperação de item"""

    def __init__(self, claim_repository: ClaimRepositoryInterface) -> None:

        """Inicializa os atributos de instância de RejectClaimUseCase

        Parameters
        ----------
        claim_repository: ClaimRepositoryInterface
            Repositório de negociação de recuperação de item para busca de dados

        """

        self.__claim_repository = claim_repository
    
    def execute(self, dto: RejectClaimDTO) -> None:

        """Executa o fluxo de eventos do caso de uso

        Parameters
        ----------
        dto: RejectClaimDTO
            Objeto de transferência de dados contendo o ID da negociação e o ID do usuário logado
        
        Raises
        ------
        ClaimDoesntExistError
            Exceção levantada quando uma negociação não for encontrada
        
        UserAccountDoesntHavePermissionError
            Exceção levantada caso o usuário logado não seja quem criou o item encontrado
        
        CurrentClaimStatusError
            Exceção levantada caso o status de negociação atual não seja Pendente

        """

        claim = self.__claim_repository.get_claim_by_id(dto.claim_id)

        if not claim:

            raise ClaimDoesntExistError("Negociação não encontrada")
        
        if dto.user_id != claim.associated_found_item.associated_user_account.id:

            raise UserAccountDoesntHavePermissionError("Usuário não tem permissão para essa operação")

        if claim.status.name != "Pendente":

            raise CurrentClaimStatusError("Uma negociação que não tenha status 'Pendente' não pode ser rejeitada")

        new_claim = Claim(
            id=claim.id,
            created_at=claim.created_at,
            claimant_user_account=claim.claimant_user_account,
            associated_found_item=claim.associated_found_item,
            status=ClaimStatus("Rejeitada"),
            retrieval_code=claim.retrieval_code,
        )

        _ = self.__claim_repository.update_claim(new_claim, dto.claim_id)
