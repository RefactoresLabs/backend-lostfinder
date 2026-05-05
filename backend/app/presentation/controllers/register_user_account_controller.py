from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse

from backend.app.application.dtos.register_user_account_dto import RegisterUserAccountDTO
from backend.app.application.use_cases.register_user_account_use_case import RegisterUserAccountUseCase

from backend.app.domain.exceptions.email_exists_error import EmailExistsError


class RegisterUserAccountController:

    """Ponto de acesso entre o endpoint e caso de uso RegisterUserAccountUseCase"""

    def __init__(self, use_case: RegisterUserAccountUseCase) -> None:

        """Inicializa os atributos de instância de RegisterUserAccountController

        Parameters
        ----------
        use_case: RegisterUserAccountUseCase
            Caso de uso de registro de conta de usuário
        
        """

        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Registra uma conta de usuário com os dados obtidos do endpoint

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP com os dados do endpoint
        
        Returns
        -------
        HttpResponse
            Resposta HTTP

        """

        body = http_request.body

        required_fields = ["name", "email", "password", "confirm_password", "phone"]

        if not all([field in body.keys() for field in required_fields]):

            return HttpResponse(
                400, 
                {
                    "message": "Campos obrigatórios não informados",
                    "code": "REQUIRED_FIELD_MISSING_ERROR",
                }
            )
        
        for field in required_fields:

            if isinstance(body[field], str) and not body[field].strip():

                return HttpResponse(
                    400, 
                    {
                        "message": f"Campo {field} está vazio",
                        "code": "EMPTY_FIELD_ERROR",
                        "field": field
                    }
                )


        if body["password"] != body["confirm_password"]:

            return HttpResponse(
                400, 
                {
                    "message": "Senha e confirmar senha não correspondem",
                    "code": "PASSWORD_MISMATCH_ERROR",
                }
            )
        
        dto = RegisterUserAccountDTO(
            body["name"],
            body["email"],
            body["password"],
            body["phone"],
        )

        try:

            self.__use_case.execute(dto)

            return HttpResponse(
                201, 
                {
                    "message": "Conta de usuário registrada com sucesso"
                }
            )

        except EmailExistsError as exc:

            return HttpResponse(
                409,
                {
                    "message": str(exc),
                    "code": "EMAIL_ALREADY_EXISTS_ERROR",
                }
            ) 

        



