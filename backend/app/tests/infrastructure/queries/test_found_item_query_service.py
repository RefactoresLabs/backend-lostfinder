import pytest


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


from backend.app.infrastructure.queries.found_item_query_service import FoundItemQueryService
from backend.app.infrastructure.persistence.models.building_model import BuildingModel
from backend.app.infrastructure.persistence.models.building_space_model import BuildingSpaceModel
from backend.app.infrastructure.persistence.models.category_model import CategoryModel
from backend.app.infrastructure.persistence.models.localization_model import LocalizationModel
from backend.app.infrastructure.persistence.models.user_account_model import UserAccountModel
from backend.app.infrastructure.persistence.models.image_model import ImageModel
from backend.app.infrastructure.persistence.models.found_item_model import FoundItemModel
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

    found_item1 = FoundItemModel(
        id=1,
        found_space_id=1,
        left_space_id=2,
    )

    found_item2 = FoundItemModel(
        id=2,
        found_space_id=2,
        left_space_id=2,
    )

    found_item3 = FoundItemModel(
        id=3,
        found_space_id=3,
        left_space_id=3,
    )

    found_item4 = FoundItemModel(
        id=4,
        found_space_id=3,
        left_space_id=3,
    )
    
    found_item5 = FoundItemModel(
        id=5,
        found_space_id=3,
        left_space_id=3,
    )

    found_item6 = FoundItemModel(
        id=6,
        found_space_id=3,
        left_space_id=3,
    )

    found_item7 = FoundItemModel(
        id=7,
        found_space_id=3,
        left_space_id=3,
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
        found_item1,
        found_item2,
        found_item3,
        found_item4,
        found_item5,
        found_item6,
        found_item7,
        image
    ])

    session.commit()   

def test_get_all_found_item_summarized_success(session: Session, seed_data):

    query_service = FoundItemQueryService(session)

    filters = ListItemsSummaryFilters(None, None)
    sort = ListItemsSummarySort(ListItemsSummarySortField.NAME, ListItemsSummarySortOption.ASC)

    found_items_summarized = query_service.get_all_found_items_summarized(filters, sort)

    assert len(found_items_summarized) == 7
    assert found_items_summarized[0]["item_name"] == "Borracha"
    assert found_items_summarized[1]["item_name"] == "Borracha"

def test_get_all_found_items_summarized_filter_name(session: Session, seed_data):

    query_service = FoundItemQueryService(session)

    filters = ListItemsSummaryFilters("Borracha", None)
    sort = ListItemsSummarySort(ListItemsSummarySortField.NAME, ListItemsSummarySortOption.ASC)

    found_items_summarized = query_service.get_all_found_items_summarized(filters, sort)

    assert len(found_items_summarized) == 3
    assert found_items_summarized[0]["item_name"] == "Borracha"
    assert found_items_summarized[1]["item_name"] == "Borracha"

def test_get_all_found_items_summarized_filter_category_id(session: Session, seed_data):

    query_service = FoundItemQueryService(session)

    filters = ListItemsSummaryFilters(None, 1)
    sort = ListItemsSummarySort(ListItemsSummarySortField.NAME, ListItemsSummarySortOption.ASC)

    found_items_summarized = query_service.get_all_found_items_summarized(filters, sort)

    assert len(found_items_summarized) == 3
    assert found_items_summarized[0]["item_name"] == "Borracha"
    assert found_items_summarized[1]["item_name"] == "Carteira"
    assert found_items_summarized[2]["item_name"] == "Fone"

def test_get_all_found_items_summarized_filter_name_and_category_id(session: Session, seed_data):

    query_service = FoundItemQueryService(session)

    filters = ListItemsSummaryFilters("Borracha", 1)
    sort = ListItemsSummarySort(ListItemsSummarySortField.NAME, ListItemsSummarySortOption.ASC)

    found_items_summarized = query_service.get_all_found_items_summarized(filters, sort)

    assert len(found_items_summarized) == 1
    assert found_items_summarized[0]["item_name"] == "Borracha"

def test_get_all_found_items_summarized_name_desc_sort_option(session: Session, seed_data):

    query_service = FoundItemQueryService(session)

    filters = ListItemsSummaryFilters(None, None)
    sort = ListItemsSummarySort(ListItemsSummarySortField.NAME, ListItemsSummarySortOption.DESC)

    found_items_summarized = query_service.get_all_found_items_summarized(filters, sort)

    assert len(found_items_summarized) == 7
    assert found_items_summarized[0]["item_name"] == "Lápis"

def test_get_found_items_summarized_by_user_id_success(session: Session, seed_data):

    query_service = FoundItemQueryService(session)

    found_items_summarized = query_service.get_found_items_summarized_by_user_id(1)

    assert found_items_summarized[0]["item_name"] == "Lápis"
    assert found_items_summarized[0]["user_name"] == "teste"
    assert found_items_summarized[1]["user_name"] == "teste"