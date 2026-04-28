from backend.app.domain.repositories.building_space_repository_interface import BuildingSpaceRepositoryInterface
from backend.app.domain.entities.building_space import BuildingSpace
from backend.app.domain.entities.building import Building
from backend.app.domain.value_objects.localization import Localization

from backend.app.infrastructure.persistence.models.building_space_model import BuildingSpaceModel
from backend.app.infrastructure.persistence.models.building_model import BuildingModel
from backend.app.infrastructure.persistence.models.localization_model import LocalizationModel

from sqlalchemy.orm import Session


class BuildingSpaceRepository(BuildingSpaceRepositoryInterface):

    """Lida com as transações de persistência da entidade BuildingSpace"""

    def __init__(self, session: Session) -> None:

        """Inicializa os atributos de instância de BuildingSpaceRepository

        Parameters
        ----------
        session: Session
            Sessão atual que lida com as transações

        """

        self.__session = session

    def get_building_space_by_id(self, id: int) -> BuildingSpace | None:

        """Obtém dados associados a uma instância da tabela building_space pelo ID

        Parameters
        ----------
        id: int
            ID do espaço do prédio a ser obtido

        Returns
        -------
        BuildingSpace | None
            Entidade espaço do prédio com os dados buscados, ou None se não encontrado

        """

        result = self.__session.query(
            BuildingSpaceModel, BuildingModel, LocalizationModel
        ).join(
            BuildingModel,
            BuildingModel.id == BuildingSpaceModel.building_id,
        ).join(
            LocalizationModel,
            LocalizationModel.id == BuildingModel.localization_id,
        ).filter(
            BuildingSpaceModel.id == id
        ).first()

        if not result:

            return None

        building_space_model, building_model, localization_model = result

        localization = Localization(
            cep=localization_model.cep,
            neighborhood=localization_model.neighborhood,
            street=localization_model.street,
        )

        building = Building(
            id=building_model.id,
            name=building_model.name,
            associated_localization=localization,
        )

        return BuildingSpace(
            id=building_space_model.id,
            name=building_space_model.name,
            associated_building=building,
        )
