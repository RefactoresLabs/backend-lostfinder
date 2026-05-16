from backend.app.domain.repositories.claim_repository_interface import ClaimRepositoryInterface
from backend.app.domain.entities.claim import Claim
from backend.app.domain.entities.found_item import FoundItem
from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.entities.building_space import BuildingSpace
from backend.app.domain.entities.building import Building
from backend.app.domain.entities.category import Category
from backend.app.domain.value_objects.localization import Localization
from backend.app.domain.value_objects.image import Image
from backend.app.domain.value_objects.claim_status import ClaimStatus

from backend.app.infrastructure.persistence.models.claim_model import ClaimModel
from backend.app.infrastructure.persistence.models.claim_status_model import ClaimStatusModel
from backend.app.infrastructure.persistence.models.user_account_model import UserAccountModel
from backend.app.infrastructure.persistence.models.item_model import ItemModel
from backend.app.infrastructure.persistence.models.found_item_model import FoundItemModel
from backend.app.infrastructure.persistence.models.building_space_model import BuildingSpaceModel
from backend.app.infrastructure.persistence.models.building_model import BuildingModel
from backend.app.infrastructure.persistence.models.localization_model import LocalizationModel
from backend.app.infrastructure.persistence.models.category_model import CategoryModel
from backend.app.infrastructure.persistence.models.image_model import ImageModel


from sqlalchemy.orm import Session, aliased


class ClaimRepository(ClaimRepositoryInterface):

    """Lida com as transações de persistência da entidade Claim"""

    def __init__(self, session: Session) -> None:

        """Inicializa os atributos de instância de ClaimRepository

        Parameters
        ----------
        session: Session
            Sessão que lida com as transações

        """

        self.__session = session
    
    def create_new_claim(self, claim: Claim) -> Claim | None:

        """Cria novas instâncias associadas a tabela claim

        Parameters
        ----------
        claim: Claim
            Objeto da entidade de negociação com os dados a serem armazenados
        
        Returns
        -------
        Claim | None
            Objeto da entidade de negociação com os dados armazenados

        """

        # Obtém o ID do status correspondente ao nome do status da negociação
        result = self.__session.query(
            ClaimStatusModel.id
        ).filter(
            ClaimStatusModel.name == claim.status.name
        ).first()

        if not result:

            return None
        
        claim_status_id = result[0]

        claim_model = ClaimModel(
            claimant_user_account_id=claim.claimant_user_account.id,
            associated_found_item_id=claim.associated_found_item.id,
            status_id=claim_status_id
        )

        self.__session.add(
            claim_model
        )
        self.__session.flush()

        claim._set_id(claim_model.id)
        claim._set_created_at(claim_model.created_at)

        return claim
    
    def update_claim(self, claim: Claim, claim_id: int) -> Claim:

        """Atualiza uma instância associada a tabela claim através do ID

        Parameters
        ----------
        claim: Claim
            Objeto da entidade de negociação com os dados a serem atualizados
        
        claim_id: int
            ID da negociação a ser atualizada
        
        Returns
        -------
        Claim
            Objeto da entidade de negociação com os dados atualizados

        """

        # Obtém o ID do status correspondente ao nome do status da negociação
        result = self.__session.query(
            ClaimStatusModel.id
        ).filter(
            ClaimStatusModel.name == claim.status.name
        ).first()

        if not result:

            return None
        
        claim_status_id = result[0]

        claim_updated_data = {
            "status_id": claim_status_id,
            "retrieval_code": claim.retrieval_code
        }

        self.__session.query(
            ClaimModel
        ).filter(
            ClaimModel.id == claim_id
        ).update(
            claim_updated_data
        )

        return claim
    
    def get_claim_by_id(self, claim_id: int) -> Claim | None:

        """Obtém uma instância associada a tabela claim através do ID

        Parameters
        ----------
        claim_id: int
            ID da negociação a ser obtida
        
        Returns
        -------
        Claim | None
            Objeto da entidade de negociação com os dados a serem obtidos

        """

        FoundItemUserAccount = aliased(UserAccountModel)
        ClaimantUserAccount = aliased(UserAccountModel)

        FoundSpace = aliased(BuildingSpaceModel)
        LeftSpace = aliased(BuildingSpaceModel)

        FoundBuilding = aliased(BuildingModel)
        LeftBuilding = aliased(BuildingModel)

        FoundLocalization = aliased(LocalizationModel)
        LeftLocalization = aliased(LocalizationModel)

        result = self.__session.query(
            ClaimModel,
            ClaimStatusModel,
            ClaimantUserAccount,
            ItemModel,
            FoundItemModel,
            CategoryModel,
            FoundItemUserAccount,
            FoundSpace, FoundBuilding, FoundLocalization,
            LeftSpace, LeftBuilding, LeftLocalization
        ).join(
            ClaimStatusModel,
            ClaimStatusModel.id == ClaimModel.status_id
        ).join(
            ClaimantUserAccount,
            ClaimantUserAccount.id == ClaimModel.claimant_user_account_id,
        ).join(
            ItemModel,
            ItemModel.id == ClaimModel.associated_found_item_id,
        ).join(
            FoundItemModel,
            FoundItemModel.id == ClaimModel.associated_found_item_id,
        ).join(
            CategoryModel,
            CategoryModel.id == ItemModel.category_id,
        ).join(
            FoundItemUserAccount,
            FoundItemUserAccount.id == ItemModel.user_id,
        ).join(
            FoundSpace,
            FoundSpace.id == FoundItemModel.found_space_id,
        ).join(
            FoundBuilding,
            FoundBuilding.id == FoundSpace.building_id,
        ).join(
            FoundLocalization,
            FoundLocalization.id == FoundBuilding.localization_id,
        ).join(
            LeftSpace,
            LeftSpace.id == FoundItemModel.left_space_id,
        ).join(
            LeftBuilding,
            LeftBuilding.id == LeftSpace.building_id,
        ).join(
            LeftLocalization,
            LeftLocalization.id == LeftBuilding.localization_id,
        ).filter(
            ClaimModel.id == claim_id
        ).first()

        if not result:

            return None
        
        (
            claim_model,
            claim_status_model,
            claimant_user_account_model,
            item_model,
            found_item_model,
            category_model,
            found_item_user_account_model,
            found_building_space_model,
            found_building_model,
            found_localization_model,
            left_building_space_model,
            left_building_model,
            left_localization_model,
        ) = result
        
        image_models = self.__session.query(
            ImageModel
        ).filter(
            ImageModel.item_id == item_model.id
        ).all()

        found_localization = Localization(
            cep=found_localization_model.cep,
            neighborhood=found_localization_model.neighborhood,
            street=found_localization_model.street,
        )

        found_building = Building(
            id=found_building_model.id,
            name=found_building_model.name,
            associated_localization=found_localization
        )

        found_building_space = BuildingSpace(
            id=found_building_space_model.id,
            name=found_building_space_model.name,
            associated_building=found_building
        )

        left_localization = Localization(
            cep=left_localization_model.cep,
            neighborhood=left_localization_model.neighborhood,
            street=left_localization_model.street,
        )

        left_building = Building(
            id=left_building_model.id,
            name=left_building_model.name,
            associated_localization=left_localization
        )

        left_building_space = BuildingSpace(
            id=left_building_space_model.id,
            name=left_building_space_model.name,
            associated_building=left_building
        )

        found_item_user_account = UserAccount(
            id=found_item_user_account_model.id,
            name=found_item_user_account_model.name,
            email=found_item_user_account_model.email,
            password=found_item_user_account_model.password,
            phone=found_item_user_account_model.phone
        )

        found_item = FoundItem(
            id=item_model.id,
            name=item_model.name,
            description=item_model.description,
            images=[
                Image(url=image_model.url)
                for image_model in image_models
            ],
            category=Category(
                id=category_model.id,
                name=category_model.name
            ),
            associated_user_account=found_item_user_account,
            approx_found_building_space=found_building_space,
            approx_left_building_space=left_building_space,
        )

        claimant_user_account = UserAccount(
            id=claimant_user_account_model.id,
            name=claimant_user_account_model.name,
            email=claimant_user_account_model.email,
            password=claimant_user_account_model.password,
            phone=claimant_user_account_model.phone,
        )

        status = ClaimStatus(name=claim_status_model.name)

        return Claim(
            id=claim_model.id,
            created_at=claim_model.created_at,
            claimant_user_account=claimant_user_account,
            associated_found_item=found_item,
            status=status,
            retrieval_code=claim_model.retrieval_code,
        )
    
    def delete_claim(self, claim_id: int) -> bool:

        """Remove as instâncias associadas a tabela claim pelo ID

        Parameters
        ----------
        claim_id: int
            ID da negociação
        
        Returns
        -------
        bool
            Retorna False, se nenhuma instância foi removida. Caso contrário, retorna True

        """
        
        rows_removed = self.__session.query(
            ClaimModel
        ).filter(
            ClaimModel.id == claim_id,
        ).delete(
            synchronize_session=False
        )

        return rows_removed > 0
    
    def check_retrieval_code_exists(self, retrieval_code: str) -> bool:

        """Verifica se existe uma instância associada a tabela claim com o código de recuperação passado

        Parameters
        ----------
        retrieval_code: str
            Código de recuperação a ser verificado
        
        Returns
        -------
        bool
            Retorna True, se o código já existir. Caso contrário, retorna False

        """

        claim_model = self.__session.query(
            ClaimModel
        ).filter(
            ClaimModel.retrieval_code == retrieval_code
        ).first()

        return claim_model is not None