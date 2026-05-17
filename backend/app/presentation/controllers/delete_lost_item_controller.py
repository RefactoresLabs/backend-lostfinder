from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError
from backend.app.application.use_cases.delete_lost_item_use_case import DeleteLostItemUseCase
from backend.app.application.dtos.delete_lost_item_dto import DeleteLostItemDTO
from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse


class DeleteLostItemController:

    """Ponto de acesso entre o endpoint /lost-items/{item_id} e o caso de uso DeleteLostItemUseCase"""

    def __init__(self, use_case: DeleteLostItemUseCase) -> None:

        """Inicializa os atributos de instância de DeleteLostItemController

        Parameters
        ----------
        use_case: DeleteLostItemUseCase
            Caso de uso de exclusão de um item perdido

        """

        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Exclui um item perdido

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP com os dados do endpoint

        Returns
        -------
        HttpResponse
            Resposta HTTP

        """

        item_id = http_request.params["item_id"]

        dto = DeleteLostItemDTO(item_id)

        try:

            self.__use_case.execute(dto)

            return HttpResponse(
                status_code=200,
                body={
                    "message": "Item perdido excluido com sucesso",
                },
            )

        except ItemDoesntExistError as exc:

            return HttpResponse(
                status_code=404,
                body={
                    "message": str(exc),
                    "code": "ITEM_DOESNT_EXIST_ERROR",
                },
            )
