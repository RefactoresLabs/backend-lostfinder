from backend.app.domain.repositories.building_repository_interface import BuildingRepositoryInterface
from backend.app.domain.entities.building import Building
from backend.app.domain.value_objects.localization import Localization

from backend.app.infrastructure.persistence.models.building_model import BuildingModel
from backend.app.infrastructure.persistence.models.localization_model import LocalizationModel

from sqlalchemy.orm import Session


class BuildingRepository(BuildingRepositoryInterface):

    """Lida com as transações de persistência da entidade Building"""

    def __init__(self, session: Session) -> None:

        """Inicializa os atributos de instância de BuildingRepository

        Parameters
        ----------
        session: Session
            Sessão atual que lida com as transações

        """

        self.__session = session

    def get_all_buildings(self) -> list[Building]:
        
        """Obtém todas as instâncias associadas a tabela building

        Returns
        -------
        list[Building]
            Iterável com objetos da entidade Building

        """

        rows = self.__session.query(
            BuildingModel, LocalizationModel
        ).join(
            LocalizationModel,
            LocalizationModel.id == BuildingModel.localization_id,
        ).all()

        if not rows:

            return []
        
        return [
            Building(
                id=building_model.id,
                name=building_model.name,
                associated_localization=Localization(
                    cep=localization_model.cep,
                    neighborhood=localization_model.neighborhood,
                    street=localization_model.street,
                )
            )
            for building_model, localization_model in rows
        ]

    def get_building_by_id(self, id: int) -> Building | None:

        """Obtém dados associados a uma instância da tabela building pelo ID

        Parameters
        ----------
        id: int
            ID do prédio a ser obtido

        Returns
        -------
        Building | None
            Entidade prédio com os dados buscados, ou None se não encontrado

        """

        result = self.__session.query(
            BuildingModel, LocalizationModel
        ).join(
            LocalizationModel,
            LocalizationModel.id == BuildingModel.localization_id,
        ).filter(
            BuildingModel.id == id
        ).first()

        if not result:

            return None

        building_model, localization_model = result

        localization = Localization(
            cep=localization_model.cep,
            neighborhood=localization_model.neighborhood,
            street=localization_model.street,
        )

        return Building(
            id=building_model.id,
            name=building_model.name,
            associated_localization=localization,
        )
