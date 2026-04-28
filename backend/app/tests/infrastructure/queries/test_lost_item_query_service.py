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
        lost_item1,
        lost_item2,
        lost_item3,
        image
    ])

    session.commit()   

def test_get_all_lost_item_summarized_success(session: Session, seed_data):

    query_service = LostItemQueryService(session)

    lost_items_summarized = query_service.get_all_lost_items_summarized()

    assert len(lost_items_summarized) == 3
    assert lost_items_summarized[0]["item_name"] == "Lápis"
    assert lost_items_summarized[1]["building_space_name"] == "sala 2"
    assert lost_items_summarized[2]["image_url"] is None
