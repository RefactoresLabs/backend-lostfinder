from backend.app.domain.exceptions.claim_doesnt_exist_error import ClaimDoesntExistError
from backend.app.application.use_cases.get_claim_details_use_case import GetClaimDetailsUseCase
from backend.app.application.dtos.get_claim_details_input_dto import GetClaimDetailsInputDTO
from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse


class GetClaimDetailsController:

    """O Ponto de acesso entre endpoint e o caso de uso de obter dados detalhados de uma negociação"""

    def __init__(self, use_case: GetClaimDetailsUseCase) -> None:

        """Inicializa os atributos de instância de GetClaimDetailsController

        Parameters
        ----------
        use_case: GetClaimDetailsUseCase
            Caso de uso de obtenção dos dados detalhados de uma negociação

        """

        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Obtém os dados detalhados de uma negociação
        
        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP com os dados do endpoint
        
        Returns
        -------
        HttpResponse
            Resposta HTTP

        """

        claim_id = http_request.params["claim_id"]

        input_dto = GetClaimDetailsInputDTO(claim_id)

        try:
            output_dto = self.__use_case.execute(input_dto)

            return HttpResponse(
                status_code=200,
                body={
                    "id": output_dto.claim_id,
                    "status": {
                        "name": output_dto.status_name,
                    },
                    "claimant_user_account": {
                        "name": output_dto.claimant_user_name,
                        "phone": output_dto.claimant_user_phone,
                    },
                    "associated_found_item": {
                        "id": output_dto.associated_found_item_id,
                        "name": output_dto.associated_found_item_name,
                    },
                    "created_at": output_dto.created_at,
                },
            )

        except ClaimDoesntExistError as exc:
            return HttpResponse(
                status_code=404,
                body={
                    "message": str(exc),
                    "code": "CLAIM_DOESNT_EXIST_ERROR",
                },
            )
