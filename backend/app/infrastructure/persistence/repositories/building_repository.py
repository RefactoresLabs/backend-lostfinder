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
                    localization_model.cep,
                    localization_model.neighborhood,
                    localization_model.street,
                )
            )
            for building_model, localization_model in rows
        ]

    def get_buildind_by_id(self, id: int) -> Building | None:

        """Obtém os dados de uma instância associada a tabela building, através do ID

        Parameters
        ----------
        id: int
            ID do prédio cujos dados serão obtidos
        
        Returns
        -------
        Building | None:
            Objeto da Entidade Building

        """

        row = self.__session.query(
            BuildingModel,
            LocalizationModel
        ).join(
            LocalizationModel,
            LocalizationModel.id == BuildingModel.localization_id
        ).filter(
            BuildingModel.id == id
        ).first()

        if not row:

            return None
        
        building_model, localization_model = row
        
        return Building(
                id=building_model.id,
                name=building_model.name,
                associated_localization=Localization(
                    localization_model.cep,
                    localization_model.neighborhood,
                    localization_model.street,
                )
            )

