import jwt
import os
from datetime import timezone


class JwtDecoder:

    """Responsável pela decodificação e validação de tokens JWT"""

    @staticmethod
    def decode(token: str) -> dict:

        """Decodifica e valida um token JWT

        Parameters
        ----------
        token: str
            Token JWT a ser decodificado

        Returns
        -------
        dict
            Payload decodificado do token

        Raises
        ------
        jwt.ExpiredSignatureError
            Se o token estiver expirado

        jwt.InvalidTokenError
            Se o token for inválido ou malformado

        """

        secret = os.environ["JWT_SECRET"]

        return jwt.decode(token, secret, algorithms=["HS256"])
