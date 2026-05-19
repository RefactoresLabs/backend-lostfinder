from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse

from backend.app.application.dtos.create_lost_item_dto import CreateLostItemDTO
from backend.app.application.use_cases.create_lost_item_use_case import CreateLostItemUseCase

from backend.app.domain.exceptions.category_doesnt_exist_error import CategoryDoesntExistError
from backend.app.domain.exceptions.building_space_doesnt_exist_error import BuildingSpaceDoesntExistError
from backend.app.domain.exceptions.user_account_doesnt_exist_error import UserAccountDoesntExistError


class CreateLostItemController:

    """Ponto de acesso entre o endpoint /lost-items e o caso de uso CreateLostItemUseCase"""

    def __init__(self, use_case: CreateLostItemUseCase) -> None:

        """Inicializa os atributos de instância de CreateLostItemController

        Parameters
        ----------
        use_case: CreateLostItemUseCase
            Caso de uso de registro de item perdido

        """

        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Registra um item perdido com os dados obtidos do endpoint

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP com os dados do endpoint

        Returns
        -------
        HttpResponse
            Resposta HTTP com os dados do item perdido ou mensagem de erro

        """

        body = http_request.body

        required_fields = ("name", "description", "category_id", "lost_building_space_id")

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
                        "field": "email",
                    }
                )

        image_urls = body.get("image_urls", [])

        dto = CreateLostItemDTO(
            name=body["name"],
            description=body["description"],
            image_urls=image_urls,
            category_id=body["category_id"],
            user_id=http_request.params["user_id"],
            lost_building_space_id=body["lost_building_space_id"],
        )

        try:

            self.__use_case.execute(dto)

            return HttpResponse(
                201,
                {
                    "message": "Item perdido registrado com sucesso!",
                }
            )

        except CategoryDoesntExistError as exc:

            return HttpResponse(
                400,
                {
                    "message": str(exc),
                    "code": "CATEGORY_DOESNT_EXIST_ERROR"
                }
            )

        except BuildingSpaceDoesntExistError as exc:

            return HttpResponse(
                400,
                {
                    "message": str(exc),
                    "code": "BUILDING_SPACE_DOESNT_EXIST_ERROR",
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
