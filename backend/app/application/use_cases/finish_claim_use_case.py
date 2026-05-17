from backend.app.domain.repositories.claim_repository_interface import ClaimRepositoryInterface
from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface

from backend.app.domain.entities.claim import Claim
from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.value_objects.claim_status import ClaimStatus

from backend.app.domain.exceptions.claim_doesnt_exist_error import ClaimDoesntExistError
from backend.app.domain.exceptions.current_claim_status_error import CurrentClaimStatusError
from backend.app.domain.exceptions.user_account_doesnt_have_permission_error import UserAccountDoesntHavePermissionError
from backend.app.domain.exceptions.retrieval_code_mismatch_error import RetrievalCodeMismatchError

from backend.app.application.dtos.finish_claim_dto import FinishClaimDTO


class FinishClaimUseCase:

    """Representa um caso de uso de finalizar uma negociação de recuperação de item"""

    def __init__(self, claim_repository: ClaimRepositoryInterface, user_account_repository: UserAccountRepositoryInterface):

        """Inicializa os atributos de instância de FinishClaimUseCase

        Parameters
        ----------
        claim_repository: ClaimRepositoryInterface
            Repositório de negociação de recuperação de item para busca de dados
        
        user_account_repository: UserAccountRepositoryInterface
            Repositório de conta de usuário para atualização de dados
        
        """

        self.__claim_repository = claim_repository
        self.__user_account_repository = user_account_repository
    
    def execute(self, dto: FinishClaimDTO) -> None:

        """Executa o fluxo de eventos do caso de uso

        Parameters
        ----------
        dto: FinishClaimDTO
            Objeto de transferência de dados contendo o ID da negociação a ser finalizada
        
        Raises
        ------
        ClaimDoesntExistError
            Exceção levantanda quando a negociação não for encontrada
        
        UserAccountDoesntHavePermissionError
            Exceção levantada quando a conta de usuário logada não corresponde a quem criou a negociação

        CurrentClaimStatusError
            Exceção levantada caso o status de negociação atual não seja Aceita   

        RetrievalCodeMismatchError
            Exceção levantada caso o código passado não corresponda ao código da negociação

        """

        claim = self.__claim_repository.get_claim_by_id(dto.claim_id)

        if not claim:

            raise ClaimDoesntExistError("Negociação não encontrada")

        if dto.user_id != claim.claimant_user_account.id:

            raise UserAccountDoesntHavePermissionError("Usuário não tem permissão para essa operação")
        
        if claim.status.name != "Aceita":

            raise CurrentClaimStatusError("Uma negociação que não tenha status 'Aceita' não pode ser concluída")

        if dto.retrieval_code != claim.retrieval_code:

            raise RetrievalCodeMismatchError("O código de recuperação passado não corresponde ao da negociação")

        new_claim = Claim(
            id=claim.id,
            created_at=claim.created_at,
            claimant_user_account=claim.claimant_user_account,
            associated_found_item=claim.associated_found_item,
            status=ClaimStatus("Finalizada"),
            retrieval_code=claim.retrieval_code,
        )

        _ = self.__claim_repository.update_claim(new_claim, dto.claim_id)

        new_found_item_user_account = UserAccount(
            id=claim.associated_found_item.associated_user_account.id,
            name=claim.associated_found_item.associated_user_account.name,
            email=claim.associated_found_item.associated_user_account.email,
            password=claim.associated_found_item.associated_user_account.password,
            phone=claim.associated_found_item.associated_user_account.phone,
            score=50,
        )

        new_claimant_user_account = UserAccount(
            id=claim.claimant_user_account.id,
            name=claim.claimant_user_account.name,
            email=claim.claimant_user_account.email,
            password=claim.claimant_user_account.password,
            phone=claim.claimant_user_account.phone,
            score=20,
        )

        _ = self.__user_account_repository.update_user_account(new_found_item_user_account, new_found_item_user_account.id)
        _ = self.__user_account_repository.update_user_account(new_claimant_user_account, new_claimant_user_account.id)



