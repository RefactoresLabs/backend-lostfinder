from backend.app.application.use_cases.list_user_account_found_items_summarized_use_case import ListUserAccountFoundItemsSummarizedUseCase
from backend.app.application.dtos.list_user_account_items_summarized_input_dto import ListUserAccountItemsSummarizedInputDTO

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse

from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError


class ListUserAccountFoundItemsSummarizedController:

    """Ponto de acesso entre o endpoint e o caso de uso de listar itens encontrados resumidamente de uma conta de usuário"""

    def __init__(self, use_case: ListUserAccountFoundItemsSummarizedUseCase) -> None:

        """Inicializa os atributos de instância de ListUserAccountFoundItemsSummarizedController

        Parameters
        ----------
        use_case: ListUserAccountFoundItemsSummarizedUseCase
            Caso de uso de listar os itens encontrados de uma conta de usuário

        """

        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Lista os itens encontrados resumidos de uma conta de usuário específica

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP
        
        Returns
        -------
        http_response: HttpResponse
            Resposta HTTP

        """

        input_dto = ListUserAccountItemsSummarizedInputDTO(
            http_request.params["user_id"]
        )

        try:

            output_dtos = self.__use_case.execute(input_dto)

            return HttpResponse(
                200,
                body=[
                    {
                        "id": output_dto.item_id,
                        "name": output_dto.item_name,
                        "user": {
                            "name": output_dto.user_name,
                        },
                        "category": {
                            "name": output_dto.category_name,
                        },
                        "found_building_space": {
                            "name": output_dto.building_space_name,
                        },
                        "image": {
                            "url": output_dto.image_url,
                        },
                    }
                for output_dto in output_dtos
                ]
            )

        except UserAccountDoesntExistError as exc:

            return HttpResponse(
                404,
                body={
                    "message": str(exc),
                    "code": "USER_ACCOUNT_DOESNT_EXIST_ERROR",
                }
            )

