from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder
import pytest


def test_build_sqlite_memory_success():

    assert DatabaseURLBuilder.build("sqlite", {}) == "sqlite:///:memory:"

def test_build_sqlite_file_success():

    assert DatabaseURLBuilder.build("sqlite", {"DATABASE": "teste"}) == "sqlite:///teste"

def test_build_sqlite_file_value_error():

    with pytest.raises(TypeError):

        _ = DatabaseURLBuilder.build("sqlite", {"DATABASE": 4}) == "sqlite:///teste"

def test_build_postgresql_success():

    data = {
        "DATABASE": "teste",
        "USERNAME": "admin",
        "PASSWORD": "1234",
        "HOSTNAME": "localhost",
        "PORT": "3306",
    }

    assert DatabaseURLBuilder.build("postgresql", data) == "postgresql://admin:1234@localhost:3306/teste"

def test_build_postgresql_wrong_username_type():

    data = {
        "DATABASE": "teste",
        "PASSWORD": "1234",
        "HOSTNAME": "localhost",
        "PORT": "3306",
        "USERNAME": 4
    }

    with pytest.raises(TypeError):

        _ = DatabaseURLBuilder.build("postgresql", data)

def test_build_postgresql_username_key_missing():

    data = {
        "DATABASE": "teste",
        "PASSWORD": "1234",
        "HOSTNAME": "localhost",
        "PORT": "3306",
    }

    with pytest.raises(KeyError):

        _ = DatabaseURLBuilder.build("postgresql", data)