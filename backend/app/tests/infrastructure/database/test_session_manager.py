from backend.app.infrastructure.database.session_manager import SessionManager

import pytest

def test_session_was_created_during_context():

    database_url = "sqlite:///teste.db"

    with SessionManager(database_url) as session_manager:

        assert session_manager.session != None

def test_session_is_invalid_after_context():

    database_url = "sqlite:///teste.db"

    with SessionManager(database_url) as session_manager:

        session = session_manager.session
    
    with pytest.raises(Exception):

        session.execute("SELECT 1")