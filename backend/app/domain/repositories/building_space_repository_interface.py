from abc import ABC, abstractmethod

from backend.app.domain.entities.building_space import BuildingSpace


class BuildingSpaceRepositoryInterface(ABC):

    """Interface do repositório da entidade BuildingSpace"""

    @abstractmethod
    def get_building_space_by_id(self, id: int) -> BuildingSpace | None: ...
