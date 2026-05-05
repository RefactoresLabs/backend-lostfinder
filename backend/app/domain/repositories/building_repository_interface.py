from abc import ABC, abstractmethod

from backend.app.domain.entities.building import Building


class BuildingRepositoryInterface(ABC):

    """Interface do repositório da entidade Building"""

    @abstractmethod
    def get_building_by_id(self, id: int) -> Building | None:

        """Obtém uma entidade Building pelo seu identificador

        Parameters
        ----------
        id: int
            Identificador do prédio a ser buscado

        Returns
        -------
        Building | None
            Entidade prédio com os dados buscados, ou None se não encontrado

        """
        ...
