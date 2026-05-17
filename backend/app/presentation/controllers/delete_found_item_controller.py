from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError
from backend.app.application.use_cases.delete_found_item_use_case import DeleteFoundItemUseCase
from backend.app.application.dtos.delete_found_item_dto import DeleteFoundItemDTO
from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse


class DeleteFoundItemController:

    """Ponto de acesso entre o endpoint /found-items/{item_id} e o caso de uso DeleteFoundItemUseCase"""

    def __init__(self, use_case: DeleteFoundItemUseCase) -> None:

        """Inicializa os atributos de instância de DeleteFoundItemController

        Parameters
        ----------
        use_case: DeleteFoundItemUseCase
            Caso de uso de exclusão de um item encontrado

        """

        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Exclui um item encontrado

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

        dto = DeleteFoundItemDTO(item_id)

        try:

            self.__use_case.execute(dto)

            return HttpResponse(
                status_code=200,
                body={
                    "message": "Item encontrado excluido com sucesso",
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
