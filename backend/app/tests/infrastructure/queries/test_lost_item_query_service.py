import pytest


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


from backend.app.infrastructure.queries.lost_item_query_service import LostItemQueryService
from backend.app.infrastructure.persistence.models.building_model import BuildingModel
from backend.app.infrastructure.persistence.models.building_space_model import BuildingSpaceModel
from backend.app.infrastructure.persistence.models.category_model import CategoryModel
from backend.app.infrastructure.persistence.models.localization_model import LocalizationModel
from backend.app.infrastructure.persistence.models.user_account_model import UserAccountModel
from backend.app.infrastructure.persistence.models.image_model import ImageModel
from backend.app.infrastructure.persistence.models.lost_item_model import LostItemModel
from backend.app.infrastructure.persistence.models.item_model import ItemModel
from backend.app.infrastructure.persistence.models.base import Base

from backend.app.application.queries.filters.list_items_summary_filters import ListItemsSummaryFilters
from backend.app.application.queries.sorts.list_items_summary_sort import ListItemsSummarySort
from backend.app.application.queries.sorts.enums.list_items_summary_sort_field import ListItemsSummarySortField
from backend.app.application.queries.sorts.enums.list_items_summary_sort_option import ListItemsSummarySortOption


@pytest.fixture
def session():

    """Simula uma sessão a um banco em memória
    """

    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()

@pytest.fixture
def seed_data(session: Session):

    """Simula a criação de dados no banco em memória
    """

    localization = LocalizationModel(
        id=1,
        cep="11111111",
        neighborhood="bairro 1",
        street="rua 1"
    )

    building = BuildingModel(
        id=1,
        name="predio 1",
        localization_id=1
    )

    building_space1 = BuildingSpaceModel(
        id=1,
        name="sala 1",
        building_id=1
    )

    building_space2 = BuildingSpaceModel(
        id=2,
        name="sala 2",
        building_id=1
    )

    building_space3 = BuildingSpaceModel(
        id=3,
        name="sala 3",
        building_id=1
    )

    category1 = CategoryModel(
        id=1,
        name="Acessório Pessoal"
    )

    category2 = CategoryModel(
        id=2,
        name="Material"
    )

    user = UserAccountModel(
        id=1,
        name="teste",
        email="teste@email.com",
        password="1234",
        phone="1111"
    )

    item1 = ItemModel(
        id=1,
        name="Lápis",
        description="Lápis preto faber castel",
        category_id=2,
        user_id=1,
    )

    item2 = ItemModel(
        id=2,
        name="Caneta",
        description="Caneta preta",
        category_id=2,
        user_id=1,
    )

    item3 = ItemModel(
        id=3,
        name="Borracha",
        description="Borracha laranja e azul",
        category_id=2,
        user_id=1,
    )

    item4 = ItemModel(
        id=4,
        name="Borracha",
        description="Borracha branca",
        category_id=2,
        user_id=1,
    )

    item5 = ItemModel(
        id=5,
        name="Carteira",
        description="Carteira Preta",
        category_id=1,
        user_id=1,
    )

    item6 = ItemModel(
        id=6,
        name="Fone",
        description="Fone JBL Branco",
        category_id=1,
        user_id=1,
    )

    item7 = ItemModel(
        id=7,
        name="Borracha",
        description="Borracha preta",
        category_id=1,
        user_id=1,
    )

    lost_item1 = LostItemModel(
        id=1,
        lost_space_id=1,
    )

    lost_item2 = LostItemModel(
        id=2,
        lost_space_id=2,
    )

    lost_item3 = LostItemModel(
        id=3,
        lost_space_id=3,
    )

    lost_item4 = LostItemModel(
        id=4,
        lost_space_id=3,
    )
    
    lost_item5 = LostItemModel(
        id=5,
        lost_space_id=3,
    )

    lost_item6 = LostItemModel(
        id=6,
        lost_space_id=3,
    )

    lost_item7 = LostItemModel(
        id=7,
        lost_space_id=3,
    )

    image = ImageModel(
        id=1,
        url="./image1.png",
        item_id=1,
    )

    session.add_all([
        localization,
        building,
        building_space1,
        building_space2,
        building_space3,
        category1,
        category2,
        user,
        item1,
        item2,
        item3,
        item4,
        item5,
        item6,
        item7,
        lost_item1,
        lost_item2,
        lost_item3,
        lost_item4,
        lost_item5,
        lost_item6,
        lost_item7,
        image
    ])

    session.commit()   

def test_get_all_lost_item_summarized_success(session: Session, seed_data):

    query_service = LostItemQueryService(session)

    filters = ListItemsSummaryFilters(None, None)
    sort = ListItemsSummarySort(ListItemsSummarySortField.NAME, ListItemsSummarySortOption.ASC)

    lost_items_summarized = query_service.get_all_lost_items_summarized(filters, sort)

    assert len(lost_items_summarized) == 7
    assert lost_items_summarized[0]["item_name"] == "Borracha"
    assert lost_items_summarized[1]["item_name"] == "Borracha"

def test_get_all_lost_items_summarized_filter_name(session: Session, seed_data):

    query_service = LostItemQueryService(session)

    filters = ListItemsSummaryFilters("Borracha", None)
    sort = ListItemsSummarySort(ListItemsSummarySortField.NAME, ListItemsSummarySortOption.ASC)

    lost_items_summarized = query_service.get_all_lost_items_summarized(filters, sort)

    assert len(lost_items_summarized) == 3
    assert lost_items_summarized[0]["item_name"] == "Borracha"
    assert lost_items_summarized[1]["item_name"] == "Borracha"

def test_get_all_lost_items_summarized_filter_category_id(session: Session, seed_data):

    query_service = LostItemQueryService(session)

    filters = ListItemsSummaryFilters(None, 1)
    sort = ListItemsSummarySort(ListItemsSummarySortField.NAME, ListItemsSummarySortOption.ASC)

    lost_items_summarized = query_service.get_all_lost_items_summarized(filters, sort)

    assert len(lost_items_summarized) == 3
    assert lost_items_summarized[0]["item_name"] == "Borracha"
    assert lost_items_summarized[1]["item_name"] == "Carteira"
    assert lost_items_summarized[2]["item_name"] == "Fone"

def test_get_all_lost_items_summarized_filter_name_and_category_id(session: Session, seed_data):

    query_service = LostItemQueryService(session)

    filters = ListItemsSummaryFilters("Borracha", 1)
    sort = ListItemsSummarySort(ListItemsSummarySortField.NAME, ListItemsSummarySortOption.ASC)

    lost_items_summarized = query_service.get_all_lost_items_summarized(filters, sort)
    
    assert len(lost_items_summarized) == 1
    assert lost_items_summarized[0]["item_name"] == "Borracha"

def test_get_all_lost_items_summarized_name_desc_sort_option(session: Session, seed_data):

    query_service = LostItemQueryService(session)

    filters = ListItemsSummaryFilters(None, None)
    sort = ListItemsSummarySort(ListItemsSummarySortField.NAME, ListItemsSummarySortOption.DESC)

    lost_items_summarized = query_service.get_all_lost_items_summarized(filters, sort)

    assert len(lost_items_summarized) == 7
    assert lost_items_summarized[0]["item_name"] == "Lápis"

def test_get_lost_items_summarized_by_user_id_success(session: Session, seed_data):

    query_service = LostItemQueryService(session)

    lost_items_summarized = query_service.get_lost_items_summarized_by_user_id(1)

    assert lost_items_summarized[0]["item_name"] == "Lápis"
    assert lost_items_summarized[0]["user_name"] == "teste"
    assert lost_items_summarized[1]["user_name"] == "teste"
