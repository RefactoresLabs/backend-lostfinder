from backend.app.infrastructure.persistence.repositories.building_space_repository import BuildingSpaceRepository

from backend.app.infrastructure.persistence.models.base import Base
from backend.app.infrastructure.persistence.models.building_space_model import BuildingSpaceModel
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

    building_space1 = BuildingSpaceModel(
        id=1,
        name="sala 1",
        building_id=1,
    )

    building_space2 = BuildingSpaceModel(
        id=2,
        name="sala 2",
        building_id=2,
    )

    building_space3 = BuildingSpaceModel(
        id=3,
        name="sala 3",
        building_id=2,
    )

    session.add_all([
        localization1,
        localization2,
        building1,
        building2,
        building_space1,
        building_space2,
        building_space3,
    ])

    session.commit()

def test_get_building_space_by_id_success(session, seed_data):

    repo = BuildingSpaceRepository(session)

    building_space = repo.get_building_space_by_id(2)

    assert building_space.name == "sala 2"
    assert building_space.associated_building.name == "predio 2"
    assert building_space.associated_building.localization.street == "rua 2"

def test_get_building_space_by_id_when_id_not_exists(session, seed_data):

    repo = BuildingSpaceRepository(session)

    building_space = repo.get_building_space_by_id(4)

    assert building_space is None

def test_get_building_spaces_by_building_id_success(session, seed_data):

    repo = BuildingSpaceRepository(session)

    building_spaces = repo.get_building_spaces_by_building_id(2)

    assert len(building_spaces) == 2
    assert building_spaces[0].name == "sala 2"
    assert building_spaces[0].associated_building.localization.cep == "22222222"
    assert building_spaces[1].name == "sala 3"
    assert building_spaces[1].associated_building.localization.cep == "22222222"

def test_get_building_spaces_by_building_id_when_building_id_not_exists(session, seed_data):

    repo = BuildingSpaceRepository(session)

    building_spaces = repo.get_building_spaces_by_building_id(3)

    assert building_spaces == []
