from backend.app.infrastructure.persistence.repositories.building_repository import BuildingRepository

from backend.app.infrastructure.persistence.models.base import Base
from backend.app.infrastructure.persistence.models.building_model import BuildingModel
from backend.app.infrastructure.persistence.models.localization_model import LocalizationModel

import pytest

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine


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

    localization1 = LocalizationModel(
        id=1,
        cep="11111111",
        neighborhood="bairro 1",
        street="rua 1"
    )

    localization2 = LocalizationModel(
        id=2,
        cep="22222222",
        neighborhood="bairro 2",
        street="rua 2"
    )

    building1 = BuildingModel(
        id=1,
        name="predio 1",
        localization_id=1
    )

    building2 = BuildingModel(
        id=2,
        name="predio 2",
        localization_id=2
    )

    session.add_all([
        localization1,
        localization2,
        building1,
        building2
    ])

    session.commit()

def test_get_all_buildings_success(session, seed_data):

    repo = BuildingRepository(session)

    buildings = repo.get_all_buildings()

    assert len(buildings) == 2
    assert buildings[0].name == "predio 1"
    assert buildings[0].localization.street == "rua 1"
    assert buildings[1].name == "predio 2"
    assert buildings[1].localization.cep == "22222222"

def test_get_all_buildings_zero_elements(session):

    repo = BuildingRepository(session)

    buildings = repo.get_all_buildings()

    assert buildings == []

def test_get_building_by_id_success(session, seed_data):

    repo = BuildingRepository(session)

    building = repo.get_buildind_by_id(2)

    assert building.name == "predio 2"
    assert building.localization.cep == "22222222"

def test_get_building_by_id_when_id_not_exists(session, seed_data):

    repo = BuildingRepository(session)

    building = repo.get_buildind_by_id(3)

    assert building is None
