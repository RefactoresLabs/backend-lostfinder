from backend.app.application.use_cases.list_categories_use_case import ListCategoriesUseCase

from backend.app.presentation.schemas.http_response import HttpResponse


class ListCategoriesController:

    """Ponto de acesso entre o endpoint e o caso de uso de listar categorias"""

    def __init__(self, use_case: ListCategoriesUseCase) -> None:

        """Inicializa os atributos de instância de ListCategoriesController

        Parameters
        ----------
        use_case: ListCategoriesUseCase
            Caso de uso de listar categorias

        """

        self.__use_case = use_case
    
    def handle(self) -> HttpResponse:

        """Lista as categorias do sistema
        
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