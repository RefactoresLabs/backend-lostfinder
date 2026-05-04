import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from backend.app.infrastructure.persistence.models.base import Base
from backend.app.infrastructure.persistence.repositories.found_item_repository import FoundItemRepository
from backend.app.infrastructure.persistence.models.building_model import BuildingModel
from backend.app.infrastructure.persistence.models.building_space_model import BuildingSpaceModel
from backend.app.infrastructure.persistence.models.category_model import CategoryModel
from backend.app.infrastructure.persistence.models.localization_model import LocalizationModel
from backend.app.infrastructure.persistence.models.user_account_model import UserAccountModel
from backend.app.infrastructure.persistence.models.image_model import ImageModel
from backend.app.infrastructure.persistence.models.found_item_model import FoundItemModel
from backend.app.infrastructure.persistence.models.item_model import ItemModel

from backend.app.domain.entities.found_item import FoundItem
from backend.app.domain.value_objects.image import Image
from backend.app.domain.value_objects.localization import Localization
from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.entities.category import Category
from backend.app.domain.entities.building import Building
from backend.app.domain.entities.building_space import BuildingSpace


from typing import Generator


@pytest.fixture
def session() -> Generator[Session, None, None]:

    """Simula uma sessão a um banco em memória
    """

    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()

@pytest.fixture
def seed_data(session: Session) -> None:

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
        name="recepção",
        building_id=1
    )

    building_space3 = BuildingSpaceModel(
        id=3,
        name="coordenação",
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

    item = ItemModel(
        id=1,
        name="Lápis",
        description="Lápis preto faber castel",
        category_id=2,
        user_id=1,
    )

    found_item = FoundItemModel(
        id=1,
        found_space_id=1,
        left_space_id=2,
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
        item,
        found_item,
        image
    ])

    session.commit()

def test_create_found_item_success(session, seed_data):

    repo = FoundItemRepository(session)

    images = [
        Image(url="./image1.png"),
        Image(url="./image3.png")
    ]

    category = Category(
        id=1,
        name="Acessório Pessoal",
    )

    localization = Localization(
        cep="11111111",
        neighborhood="bairro 1",
        street="rua 1",
    )

    building = Building(
        id=1,
        name="predio 1",
        associated_localization=localization
    )

    building_space = BuildingSpace(
        id=1,
        name="sala 1",
        associated_building=building
    )

    user_account = UserAccount(
        id=1,
        name="teste",
        email="teste@email.com",
        password="1234",
        phone="1111"
    )

    lost_item = FoundItem(
        id=None,
        name="Carteira",
        description="Carteria Preta 20mm",
        images=images,
        category=category,
        associated_user_account=user_account,
        approx_found_building_space=building_space,
        approx_left_building_space=building_space,
    )

    repo.create_new_found_item(lost_item)

    item_result = session.query(ItemModel).filter(ItemModel.id == 2).first()
    found_item_result = session.query(FoundItemModel).filter(FoundItemModel.id == 2).first()
    images_result = session.query(ImageModel).filter(ImageModel.item_id == 2).all()

    assert item_result is not None
    assert found_item_result is not None
    assert found_item_result.id == 2
    assert len(images_result) == 2

def test_update_found_item_success(session, seed_data):

    repo = FoundItemRepository(session)

    localization = Localization(
        cep="11111111",
        neighborhood="bairro 1",
        street="rua 1",
    )

    building = Building(
        id=1,
        name="predio 1",
        associated_localization=localization
    )

    found_building_space = BuildingSpace(
        id=1,
        name="sala 1",
        associated_building=building
    )

    left_building_space = BuildingSpace(
        id=3,
        name="coordenação",
        associated_building=building
    )

    user_account = UserAccount(
        id=1,
        name="teste",
        email="teste@email.com",
        password="1234",
        phone="1111"
    )

    to_update_found_item = FoundItem(
        id=1,
        name="Chave",
        description="Chave prateada luz",
        images= [
            Image(url="./image3.png")
        ],
        category=Category(
            id=1,
            name="Acessório Pessoal"
        ),
        associated_user_account=user_account,
        approx_found_building_space=found_building_space,
        approx_left_building_space=left_building_space,
    )

    updated_found_item = repo.update_found_item(to_update_found_item, 1)

    assert updated_found_item.name == to_update_found_item.name
    assert updated_found_item.description == to_update_found_item.description
    assert updated_found_item.category.name == to_update_found_item.category.name
    assert updated_found_item.images[0].url == to_update_found_item.images[0].url
    assert updated_found_item.id == updated_found_item.id
    assert updated_found_item.associated_user_account.name == to_update_found_item.associated_user_account.name
    assert updated_found_item.approx_left_building_space.name == "coordenação"

def test_get_found_item_by_id_success(session, seed_data):

    repo = FoundItemRepository(session)

    found_item = repo.get_found_item_by_id(1)

    assert found_item is not None
    assert found_item.name == "Lápis"
    assert found_item.category.name == "Material"
    assert found_item.approx_found_building_space.name == "sala 1"
    assert found_item.approx_left_building_space.name == "recepção"

def test_delete_found_item_success(session, seed_data):

    repo = FoundItemRepository(session)

    is_row_deleted = repo.delete_found_item(1)

    assert is_row_deleted is True

def test_delete_found_item_id_not_exists(session, seed_data):

    repo = FoundItemRepository(session)

    is_row_deleted = repo.delete_found_item(3)

    assert is_row_deleted is False