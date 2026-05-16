import jwt
import os
from datetime import datetime, timedelta, timezone

from backend.app.application.interfaces.token_generator import TokenGenerator


class JwtTokenGenerator(TokenGenerator):

    """Implementação do TokenGenerator usando o algoritmo JWT (PyJWT)"""

    def generate(self, payload: dict) -> str:

        """Gera um token JWT assinado com a chave secreta da aplicação

        Parameters
        ----------
        payload: dict
            Dados a serem embutidos no token (ex: user_id, email)

        Returns
        -------
        str
            Token JWT codificado

        """

        expiration = datetime.now(tz=timezone.utc) + timedelta(hours=24)

        payload_with_exp = {**payload, "exp": expiration}

        secret = os.environ["JWT_SECRET"]

        token = jwt.encode(payload_with_exp, secret, algorithm="HS256")

        return token
