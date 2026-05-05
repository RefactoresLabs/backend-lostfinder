from sqlalchemy.orm import Session
from sqlalchemy import func


from backend.app.infrastructure.persistence.models.building_space_model import BuildingSpaceModel
from backend.app.infrastructure.persistence.models.category_model import CategoryModel
from backend.app.infrastructure.persistence.models.found_item_model import FoundItemModel
from backend.app.infrastructure.persistence.models.item_model import ItemModel
from backend.app.infrastructure.persistence.models.image_model import ImageModel
from backend.app.infrastructure.persistence.models.user_account_model import UserAccountModel

from backend.app.application.interfaces.found_item_query_service_interface import FoundItemQueryServiceInterface


from typing import Any


class FoundItemQueryService(FoundItemQueryServiceInterface):

    """Lida com transações mais específicas de item encontrado"""

    def __init__(self, session: Session) -> None:

        """Inicializa os atributos de instância de FoundItemQueryService

        Parameters
        ----------
        session: Session
            Sessão que lida com transações

        """

        self.__session = session

    def get_all_found_items_summarized(self) -> list[dict[str, Any]]:

        """Obtém os dados resumidos das instâncias associadas a found_item

        Returns
        -------
        list[dict[str, Any]]
            Iterável com dados resumidos de itens encontrados

        """

        # Agrega o ID do item associado a imagem pela imagem registrada primeiro (menor ID)
        subquery = (
            self.__session.query(
                ImageModel.item_id,
                func.min(ImageModel.id).label("min_image_id")
            ).group_by(
                ImageModel.item_id
            ).subquery()
        )

        results = self.__session.query(
            ItemModel.id,
            ItemModel.name,
            UserAccountModel.name,
            CategoryModel.name,
            BuildingSpaceModel.name,
            ImageModel.url,
        ).join(
            FoundItemModel,
            FoundItemModel.id == ItemModel.id,
        ).join(
            UserAccountModel,
            UserAccountModel.id == ItemModel.user_id,
        ).join(
            CategoryModel,
            CategoryModel.id == ItemModel.category_id,
        ).join(
            BuildingSpaceModel,
            BuildingSpaceModel.id == FoundItemModel.found_space_id,
        ).outerjoin(
            subquery,
            subquery.c.item_id == ItemModel.id,
        ).outerjoin(
            ImageModel,
            ImageModel.id == subquery.c.min_image_id,
        ).all()
        
        return [
            {
                "item_id": result[0],
                "item_name": result[1],
                "user_name": result[2],
                "category_name": result[3],
                "building_space_name": result[4],
                "image_url": result[5],
            }
        for result in results
        ]
    
    def get_found_items_summarized_by_user_id(self, user_id: int) -> list[dict[str, Any]]:
        
        """Obtém os dados resumidos das instâncias associadas a found_item de uma conta de usuário, através do ID desse usuário

        Parameters
        ----------
        user_id: int
            ID da conta de usuário pelo qual os itens encontrados associados serão obtidos

        Returns
        -------
        list[dict[str, Any]]
            Iterável com dados resumidos de itens encontrados

        """

        # Agrega o ID do item associado a imagem pela imagem registrada primeiro (menor ID)
        subquery = (
            self.__session.query(
                ImageModel.item_id,
                func.min(ImageModel.id).label("min_image_id")
            ).group_by(
                ImageModel.item_id
            ).subquery()
        )

        results = self.__session.query(
            ItemModel.id,
            ItemModel.name,
            UserAccountModel.name,
            CategoryModel.name,
            BuildingSpaceModel.name,
            ImageModel.url,
        ).join(
            FoundItemModel,
            FoundItemModel.id == ItemModel.id,
        ).join(
            UserAccountModel,
            UserAccountModel.id == ItemModel.user_id,
        ).join(
            CategoryModel,
            CategoryModel.id == ItemModel.category_id,
        ).join(
            BuildingSpaceModel,
            BuildingSpaceModel.id == FoundItemModel.found_space_id,
        ).outerjoin(
            subquery,
            subquery.c.item_id == ItemModel.id,
        ).outerjoin(
            ImageModel,
            ImageModel.id == subquery.c.min_image_id,
        ).filter(
            UserAccountModel.id == user_id,
        ).all()
        
        return [
            {
                "item_id": result[0],
                "item_name": result[1],
                "user_name": result[2],
                "category_name": result[3],
                "building_space_name": result[4],
                "image_url": result[5],
            }
        for result in results
        ]