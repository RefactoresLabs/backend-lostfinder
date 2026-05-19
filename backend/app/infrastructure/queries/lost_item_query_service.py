from sqlalchemy.orm import Session
from sqlalchemy import func


from backend.app.infrastructure.persistence.models.building_space_model import BuildingSpaceModel
from backend.app.infrastructure.persistence.models.category_model import CategoryModel
from backend.app.infrastructure.persistence.models.lost_item_model import LostItemModel
from backend.app.infrastructure.persistence.models.item_model import ItemModel
from backend.app.infrastructure.persistence.models.image_model import ImageModel
from backend.app.infrastructure.persistence.models.user_account_model import UserAccountModel

from backend.app.application.interfaces.lost_item_query_service_interface import LostItemQueryServiceInterface
from backend.app.application.queries.filters.list_items_summary_filters import ListItemsSummaryFilters
from backend.app.application.queries.sorts.list_items_summary_sort import ListItemsSummarySort
from backend.app.application.queries.sorts.enums.list_items_summary_sort_field import ListItemsSummarySortField
from backend.app.application.queries.sorts.enums.list_items_summary_sort_option import ListItemsSummarySortOption
from backend.app.application.queries.exceptions.invalid_sort_field_error import InvalidSortFieldError
from backend.app.application.queries.exceptions.sort_option_doesnt_exist_error import SortOptionDoesntExistError

from typing import Any


class LostItemQueryService(LostItemQueryServiceInterface):

    """Lida com transações mais específicas de item perdido"""

    def __init__(self, session: Session) -> None:

        """Inicializa os atributos de instância de LostItemQueryService

        Parameters
        ----------
        session: Session
            Sessão que lida com transações

        """

        self.__session = session

    def get_all_lost_items_summarized(self, filters: ListItemsSummaryFilters, sort: ListItemsSummarySort) -> list[dict[str, Any]]:

        """Obtém os dados resumidos das instâncias associadas a lost_item

        Parameters
        ----------
        filters: ListItemsSummaryFilters
            Filtros a serem aplicados na consulta
        
        sort: ListItemsSummarySort
            Ordenamento a ser aplicado na consulta

        Returns
        -------
        list[dict[str, any]]
            Iterável com dados resumidos de itens perdidos

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

        query = self.__session.query(
            ItemModel.id,
            ItemModel.name,
            UserAccountModel.name,
            CategoryModel.name,
            BuildingSpaceModel.name,
            ImageModel.url,
        ).join(
            LostItemModel,
            LostItemModel.id == ItemModel.id,
        ).join(
            UserAccountModel,
            UserAccountModel.id == ItemModel.user_id,
        ).join(
            CategoryModel,
            CategoryModel.id == ItemModel.category_id,
        ).join(
            BuildingSpaceModel,
            BuildingSpaceModel.id == LostItemModel.lost_space_id,
        ).outerjoin(
            subquery,
            subquery.c.item_id == ItemModel.id,
        ).outerjoin(
            ImageModel,
            ImageModel.id == subquery.c.min_image_id,
        )

        if filters.name is not None:

            query = query.filter(
                ItemModel.name.ilike(f"%{filters.name}%")
            )
        
        if filters.category_id is not None:

            query = query.filter(
                CategoryModel.id == filters.category_id
            )
        
        sortable_fields = {
            ListItemsSummarySortField.NAME: ItemModel.name
        }

        sort_column = sortable_fields.get(sort.sort_field)

        if sort_column:

            match sort.sort_option:

                case ListItemsSummarySortOption.ASC:

                    query = query.order_by(sort_column.asc())
                
                case ListItemsSummarySortOption.DESC:

                    query = query.order_by(sort_column.desc())
                
                case _:

                    raise SortOptionDoesntExistError("Essa opção de ordenamento não existe")

        else:

            raise InvalidSortFieldError("Não há como ordenar por esse campo")
        

        results = query.all()
        
        return [
            {
                "item_id": result[0],
                "item_name": result[1],
                "user_name": result[2],
                "category_name": result[3],
                "building_space_name": result[4],
                "image_url": result[5] if result[5] else ""
            }
        for result in results
        ]
    
    def get_lost_items_summarized_by_user_id(self, user_id: int) -> list[dict[str, Any]]:

        """Obtém os dados resumidos das instâncias associadas a lost_item de uma conta de usuário, através do ID desse usuário

        Parameters
        ----------
        user_id: int
            ID da conta de usuário pelo qual os itens perdidos associados serão obtidos
        
        Returns
        -------
        list[dict[str, any]]
            Iterável com dados resumidos de itens perdidos

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
            LostItemModel,
            LostItemModel.id == ItemModel.id,
        ).join(
            UserAccountModel,
            UserAccountModel.id == ItemModel.user_id,
        ).join(
            CategoryModel,
            CategoryModel.id == ItemModel.category_id,
        ).join(
            BuildingSpaceModel,
            BuildingSpaceModel.id == LostItemModel.lost_space_id,
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
                "image_url": result[5] if result[5] else ""
            }
        for result in results
        ]