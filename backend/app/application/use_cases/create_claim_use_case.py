from backend.app.domain.repositories.claim_repository_interface import ClaimRepositoryInterface
from backend.app.domain.repositories.found_item_repository_interface import FoundItemRepositoryInterface
from backend.app.domain.repositories.user_account_repository_interface import UserAccountRepositoryInterface

from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError
from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError

from backend.app.domain.entities.claim import Claim
from backend.app.domain.value_objects.claim_status import ClaimStatus

from backend.app.application.dtos.create_claim_dto import CreateClaimDTO


class CreateClaimUseCase:

    """Representa um caso de uso de criar uma negociação de recuperação de item"""

    def __init__(
            self, 
            claim_repository: ClaimRepositoryInterface, 
            found_item_repository: FoundItemRepositoryInterface,
            user_account_repository: UserAccountRepositoryInterface
            ):
        
        """Inicializa os atributos de instância de CreateClaimUseCase

        Parameters
        ----------
        claim_repository: ClaimRepositoryInterface
            Repositório de negociação de recuperação de item para persistência de dados
        
        found_item_repository: FoundItemRepositoryInterface
            Repositório de item encontrado para busca de dados
        
        user_account_repository: UserAccountRepositoryInterface
            Repositório de conta de usuário para busca de dados

        """
        
        self.__claim_repository = claim_repository
        self.__found_item_repository = found_item_repository
        self.__user_account_repository = user_account_repository
    
    def execute(self, dto: CreateClaimDTO) -> None:

        """Executa o fluxo de eventos do caso de uso

        Parameters
        ----------
        dto: CreateClaimDTO
            Objeto de transferência de dados contendo os dados a serem armazenados
        
        Raises
        ------
        ItemDoesntExistError
            Exceção levantada quando o item não for encontrado
        
        UserAccountDoesntExistError
            Exceção levantada quando a conta de usuário não for encontrada
        
        """

        found_item = self.__found_item_repository(dto.found_item_id)

        if not found_item:

            raise ItemDoesntExistError("Item não encontrado")

        user_account = self.__user_account_repository.get_user_account_by_id(dto.user_id)

        if not user_account:

            raise UserAccountDoesntExistError("Conta de usuário não encontrada")

        claim = Claim(
            id=None,
            created_at=None,
            claimant_user_account=user_account,
            associated_found_item=found_item,
            status=ClaimStatus("Pendente")
        )

        _ = self.__claim_repository.create_new_claim(claim)

