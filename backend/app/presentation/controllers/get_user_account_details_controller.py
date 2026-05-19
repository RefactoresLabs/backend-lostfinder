from backend.app.application.use_cases.get_user_account_details_use_case import GetUserAccountDetailsUseCase
from backend.app.application.dtos.get_user_account_details_input_dto import GetUserAccountDetailsInputDTO

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse

from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError


class GetUserAccountDetailsController:

    """Ponto de acesso entre o endpoint e o caso de uso de obter os detalhes da conta de usuário"""

    def __init__(self, use_case: GetUserAccountDetailsUseCase) -> None:

        """Inicializa os atributos de instância de GetUserAccountDetailsController

        Parameters
        ----------
        use_case: GetUserAccountDetailsUseCase
            Caso de uso de obter os detalhes de uma conta de usuário

        """

        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Obtém os detalhes de uma conta de usuário

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP
        
        Returns
        -------
        HttpResponse
            Resposta HTTP

        """

        input_dto = GetUserAccountDetailsInputDTO(
            http_request.params["user_id"],
        )

        try:

            output_dto = self.__use_case.execute(input_dto)

            return HttpResponse(
                200,
                {
                    "id": output_dto.id,
                    "name": output_dto.name,
                    "email": output_dto.email,
                    "phone": output_dto.phone,
                    "score": output_dto.score,
                }
            )
        
        except UserAccountDoesntExistError as exc:

            return HttpResponse(
                404,
                {
                    "message": str(exc),
                    "code": "USER_ACCOUNT_DOESNT_EXIST_ERROR",
                }
            )

        

        