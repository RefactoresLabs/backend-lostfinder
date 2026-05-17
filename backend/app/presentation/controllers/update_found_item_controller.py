from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse

from backend.app.application.dtos.update_found_item_dto import UpdateFoundItemDTO
from backend.app.application.use_cases.update_found_item_use_case import UpdateFoundItemUseCase

from backend.app.domain.exceptions.category_doesnt_exist_error import CategoryDoesntExistError
from backend.app.domain.exceptions.building_space_doesnt_exist_error import BuildingSpaceDoesntExistError
from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError


class UpdateFoundItemController:

    """Ponto de acesso entre o endpoint /found-items/{item_id} e o caso de uso UpdateFoundItemUseCase"""

    def __init__(self, use_case: UpdateFoundItemUseCase) -> None:

        """Inicializa os atributos de instância de UpdateFoundItemController

        Parameters
        ----------
        use_case: UpdateFoundItemUseCase
            Caso de uso de atualização de item encontrado

        """

        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Atualiza um item encontrado com os dados obtidos do endpoint

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP com os dados do endpoint

        Returns
        -------
        HttpResponse
            Resposta HTTP com mensagem de sucesso ou erro

        """

        body = http_request.body
        item_id = http_request.params["item_id"]

        required_fields = ["name", "description", "category_id", "found_building_space_id", "left_building_space_id"]

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
                        "field": field,
                    }
                )

        image_urls = body.get("image_urls", [])

        dto = UpdateFoundItemDTO(
            item_id=item_id,
            name=body["name"],
            description=body["description"],
            image_urls=image_urls,
            category_id=body["category_id"],
            found_building_space_id=body["found_building_space_id"],
            left_building_space_id=body["left_building_space_id"],
        )

        try:

            self.__use_case.execute(dto)

            return HttpResponse(
                200,
                {
                    "message": "Item encontrado atualizado com sucesso",
                }
            )

        except ItemDoesntExistError as exc:

            return HttpResponse(
                404,
                {
                    "message": str(exc),
                    "code": "ITEM_DOESNT_EXIST_ERROR",
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
