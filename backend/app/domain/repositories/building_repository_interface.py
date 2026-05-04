from abc import ABC, abstractmethod


from backend.app.domain.entities.building import Building


class BuildingRepositoryInterface:

    """Interface do repositório da entidade Building"""

    @abstractmethod
    def get_all_buildings(self) -> list[Building]: ...

    @abstractmethod
    def get_buildind_by_id(self, id: int) -> Building | None: ...