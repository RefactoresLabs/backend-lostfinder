from backend.app.domain.repositories.lost_item_repository_interface import LostItemRepositoryInterface
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError
from backend.app.application.dtos.delete_lost_item_dto import DeleteLostItemDTO


class DeleteLostItemUseCase:

    """Caso de uso responsável pela exclusão de um item perdido"""

    def __init__(self, repository: LostItemRepositoryInterface) -> None:

        """Inicializa os atributos de instância de DeleteLostItemUseCase

        Parameters
        ----------
        repository: LostItemRepositoryInterface
            Repositório de item perdido para execução das operações

        """

        self.__repository = repository

    def execute(self, dto: DeleteLostItemDTO) -> bool:

        """Executa o fluxo de eventos do caso de uso de excluir um item perdido

        Parameters
        ----------
        dto: DeleteLostItemDTO
            DTO contendo o ID do item perdido a ser excluído

        Returns
        -------
        bool
            Retorna True se o item foi excluído com sucesso

        Raises
        ------
        ItemDoesntExistError
            Exceção levantada quando um item não foi encontrado

        """

        deleted = self.__repository.delete_lost_item(dto.item_id)

        if not deleted:

            raise ItemDoesntExistError("Item não encontrado")

        return deleted
