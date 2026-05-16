from backend.app.domain.repositories.category_repository_interface import CategoryRepositoryInterface

from backend.app.application.dtos.list_categories_dto import ListCategoriesDTO

class ListCategoriesUseCase:

    """Representa um caso de uso de listar categorias"""

    def __init__(self, category_repository: CategoryRepositoryInterface) -> None:

        """Inicializa os atributos de instância de ListCategoriesUseCase

        Parameters
        ----------
        category_repository: CategoryRepositoryInterface
            Repositório de categorias para busca de dados

        """

        self.__repository = category_repository
    
    def execute(self) -> list[ListCategoriesDTO]:

        """Executa o fluxo de eventos do caso de uso

        Returns
        -------
        ListCategoriesDTO
            Objetos de transferência de dados com os dados de cada categoria

        """

        categories = self.__repository.get_all_categories()

        return [
            ListCategoriesDTO(
                id=category.id,
                name=category.name,
            )
            for category in categories
        ]