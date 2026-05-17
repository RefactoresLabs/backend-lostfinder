from backend.app.domain.repositories.claim_repository_interface import ClaimRepositoryInterface
from backend.app.domain.exceptions.claim_doesnt_exist_error import ClaimDoesntExistError
from backend.app.application.dtos.delete_claim_dto import DeleteClaimDTO


class DeleteClaimUseCase:

    """Representa um caso de uso de excluir uma negociação de recuperação"""

    def __init__(self, repository: ClaimRepositoryInterface) -> None:

        """Inicializa os atributos de instância de DeleteClaimUseCase

        Parameters
        ----------
        repository: ClaimRepositoryInterface
            Repositório de negociações para execução das operações

        """

        self.__repository = repository

    def execute(self, dto: DeleteClaimDTO) -> bool:

        """Executa o fluxo de eventos do caso de uso de excluir uma negociação

        Parameters
        ----------
        dto: DeleteClaimDTO
            DTO contendo o ID da negociação a ser excluída
        
        Returns
        -------
        bool
            Retorna True se a negociação foi excluída com sucesso

        Raises
        ------
        ClaimDoesntExistError
            Exceção levantada quando uma negociação não foi encontrada
            
        """

        deleted = self.__repository.delete_claim(dto.claim_id)

        if not deleted:
            raise ClaimDoesntExistError("Negociação não encontrada")

        return deleted
