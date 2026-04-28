from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse

from backend.app.application.dtos.create_found_item_dto import CreateFoundItemDTO
from backend.app.application.use_cases.create_found_item_use_case import CreateFoundItemUseCase


class CreateFoundItemController:

    """Ponto de acesso entre o endpoint /found-items e o caso de uso CreateFoundItemUseCase"""

    def __init__(self, use_case: CreateFoundItemUseCase) -> None:

        """Inicializa os atributos de instância de CreateFoundItemController

        Parameters
        ----------
        use_case: CreateFoundItemUseCase
            Caso de uso de registro de item encontrado

        """

        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Registra um item encontrado com os dados obtidos do endpoint

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP com os dados do endpoint

        Returns
        -------
        HttpResponse
            Resposta HTTP com os dados do item encontrado ou mensagem de erro

        """

        body = http_request.body

        required_fields = ["name", "description", "category_id", "found_building_space_id", "left_building_space_id"]

        if not all([field in body.keys() for field in required_fields]):

            return HttpResponse(
                400,
                {
                    "message": "Campos obrigatórios não informados"
                }
            )

        for field in required_fields:

            if isinstance(body[field], str) and not body[field].strip():

                return HttpResponse(
                    400,
                    {
                        "message": f"Campo {field} está vazio"
                    }
                )

        image_urls = body.get("image_urls", [])

        dto = CreateFoundItemDTO(
            name=body["name"],
            description=body["description"],
            image_urls=image_urls,
            category_id=body["category_id"],
            user_id=http_request.params["user_id"],
            found_building_space_id=body["found_building_space_id"],
            left_building_space_id=body["left_building_space_id"],
        )

        try:

            result = self.__use_case.execute(dto)

            return HttpResponse(
                201,
                {
                    "message": "Item encontrado registrado com sucesso!",
                    "data": result,
                }
            )

        except ValueError as exc:

            return HttpResponse(
                404,
                {
                    "message": str(exc)
                }
            )
