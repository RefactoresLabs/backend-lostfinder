from backend.app.domain.repositories.found_item_repository_interface import FoundItemRepositoryInterface

from backend.app.domain.entities.found_item import FoundItem
from backend.app.domain.entities.category import Category
from backend.app.domain.entities.building_space import BuildingSpace
from backend.app.domain.entities.building import Building
from backend.app.domain.entities.user_account import UserAccount

from backend.app.domain.value_objects.localization import Localization
from backend.app.domain.value_objects.image import Image

from backend.app.infrastructure.persistence.models.found_item_model import FoundItemModel
from backend.app.infrastructure.persistence.models.item_model import ItemModel
from backend.app.infrastructure.persistence.models.category_model import CategoryModel
from backend.app.infrastructure.persistence.models.building_space_model import BuildingSpaceModel
from backend.app.infrastructure.persistence.models.image_model import ImageModel
from backend.app.infrastructure.persistence.models.building_model import BuildingModel
from backend.app.infrastructure.persistence.models.localization_model import LocalizationModel
from backend.app.infrastructure.persistence.models.user_account_model import UserAccountModel


from sqlalchemy.orm import Session
from sqlalchemy.orm import aliased


class FoundItemRepository(FoundItemRepositoryInterface):

    """Lida com as transações de persistência da entidade FoundItem"""

    def __init__(self, session: Session) -> None:

        """Inicializa os atributos de instância de FoundItemRepository

        Parameters
        ----------
        session: Session
            Sessão atual que lida com as transações

        """

        self.__session = session

    def create_new_found_item(self, found_item: FoundItem) -> FoundItem | None:

        """Cria novas instâncias associadas a tabela found_item

        Parameters
        ----------
        found_item: FoundItem
            Objeto da entidade item encontrado com os dados a serem armazenados
        
        Returns
        -------
        FoundItem | None
            Objeto da entidade item encontrado com os dados armazenados

        """
        
        # Insere nova instância de item
        item_model = ItemModel(
            name=found_item.name,
            description=found_item.description,
            category_id=found_item.category.id,
            user_id=found_item.associated_user_account.id,
        )

        self.__session.add(item_model)
        self.__session.flush() # Envia as transações para o banco, sem commitar, para obter o id do item

        # Insere nova instância de found_item
        found_item_model = FoundItemModel(
            id=item_model.id,
            found_space_id=found_item.approx_found_building_space.id,
            left_space_id=found_item.approx_left_building_space.id,
        )

        self.__session.add(found_item_model)

        # Insere nova instância de image
        for image in found_item.images:

            image_model = ImageModel(
                url=image.url,
                item_id=item_model.id
            )

            self.__session.add(image_model)
        
        found_item._set_id(item_model.id)

        return found_item
    
    def update_found_item(self, found_item: FoundItem, id: int) -> FoundItem:

        """Atualiza as instâncias associadas a tabela found_item através do ID

        Parameters
        ----------
        found_item: FoundItem
            Objeto da entidade item encontrado com os dados a serem modificados
        
        id: int
            ID do item encontrado a ser atualizado

        Returns
        -------
        LostItem
            Objeto da entidade item encontrado com os dados atualizados
        
        """

        item_updated_data = {
            "name": found_item.name,
            "description": found_item.description,
            "category_id": found_item.category.id,
        }

        found_item_updated_data = {
            "found_space_id": found_item.approx_found_building_space.id,
            "left_space_id": found_item.approx_left_building_space.id,
        }

        self.__session.query(ItemModel).filter(
            ItemModel.id == id
        ).update(
            item_updated_data,
            synchronize_session=False # Evita chamada de SELECT antes do UPDATE   
        )

        self.__session.query(FoundItemModel).filter(
            FoundItemModel.id == id
        ).update(
            found_item_updated_data,
            synchronize_session=False, # Evita chamada de SELECT antes do UPDATE
        )

        # Atualização das imagens (Remover e depois inserir)
        self.__session.query(ImageModel).filter(
            ImageModel.item_id == id
        ).delete()

        for image in found_item.images:

            image_model = ImageModel(
                url=image.url
            )

            self.__session.add(image_model)

        return found_item
    
    def get_found_item_by_id(self, id: int) -> FoundItem | None:
        
        """Obtém dados associados a uma instância da tabela found_item através do ID

        Parameters
        ----------
        id: int
            ID do item encontrado a ser obtido

        Returns
        -------
        FoundItem | None
            Objeto da entidade item encontrado com os dados buscados
        
        """
        
        FoundSpace = aliased(BuildingSpaceModel)
        LeftSpace = aliased(BuildingSpaceModel)

        FoundBuilding = aliased(BuildingModel)
        LeftBuilding = aliased(BuildingModel)

        FoundLocalization = aliased(LocalizationModel)
        LeftLocalization = aliased(LocalizationModel)

        result = self.__session.query(
            ItemModel, FoundItemModel, CategoryModel, UserAccountModel, 
            FoundSpace, FoundBuilding, FoundLocalization,
            LeftSpace, LeftBuilding, LeftLocalization,
        ).join(
            FoundItemModel,
            FoundItemModel.id == ItemModel.id,
        ).join(
            CategoryModel,
            CategoryModel.id == ItemModel.category_id,
        ).join(
            UserAccountModel,
            UserAccountModel.id == ItemModel.user_id,
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
            ItemModel.id == id
        ).first()

        if not result:

            return None

        image_models = self.__session.query(ImageModel).filter(
            ImageModel.item_id == id
        ).all()

        (
            item_model, 
            found_item_model, 
            category_model, 
            user_account_model, 
            
            found_building_space_model, 
            found_building_model, 
            found_localization_model, 
            
            left_building_space_model, 
            left_building_model, 
            left_localization_model,
         ) = result

        category = Category(
            category_model.id,
            category_model.name,
        )

        user_account = UserAccount(
            id=user_account_model.id,
            name=user_account_model.name,
            email=user_account_model.email,
            password=user_account_model.password,
            phone=user_account_model.phone,
            score=user_account_model.score,
        )

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

        return FoundItem(
            id=found_item_model.id,
            name=item_model.name,
            description=item_model.description,
            images = [Image(url=image_model.url) for image_model in image_models],
            registration_date=item_model.registration_date,
            category=category,
            associated_user_account=user_account,
            approx_found_building_space=found_building_space,
            approx_left_building_space=left_building_space,
        )
    
    def delete_found_item(self, id: int) -> bool:

        """Remove as instâncias associadas a tabela found_item pelo ID

        Parameters
        ----------
        id: int
            ID do item encontrado a ser removido
        
        Returns
        -------
        bool
            Retorna False, se nenhuma instância foi removida. Caso contrário, retorna True

        """

        # Remoção de foubd_item antes para evitar inconsistência

        self.__session.query(FoundItemModel).filter(
            FoundItemModel.id == id
        ).delete(
            synchronize_session=False
        )

        rows_removed = self.__session.query(ItemModel).filter(
            ItemModel.id == id
        ).delete(
            synchronize_session=False
        )

        # Imagens serão removidas por cascata

        return rows_removed > 0