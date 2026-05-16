from abc import ABC, abstractmethod

from backend.app.domain.entities.building import Building


class BuildingRepositoryInterface(ABC):

    """Interface do repositório da entidade Building"""

    @abstractmethod
    def get_all_buildings(self) -> list[Building]: ...

    @abstractmethod
    def get_building_by_id(self, id: int) -> Building | None: ...
