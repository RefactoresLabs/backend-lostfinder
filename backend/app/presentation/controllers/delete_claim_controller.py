from backend.app.domain.exceptions.claim_doesnt_exist_error import ClaimDoesntExistError
from backend.app.application.use_cases.delete_claim_use_case import DeleteClaimUseCase
from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse


class DeleteClaimController:

    """O Ponto de acesso entre endpoint e o caso de uso de excluir uma negociação"""

    def __init__(self, use_case: DeleteClaimUseCase) -> None:

        """Inicializa os atributos de instância de DeleteClaimController

        Parameters
        ----------
        use_case: DeleteClaimUseCase
            Caso de uso de exclusão de uma negociação

        """

        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Exclui uma negociação
        
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

        try:
            self.__use_case.execute(claim_id)

            return HttpResponse(
                status_code=200,
                body={
                    "message": "Negociação excluída com sucesso",
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
