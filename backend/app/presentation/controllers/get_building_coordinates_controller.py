from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.schemas.http_response import HttpResponse

from backend.app.application.use_cases.get_building_coordinates_use_case import GetBuildingCoordinatesUseCase


class GetBuildingCoordinatesController:

    """Ponto de acesso entre o endpoint /buildings/{id}/coordinates e o caso de uso GetBuildingCoordinatesUseCase"""

    def __init__(self, use_case: GetBuildingCoordinatesUseCase) -> None:

        """Inicializa os atributos de instância de GetBuildingCoordinatesController

        Parameters
        ----------
        use_case: GetBuildingCoordinatesUseCase
            Caso de uso de obter coordenadas do prédio

        """

        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        """Obtém as coordenadas geográficas de um prédio pelo ID

        Parameters
        ----------
        http_request: HttpRequest
            Requisição HTTP com o ID do prédio nos parâmetros

        Returns
        -------
        HttpResponse
            Resposta HTTP com os dados de coordenadas ou mensagem de erro

        """

        params = http_request.params

        building_id = params.get("building_id")

        if building_id is None:

            return HttpResponse(
                400,
                {
                    "message": "Parâmetro building_id é obrigatório"
                }
            )

        try:

            building_id = int(building_id)

        except (ValueError, TypeError):

            return HttpResponse(
                400,
                {
                    "message": "Parâmetro building_id deve ser um número inteiro"
                }
            )

        try:

            result = self.__use_case.execute(building_id)

            return HttpResponse(
                200,
                {
                    "message": "Coordenadas obtidas com sucesso!",
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

        except RuntimeError as exc:

            return HttpResponse(
                502,
                {
                    "message": str(exc)
                }
            )
