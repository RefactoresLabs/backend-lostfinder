from backend.app.domain.repositories.category_repository_interface import CategoryRepositoryInterface
from backend.app.domain.entities.category import Category

from backend.app.infrastructure.persistence.models.category_model import CategoryModel


from sqlalchemy.orm import Session


class CategoryRepository(CategoryRepositoryInterface):

    """Lida com as transações de persistência da entidade Category"""

    def __init__(self, session: Session) -> None:

        """Inicializa os atributos de instância de CategoryRepository

        Parameters
        ----------
        session: Session
            Sessão que lida com as transações

        """

        self.__session = session
    
    def get_all_categories(self) -> list[Category]:

        """Obtém todas as instâncias associadas a tabela category
        
        Returns
        -------
        list[Category]
            Iterável com objetos da entidade Category

        """

        category_models = self.__session.query(
            CategoryModel
        ).all()

        if not category_models:

            return []

        return [
            Category(
                id=category_model.id,
                name=category_model.name,
            )
            for category_model in category_models
        ]

    def get_category_by_id(self, id: int) -> Category | None:

        """Obtém os dados de instâncias associadas a tabela category pelo ID

        Parameters
        ----------
        id: int
            ID da categoria
        
        Returns
        -------
        Category
            Entidade categoria com os dados buscados

        """

        category_model = self.__session.query(CategoryModel).filter(
            CategoryModel.id == id,
        ).first()

        if not category_model:

            return None
        
        return Category(
            id=category_model.id,
            name=category_model.name,
        )