import os
import pytest

from backend.app.infrastructure.security.jwt_token_generator import JwtTokenGenerator
from backend.app.infrastructure.security.jwt_decoder import JwtDecoder


@pytest.fixture(autouse=True)
def set_jwt_secret(monkeypatch):

    """Define JWT_SECRET no ambiente para os testes"""

    monkeypatch.setenv("JWT_SECRET", "chave_secreta_de_teste_para_testes_unitarios")


def test_jwt_generate_returns_string():

    generator = JwtTokenGenerator()

    token = generator.generate({"user_id": 1, "email": "link@email.com"})

    assert isinstance(token, str)


def test_jwt_decode_returns_correct_payload():

    generator = JwtTokenGenerator()

    payload = {"user_id": 1, "email": "link@email.com"}

    token = generator.generate(payload)

    decoded = JwtDecoder.decode(token)

    assert decoded["user_id"] == 1
    assert decoded["email"] == "link@email.com"


def test_jwt_decode_raises_with_invalid_token():

    import jwt

    with pytest.raises(jwt.InvalidTokenError):

        JwtDecoder.decode("token_invalido")
