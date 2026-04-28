from backend.app.application.use_cases.list_lost_items_summarized_use_case import ListLostItemsSummarizedUseCase


from backend.app.presentation.schemas.http_response import HttpResponse
from backend.app.presentation.schemas.http_request import HttpRequest


class ListLostItemsSummarizedController:

    """O ponto de acesso entre o endpoint e o caso de uso de listar itens perdidos resumidamente"""

    def __init__(self, use_case: ListLostItemsSummarizedUseCase) -> None:

        """Inicializa os atributos de instância de ListLostItemsSummarizedController

        Parameters
        ----------
        use_case: ListLostItemsSummarizedUseCase
            Caso de uso de listar itens perdidos de forma resumida
        
        
        """

        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Lista os itens perdidos de maneira resumida

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

        dtos = self.__use_case.execute()

        if limit < 0:

            return HttpResponse(
                status_code=400,
                body={
                    "message": "O campo 'limit' não pode ser negativo!"
                }
            )
        
        elif limit == 0:

            return HttpResponse(
                status_code=200,
                body=[
                    {
                        "id": dto.item_id,
                        "name": dto.item_name,
                        "user": dto.user_name,
                        "category": dto.category_name,
                        "location": dto.building_space_name,
                        "image_url": dto.image_url,
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
                        "user": dto.user_name,
                        "category": dto.category_name,
                        "location": dto.building_space_name,
                        "image_url": dto.image_url,
                    }
                for dto in dtos[:limit]
                ],
            )