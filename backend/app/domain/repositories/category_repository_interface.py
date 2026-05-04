from abc import ABC, abstractmethod


from backend.app.domain.entities.category import Category


class CategoryRepositoryInterface(ABC):

    """Interface do repositório da entidade Category"""

    @abstractmethod
    def get_all_categories(self) -> list[Category]: ...

    @abstractmethod
    def get_category_by_id(self, id: int) -> Category | None: ...