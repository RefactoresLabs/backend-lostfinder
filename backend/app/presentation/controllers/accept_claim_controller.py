from backend.app.application.use_cases.accept_claim_use_case import AcceptClaimUseCase
from backend.app.application.dtos.accept_claim_input_dto import AcceptClaimInputDTO

from backend.app.domain.exceptions.user_account_doesnt_have_permission_error import UserAccountDoesntHavePermissionError
from backend.app.domain.exceptions.claim_doesnt_exist_error import ClaimDoesntExistError
from backend.app.domain.exceptions.current_claim_status_error import CurrentClaimStatusError

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse


class AcceptClaimController:

    """Ponto de acesso entre o endpoint e o caso de uso de aceitar uma negociação de recuperação de item"""

    def __init__(self, use_case: AcceptClaimUseCase) -> None:

        """Inicializa os atributos de instância de AcceptClaimController

        Parameters
        ----------
        use_case: AcceptClaimUseCase
            Caso de uso de aceitar uma negociação de recuperação de item

        
        """

        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Aceita uma negociação de recuperação de item

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP
        
        Returns
        -------
        HttpResponse
            Resposta HTTP

        """

        input_dto = AcceptClaimInputDTO(
            http_request.params["claim_id"],
            http_request.params["user_id"],
        )

        try:

            output_dto = self.__use_case.execute(input_dto)

            return HttpResponse(
                200,
                {
                    "retrieval_code": output_dto.retrieval_code,
                }
            )
        
        except ClaimDoesntExistError as exc:

            return HttpResponse(
                404,
                {
                    "message": str(exc),
                    "code": "CLAIM_DOESNT_EXIST_ERROR",
                }
            )
        
        except UserAccountDoesntHavePermissionError as exc:

            return HttpResponse(
                400,
                {
                    "message": str(exc),
                    "code": "USER_ACCOUNT_DOESNT_HAVE_PERMISSION_ERROR",
                }
            )
        
        except CurrentClaimStatusError as exc:

            return HttpResponse(
                400,
                {
                    "message": str(exc),
                    "code": "CURRENT_CLAIM_STATUS_ERROR",
                }
            )