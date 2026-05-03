from backend.app.domain.exceptions.item_doesnt_exist_error import ItemDoesntExistError

from backend.app.application.use_cases.get_found_item_details_use_case import GetFoundItemDetailsUseCase
from backend.app.application.dtos.get_item_details_input_dto import GetItemDetailsInputDTO

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse


class GetFoundItemDetailsController:

    """O Ponto de acesso entre endpoint e o caso de uso de obter dados detalhados de um item encontrado"""

    def __init__(self, use_case: GetFoundItemDetailsUseCase) -> None:

        """Inicializa os atributos de instância de GetFoundItemDetailsController

        Parameters
        ----------
        use_case: GetFoundItemDetailsUseCase
            Caso de uso de obtenção dos dados detalhados de um item encontrado
        

        """

        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Obtém os dados detalhados de um item encontrado
        
        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP com os dados do endpoint
        
        Returns
        -------
        HttpResponse
            Resposta HTTP

        """

        item_id = http_request.params["item_id"]

        input_dto = GetItemDetailsInputDTO(item_id)

        try:

            output_dto = self.__use_case.execute(input_dto)

            body = {
                "id": output_dto.item_id,
                "name": output_dto.item_name,
                "description": output_dto.item_description,
                "item_image_urls": output_dto.item_image_urls,
                "user": {
                    "name": output_dto.user_name,
                    "email": output_dto.user_email,
                    "phone": output_dto.user_phone,
                },
                "category": {
                    "name": output_dto.item_category_name,
                },
                "found_building_space": {
                    "name": output_dto.found_building_space_name,
                    "building": {
                        "name": output_dto.found_building_name,
                        "localization": {
                            "cep": output_dto.found_localization_cep,
                            "neighborhood": output_dto.found_localization_neighborhood,
                            "street": output_dto.found_localization_street,
                        },
                    },
                },
                "left_building_space": {
                    "name": output_dto.left_building_space_name,
                    "building": {
                        "name": output_dto.left_building_name,
                        "localization": {
                            "cep": output_dto.left_localization_cep,
                            "neighborhood": output_dto.left_localization_neighborhood,
                            "street": output_dto.left_localization_street,
                        },
                    },
                }
            }

            return HttpResponse(
                status_code=200,
                body=body
            )
        
        except ItemDoesntExistError as exc:

            return HttpResponse(
                status_code=404,
                body={
                    "message": str(exc),
                    "code": "ITEM_DOESNT_EXIST_ERROR"
                }
            )