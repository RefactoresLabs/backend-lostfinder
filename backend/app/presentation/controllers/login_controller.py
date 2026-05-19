from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse

from backend.app.application.dtos.login_dto import LoginDTO
from backend.app.application.use_cases.login_use_case import LoginUseCase

from backend.app.domain.exceptions.invalid_credentials_error import InvalidCredentialsError


class LoginController:

    """Ponto de acesso entre o endpoint /login e o caso de uso LoginUseCase"""

    def __init__(self, use_case: LoginUseCase) -> None:

        """Inicializa os atributos de instância de LoginController

        Parameters
        ----------
        use_case: LoginUseCase
            Caso de uso de autenticação de conta de usuário

        """

        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Autentica uma conta de usuário com os dados obtidos do endpoint

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP com os dados do endpoint

        Returns
        -------
        HttpResponse
            Resposta HTTP com o token JWT ou mensagem de erro

        """

        body = http_request.body

        required_fields = ("email", "password")

        if not all([field in body.keys() for field in required_fields]):
            return HttpResponse(
                400,
                {
                    "message": "Campos obrigatórios não informados",
                    "code": "REQUIRED_FIELD_MISSING_ERROR",
                },
            )

        for field in required_fields:
            if isinstance(body[field], str) and not body[field].strip():
                return HttpResponse(
                    400,
                    {
                        "message": f"Campo {field} está vazio",
                        "code": "EMPTY_FIELD_ERROR",
                        "field": field,
                    },
                )

        dto = LoginDTO(
            email=body["email"],
            password=body["password"],
        )

        try:
            token = self.__use_case.execute(dto)

            return HttpResponse(
                200,
                {
                    "token": token
                },
            )

        except InvalidCredentialsError as exc:
            return HttpResponse(
                401,
                {
                    "message": str(exc),
                    "code": "INVALID_CREDENTIALS_ERROR",
                },
            )
