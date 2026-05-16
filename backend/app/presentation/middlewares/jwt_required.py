from functools import wraps

import jwt
from flask import request, jsonify

from backend.app.infrastructure.security.jwt_decoder import JwtDecoder


def jwt_required(f):

    """Decorator que protege um endpoint Flask exigindo um token JWT válido no header Authorization

    O token deve ser enviado no formato: Authorization: Bearer <token>

    Parameters
    ----------
    f: function
        Função de view Flask a ser protegida

    Returns
    -------
    function
        Wrapper que valida o token antes de chamar a view

    """

    @wraps(f)
    def decorated(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):

            return jsonify(
                {
                    "message": "Token de autenticação não informado",
                    "code": "TOKEN_NOT_PROVIDED",
                }
            ), 401

        token = auth_header.split(" ")[1]

        try:
            payload = JwtDecoder.decode(token)
            request.user_payload = payload

        except jwt.ExpiredSignatureError:
            return jsonify(
                {
                    "message": "Token expirado",
                    "code": "EXPIRED_SIGNATURE_ERROR",
                }
            ), 401

        except jwt.InvalidTokenError:
            return jsonify(
                {
                    "message": "Token inválido",
                    "code": "INVALID_TOKEN_ERROR",
                }
            ), 401

        return f(*args, **kwargs)

    return decorated
