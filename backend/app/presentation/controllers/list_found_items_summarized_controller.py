from backend.app.application.use_cases.list_found_items_summarized_use_case import ListFoundItemsSummarizedUseCase
from backend.app.application.dtos.list_items_summarized_input_dto import ListItemsSummarizedInputDTO

from backend.app.presentation.schemas.http_response import HttpResponse
from backend.app.presentation.schemas.http_request import HttpRequest


class ListFoundItemsSummarizedController:

    """O ponto de acesso entre o endpoint e o caso de uso de listar itens encontrados resumidamente"""

    def __init__(self, use_case: ListFoundItemsSummarizedUseCase) -> None:

        """Inicializa os atributos de instância de ListFoundItemsSummarizedController

        Parameters
        ----------
        use_case: ListFoundItemsSummarizedUseCase
            Caso de uso de listar itens encontrados de forma resumida
        
        
        """

        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Lista os itens encontrados de maneira resumida

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP com os dados do endpoint
        
        Returns
        -------
        HttpResponse
            Resposta HTTP

        """

        limit = http_request.params.get("limit", 0)

        name = http_request.params.get("name")
        category_id = http_request.params.get("category_id")
        sort_by = http_request.params["sort_by"] if http_request.params["sort_by"] is not None else "name"
        sort_option = http_request.params["sort_option"] if http_request.params["sort_option"] is not None else "asc"

        dto = ListItemsSummarizedInputDTO(
            name,
            category_id,
            sort_by,
            sort_option
        )

        dtos = self.__use_case.execute(dto)

        if limit < 0:

            return HttpResponse(
                status_code=400,
                body={
                    "message": "O campo 'limit' não pode ser negativo!",
                    "code": "NEGATIVE_LIMIT_ERROR"
                }
            )
        
        elif limit == 0:

            return HttpResponse(
                status_code=200,
                body=[
                    {
                        "id": dto.item_id,
                        "name": dto.item_name,
                        "user": {
                            "name": dto.user_name
                        },
                        "category": {
                            "name": dto.category_name,
                        },
                        "found_building_space": {
                            "name": dto.building_space_name,
                        },
                        "image": {
                            "url": dto.image_url,
                        },
                    }
                for dto in dtos
                ],
            )
        
        else:

            return HttpResponse(
                status_code=200,
                body=[
                    {
                        "id": dto.item_id,
                        "name": dto.item_name,
                        "user": {
                            "name": dto.user_name
                        },
                        "category": {
                            "name": dto.category_name,
                        },
                        "found_building_space": {
                            "name": dto.building_space_name,
                        },
                        "image": {
                            "url": dto.image_url,
                        },
                    }
                for dto in dtos[:limit]
                ],
            )