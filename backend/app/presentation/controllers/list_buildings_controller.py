from backend.app.application.use_cases.list_buildings_use_case import ListBuildingsUseCase

from backend.app.presentation.schemas.http_response import HttpResponse


class ListBuildingsController:

    """Ponto de acesso entre o endpoint e o caso de uso de listar prédios"""

    def __init__(self, use_case: ListBuildingsUseCase) -> None:

        """Inicializa os atributos de instância de ListBuildingsController

        Parameters
        ----------
        use_case: ListBuildingsUseCase
            Caso de uso de listar prédios

        """

        self.__use_case = use_case
    
    def handle(self) -> HttpResponse:

        """Lista os prédios do sistema

        Returns
        -------
        HttpResponse
            Resposta HTTP

        """

        dtos = self.__use_case.execute()

        return HttpResponse(
            200,
            body=[
                {
                    "id": dto.id,
                    "name": dto.name,
                }
                for dto in dtos
            ]
        )