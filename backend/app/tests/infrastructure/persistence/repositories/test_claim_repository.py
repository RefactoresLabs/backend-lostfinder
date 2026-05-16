import pytest
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine


from backend.app.infrastructure.persistence.repositories.claim_repository import ClaimRepository

from backend.app.infrastructure.persistence.models.base import Base
from backend.app.infrastructure.persistence.models.image_model import ImageModel
from backend.app.infrastructure.persistence.models.category_model import CategoryModel
from backend.app.infrastructure.persistence.models.user_account_model import UserAccountModel
from backend.app.infrastructure.persistence.models.building_model import BuildingModel
from backend.app.infrastructure.persistence.models.building_space_model import BuildingSpaceModel
from backend.app.infrastructure.persistence.models.localization_model import LocalizationModel
from backend.app.infrastructure.persistence.models.item_model import ItemModel
from backend.app.infrastructure.persistence.models.found_item_model import FoundItemModel
from backend.app.infrastructure.persistence.models.claim_status_model import ClaimStatusModel
from backend.app.infrastructure.persistence.models.claim_model import ClaimModel

from backend.app.domain.entities.claim import Claim
from backend.app.domain.entities.found_item import FoundItem
from backend.app.domain.entities.user_account import UserAccount
from backend.app.domain.entities.category import Category
from backend.app.domain.entities.building_space import BuildingSpace
from backend.app.domain.entities.building import Building
from backend.app.domain.value_objects.image import Image
from backend.app.domain.value_objects.localization import Localization
from backend.app.domain.value_objects.claim_status import ClaimStatus

from typing import Generator

@pytest.fixture()
def session() -> Generator[Session, None, None]:

    """Simula uma sessão a um banco em memória
    """

    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    yield session

    session.close()

@pytest.fixture
def seed_data(session: Session) -> None:

    """Simula a criação de dados no banco em memória
    """

    localization_model=LocalizationModel(
        id=1,
        cep="1111",
        neighborhood="Bairro 1",
        street="Rua 1",
    )

    building_model = BuildingModel(
        id=1,
        name="Prédio 1",
        localization_id=1,
    )

    building_space_model = BuildingSpaceModel(
        id=1,
        name="Sala 1",
        building_id=1,
    )

    found_item_user_account_model = UserAccountModel(
        id=1,
        name="Link",
        email="link@email.com",
        password="1234",
        phone="12345678"
    )

    claimant_user_account_model = UserAccountModel(
        id=2,
        name="Mario",
        email="mario@email.com",
        password="1234",
        phone="12345678"
    )

    category_model = CategoryModel(
        id=1,
        name="Acessório Pessoal",
    )

    item_model = ItemModel(
        id=1,
        name="Carteira",
        description="Carteira preta",
        category_id=1,
        user_id=1,
    )

    item_model2 = ItemModel(
        id=2,
        name="Fone",
        description="Fone JBL branco",
        category_id=1,
        user_id=1,
    )

    found_item_model = FoundItemModel(
        id=1,
        found_space_id=1,
        left_space_id=1,
    )

    found_item_model2 = FoundItemModel(
        id=2,
        found_space_id=1,
        left_space_id=1,
    )

    image_model = ImageModel(
        id=1,
        url="/static/image1.png",
        item_id=1,
    )

    claim_status_model = ClaimStatusModel(
        id=1,
        name="Pendente",
    )

    claim_status_model2 = ClaimStatusModel(
        id=2,
        name="Aceito",
    )

    claim_model = ClaimModel(
        id=1,
        claimant_user_account_id=2,
        associated_found_item_id=1,
        status_id=1,
        retrieval_code="12A34B56C7",
    )

    session.add_all([
        localization_model,
        building_model,
        building_space_model,
        found_item_user_account_model,
        claimant_user_account_model,
        category_model,
        item_model,
        found_item_model,
        image_model,
        claim_status_model,
        claim_model,
        item_model2,
        found_item_model2,
        claim_status_model2,
    ])

    session.commit()

def test_create_claim_success(session, seed_data):

    localization = Localization(
        cep="1111",
        neighborhood="Bairro 1",
        street="Rua 1",
    )

    building = Building(
        id=1,
        name="Prédio 1",
        associated_localization=localization,
    )

    building_space = BuildingSpace(
        id=1,
        name="Sala 1",
        associated_building=building
    )

    found_item_user_account = UserAccount(
        id=1,
        name="Link",
        email="link@email.com",
        password="1234",
        phone="12345678",
    )

    category = Category(
        id=1,
        name="Acessório Pessoal"
    )

    found_item = FoundItem(
        id=2,
        name="Fone",
        description="Fone JBL branco",
        images=[],
        category=category,
        associated_user_account=found_item_user_account,
        approx_found_building_space=building_space,
        approx_left_building_space=building_space,
    )

    claimant_user_account = UserAccount(
        id=2,
        name="Mario",
        email="mario@email.com",
        password="1234",
        phone="12345678",
    )

    status = ClaimStatus(
        name="Pendente",
    )

    claim = Claim(
        id=None,
        created_at=None,
        claimant_user_account=claimant_user_account,
        associated_found_item=found_item,
        status=status
    )

    repo = ClaimRepository(session)

    new_claim = repo.create_new_claim(claim)

    assert new_claim.id == 2
    assert new_claim.created_at != None

def test_get_claim_by_id_success(session, seed_data):

    repo = ClaimRepository(session)

    claim = repo.get_claim_by_id(1)

    assert claim.id == 1
    assert claim.retrieval_code == "12A34B56C7"
    assert claim.status.name == "Pendente"
    assert claim.associated_found_item.associated_user_account.name == "Link"
    assert claim.claimant_user_account.name == "Mario"

def test_update_claim_success(session, seed_data):

    repo = ClaimRepository(session)

    status = ClaimStatus(
        name="Aceito",
    )

    updated_claim = repo.get_claim_by_id(1)

    claim = Claim(
        id=updated_claim.id,
        created_at=updated_claim.created_at,
        claimant_user_account=updated_claim.claimant_user_account,
        associated_found_item=updated_claim.associated_found_item,
        status=status
    )

    claim = repo.update_claim(claim, 1)

    assert claim.status.name == "Aceito"

def test_delete_claim_success(session, seed_data):

    repo = ClaimRepository(session)

    removed = repo.delete_claim(1)

    assert removed

def test_delete_claim_id_doesnt_exist(session, seed_data):

    repo = ClaimRepository(session)

    removed = repo.delete_claim(2)

    assert not removed

def test_check_retrieval_code_exists(session, seed_data):

    repo = ClaimRepository(session)

    exists = repo.check_retrieval_code_exists("12A34B56C7")

    assert exists
    
    
    

