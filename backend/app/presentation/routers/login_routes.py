from flask import request, jsonify, Flask
from dotenv import load_dotenv

import os

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.controllers.factories.login_factories import make_login_controller

from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder


def create_login_routes(app: Flask) -> None:

    """Registra as rotas de autenticação na aplicação Flask

    Parameters
    ----------
    app: Flask
        Objeto que atua como interface entre o cliente e servidor

    """

    load_dotenv()

    @app.route("/login", methods=["POST"])
    def login():

        database_url = DatabaseURLBuilder.build(
            os.environ["SGBD"],
            {
                "DATABASE": os.environ["DATABASE"],
            },
        )

        with SessionManager(database_url) as session_manager:

            http_request = HttpRequest(body=request.get_json())

            login_controller = make_login_controller(session_manager.session)

            http_response = login_controller.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
