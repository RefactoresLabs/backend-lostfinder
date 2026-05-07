from backend.app.infrastructure.persistence.repositories.category_repository import CategoryRepository

from backend.app.application.use_cases.list_categories_use_case import ListCategoriesUseCase

from backend.app.presentation.controllers.list_categories_controller import ListCategoriesController


from sqlalchemy.orm import Session


def make_list_categories_controller(session: Session) -> ListCategoriesController:

    """Factory function que cria um objeto ListCategoriesController

    Parameters
    ----------
    session: Session
        Sessão usada nas transações com o banco de dados
    
    Returns
    -------
    ListCategoriesController
        Ponto de acesso entre o endpoint e o caso de uso de listar categorias

    """

    repository = CategoryRepository(session)

    use_case = ListCategoriesUseCase(repository)

    return ListCategoriesController(use_case)