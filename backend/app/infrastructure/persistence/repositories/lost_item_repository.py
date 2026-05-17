from backend.app.domain.repositories.lost_item_repository_interface import LostItemRepositoryInterface

from backend.app.domain.entities.lost_item import LostItem
from backend.app.domain.entities.category import Category
from backend.app.domain.entities.building_space import BuildingSpace
from backend.app.domain.entities.building import Building
from backend.app.domain.entities.user_account import UserAccount

from backend.app.domain.value_objects.localization import Localization
from backend.app.domain.value_objects.image import Image

from backend.app.infrastructure.persistence.models.lost_item_model import LostItemModel
from backend.app.infrastructure.persistence.models.item_model import ItemModel
from backend.app.infrastructure.persistence.models.category_model import CategoryModel
from backend.app.infrastructure.persistence.models.building_space_model import BuildingSpaceModel
from backend.app.infrastructure.persistence.models.image_model import ImageModel
from backend.app.infrastructure.persistence.models.building_model import BuildingModel
from backend.app.infrastructure.persistence.models.localization_model import LocalizationModel
from backend.app.infrastructure.persistence.models.user_account_model import UserAccountModel


from sqlalchemy.orm import Session


class LostItemRepository(LostItemRepositoryInterface):

    """Lida com as transações de persistência da entidade LostItem"""

    def __init__(self, session: Session) -> None:

        """Inicializa os atributos de instância de LostItemRepository

        Parameters
        ----------
        session: Session
            Sessão atual que lida com as transações

        """

        self.__session = session

    def create_new_lost_item(self, lost_item: LostItem) -> LostItem:

        """Cria novas instâncias associadas a tabela lost_item

        Parameters
        ----------
        lost_item: LostItem
            Objeto da entidade item perdido com os dados a serem armazenados
        
        Returns
        -------
        LostItem
            Objeto da entidade item perdido com os dados armazenados

        """
        
        # Insere nova instância de item
        item_model = ItemModel(
            name=lost_item.name,
            description=lost_item.description,
            category_id=lost_item.category.id,
            user_id=lost_item.associated_user_account.id,
        )

        self.__session.add(item_model)
        self.__session.flush() # Envia as transações para o banco, sem commitar, para obter o id do item

        # Insere nova instância de lost_item
        lost_item_model = LostItemModel(
            id=item_model.id,
            lost_space_id=lost_item.approx_lost_building_space.id,
        )

        self.__session.add(lost_item_model)

        # Insere nova instância de image
        for image in lost_item.images:

            image_model = ImageModel(
                url=image.url,
                item_id=item_model.id
            )

            self.__session.add(image_model)
        
        lost_item._set_id(item_model.id)

        return lost_item
    
    def update_lost_item(self, lost_item: LostItem, id: int) -> LostItem:

        """Atualiza as instâncias associadas a tabela lost_item através do ID

        Parameters
        ----------
        lost_item: LostItem
            Objeto da entidade item perdido com os dados a serem modificados
        
        id: int
            ID do item perdido a ser atualizado

        Returns
        -------
        LostItem
            Objeto da entidade item perdido com os dados atualizados
        
        """

        item_updated_data = {
            "name": lost_item.name,
            "description": lost_item.description,
            "category_id": lost_item.category.id,
        }

        lost_item_updated_data = {
            "lost_space_id": lost_item.approx_lost_building_space.id,
        }

        self.__session.query(ItemModel).filter(
            ItemModel.id == id
        ).update(
            item_updated_data,
            synchronize_session=False # Evita chamada de SELECT antes do UPDATE   
        )

        self.__session.query(LostItemModel).filter(
            LostItemModel.id == id
        ).update(
            lost_item_updated_data,
            synchronize_session=False, # Evita chamada de SELECT antes do UPDATE
        )

        # Atualização das imagens (Remover e depois inserir)
        self.__session.query(ImageModel).filter(
            ImageModel.item_id == id
        ).delete()

        for image in lost_item.images:

            image_model = ImageModel(
                url=image.url
            )

            self.__session.add(image_model)

        return lost_item
    
    def get_lost_item_by_id(self, id: int) -> LostItem | None:
        
        """Obtém dados associados a uma instância da tabela lost_item através do ID

        Parameters
        ----------
        id: int
            ID do item perdido a ser obtido

        Returns
        -------
        LosItem | None
            Objeto da entidade item perdido com os dados buscados
        
        """

        result = self.__session.query(
            ItemModel, LostItemModel,
            CategoryModel, BuildingSpaceModel,
            BuildingModel, LocalizationModel,
            UserAccountModel
        ).join(
            LostItemModel,
            LostItemModel.id == ItemModel.id,
        ).join(
            CategoryModel,
            CategoryModel.id == ItemModel.category_id,
        ).join(
            BuildingSpaceModel,
            BuildingSpaceModel.id == LostItemModel.lost_space_id,
        ).join(
            BuildingModel,
            BuildingModel.id == BuildingSpaceModel.building_id,
        ).join(
            LocalizationModel,
            LocalizationModel.id == BuildingModel.localization_id,
        ).join(
            UserAccountModel,
            UserAccountModel.id == ItemModel.user_id,
        ).filter(
            ItemModel.id == id
        ).first()

        if not result:

            return None

        image_models = self.__session.query(ImageModel).filter(
            ImageModel.item_id == id
        ).all()

        item_model, lost_item_model, category_model, building_space_model, building_model, localization_model, user_account_model = result

        category = Category(
            category_model.id,
            category_model.name,
        )

        localization = Localization(
            cep=localization_model.cep,
            neighborhood=localization_model.neighborhood,
            street=localization_model.street,
        )

        building = Building(
            id=building_model.id,
            name=building_model.name,
            associated_localization=localization
        )

        building_space = BuildingSpace(
            id=building_space_model.id,
            name=building_space_model.name,
            associated_building=building
        )

        user_account = UserAccount(
            id=user_account_model.id,
            name=user_account_model.name,
            email=user_account_model.email,
            password=user_account_model.password,
            phone=user_account_model.phone,
            score=user_account_model.score,
        )

        return LostItem(
            id=lost_item_model.id,
            name=item_model.name,
            description=item_model.description,
            images = [Image(url=image_model.url) for image_model in image_models],
            registration_date=item_model.registration_date,
            category=category,
            approx_lost_building_space=building_space,
            associated_user_account=user_account,
        )
    
    def delete_lost_item(self, id: int) -> bool:

        """Remove as instâncias associadas a tabela lost_item pelo ID

        Parameters
        ----------
        id: int
            ID do item perdido a ser removido
        
        Returns
        -------
        bool
            Retorna False, se nenhuma instância foi removida. Caso contrário, retorna True

        """

        # Remoção de lost_item antes para evitar inconsistência

        self.__session.query(LostItemModel).filter(
            LostItemModel.id == id
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




