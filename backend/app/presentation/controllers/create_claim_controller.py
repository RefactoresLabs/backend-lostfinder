from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError
from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError

from backend.app.application.use_cases.create_claim_use_case import CreateClaimUseCase
from backend.app.application.dtos.create_claim_dto import CreateClaimDTO

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse


class CreateClaimController:

    """Ponto de acesso entre o endpoint e o caso de uso de criar uma negociação de recuperação de item"""

    def __init__(self, use_case: CreateClaimUseCase) -> None:

        """Inicializa os atributos de instância de CreateClaimController

        Parameters
        ----------
        use_case: CreateClaimUseCase
            Caso de uso de criar uma negociação de recuperação de item
        
        """

        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Cria uma negociação de recuperação de item

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP
        
        Returns
        -------
        HttpResponse
            Resposta HTTP

        """

        dto = CreateClaimDTO(
            http_request.body["found_item_id"],
            http_request.params["user_id"],
        )

        try:

            self.__use_case.execute(dto)

            return HttpResponse(
                201,
                {
                    "message": "Negociação registrada com sucesso!"
                }
            )
        
        except ItemDoesntExistError as exc:

            return HttpResponse(
                400,
                {
                    "message": str(exc),
                    "code": "ITEM_DOESNT_EXIST_ERROR",
                }
            )

        except UserAccountDoesntExistError as exc:

            return HttpResponse(
                400,
                {
                    "message": str(exc),
                    "code": "USER_ACCOUNT_DOESNT_EXIST_ERROR",
                }
            )

        