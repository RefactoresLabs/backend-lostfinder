from backend.app.application.use_cases.list_my_created_claims_use_case import ListMyCreatedClaimsUseCase
from backend.app.application.dtos.list_user_account_items_summarized_input_dto import ListUserAccountItemsSummarizedInputDTO

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse

from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError


class ListMyCreatedClaimsController:

    """Ponto de acesso entre o endpoint e o caso de uso de listar negociações criadas pelo usuário autenticado"""

    def __init__(self, use_case: ListMyCreatedClaimsUseCase) -> None:

        """Inicializa os atributos de instância de ListMyCreatedClaimsController

        Parameters
        ----------
        use_case: ListMyCreatedClaimsUseCase
            Caso de uso de listar as negociações criadas pelo usuário autenticado

        """

        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Lista as negociações criadas pelo usuário autenticado resumidamente

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
                        "id": output_dto.claim_id,
                        "claimant_user_account": {
                            "name": output_dto.claimant_user_name,
                        },
                        "associated_found_item": {
                            "id": output_dto.found_item_id,
                            "name": output_dto.found_item_name,
                        },
                    }
                    for output_dto in output_dtos
                ],
            )

        except UserAccountDoesntExistError as exc:

            return HttpResponse(
                404,
                body={
                    "message": str(exc),
                    "code": "USER_ACCOUNT_DOESNT_EXIST_ERROR",
                },
            )