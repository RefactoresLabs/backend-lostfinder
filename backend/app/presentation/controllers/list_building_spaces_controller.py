from backend.app.application.use_cases.list_building_spaces_use_case import ListBuildingSpacesUseCase
from backend.app.application.dtos.list_building_spaces_input_dto import ListBuildingSpacesInputDTO

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse

from backend.app.domain.exceptions.building_doesnt_exist_error import BuildingDoesntExistError

class ListBuildingSpacesController:

    """Ponto de acesso entre o endpoint e o caso de uso de listar espaços de um prédio"""

    def __init__(self, use_case: ListBuildingSpacesUseCase) -> None:

        """Inicializa os atributos de instância de ListBuildingSpacesController

        Parameters
        ----------
        use_case: ListBuildingSpacesUseCase
            Caso de uso de listar espaços de um prédio

        """

        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Lista os espaços de um prédio do sistema

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP

        Returns
        -------
        HttpResponse
            Resposta HTTP

        """

        input_dto = ListBuildingSpacesInputDTO(http_request.params["building_id"])

        try:

            output_dtos = self.__use_case.execute(input_dto)

            return HttpResponse(
                200,
                body=[
                    {
                        "id": output_dto.id,
                        "name": output_dto.name,
                    }
                    for output_dto in output_dtos
                ]
            )
        
        except BuildingDoesntExistError as exc:

            return HttpResponse(
                404,
                body={
                    "message": str(exc),
                    "code": "BUILDING_DOESNT_EXIST_ERROR",
                }
            )