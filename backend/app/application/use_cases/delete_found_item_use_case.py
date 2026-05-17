from backend.app.domain.repositories.found_item_repository_interface import FoundItemRepositoryInterface
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError
from backend.app.application.dtos.delete_found_item_dto import DeleteFoundItemDTO


class DeleteFoundItemUseCase:

    """Caso de uso responsável pela exclusão de um item encontrado"""

    def __init__(self, repository: FoundItemRepositoryInterface) -> None:

        """Inicializa os atributos de instância de DeleteFoundItemUseCase

        Parameters
        ----------
        repository: FoundItemRepositoryInterface
            Repositório de item encontrado para execução das operações

        """

        self.__repository = repository

    def execute(self, dto: DeleteFoundItemDTO) -> bool:

        """Executa o fluxo de eventos do caso de uso de excluir um item encontrado

        Parameters
        ----------
        dto: DeleteFoundItemDTO
            DTO contendo o ID do item encontrado a ser excluído

        Returns
        -------
        bool
            Retorna True se o item foi excluído com sucesso

        Raises
        ------
        ItemDoesntExistError
            Exceção levantada quando um item não foi encontrado

        """

        deleted = self.__repository.delete_found_item(dto.item_id)

        if not deleted:

            raise ItemDoesntExistError("Item não encontrado")

        return deleted
