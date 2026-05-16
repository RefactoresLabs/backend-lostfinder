from backend.app.infrastructure.persistence.repositories.category_repository import CategoryRepository

from backend.app.infrastructure.persistence.models.base import Base
from backend.app.infrastructure.persistence.models.category_model import CategoryModel

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

    category1 = CategoryModel(
        id=1,
        name="Acessório Pessoal",
    )

    category2 = CategoryModel(
        id=2,
        name="Documento",
    )

    category3 = CategoryModel(
        id=3,
        name="Material escolar",
    )

    session.add_all(
        [
            category1,
            category2,
            category3,
        ]
    )

    session.commit()

def test_get_all_categories_success(session, seed_data):

    repo = CategoryRepository(session)

    categories = repo.get_all_categories()

    assert len(categories) == 3
    assert categories[0].name == "Acessório Pessoal"
    assert categories[2].name == "Material escolar"

def test_get_all_categories_zero_elements(session):

    repo = CategoryRepository(session)

    categories = repo.get_all_categories()

    assert categories == []

def test_get_category_by_id_success(session, seed_data):

    repo = CategoryRepository(session)

    category = repo.get_category_by_id(2)

    assert category.name == "Documento"

def test_get_category_by_id_when_id_not_exists(session, seed_data):

    repo = CategoryRepository(session)

    category = repo.get_category_by_id(4)

    assert category is None
