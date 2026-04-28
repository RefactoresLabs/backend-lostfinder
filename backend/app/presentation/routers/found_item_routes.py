from flask import request, jsonify, Flask
from dotenv import load_dotenv

import os

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.controllers.factories.found_item_factories import make_create_found_item_controller
from backend.app.presentation.middlewares.jwt_required import jwt_required

from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder


def create_found_item_routes(app: Flask) -> None:

    """Registra as rotas de itens encontrados na aplicação Flask

    Parameters
    ----------
    app: Flask
        Objeto que atua como interface entre o cliente e servidor

    """

    load_dotenv()

    @app.route("/found-items", methods=["POST"])
    @jwt_required
    def create_found_item():

        database_url = DatabaseURLBuilder.build(
            os.environ["SGBD"],
            {
                "DATABASE": os.environ["DATABASE"],
            },
        )

        with SessionManager(database_url) as session_manager:

            http_request = HttpRequest(
                body=request.get_json(),
                params={"user_id": request.user_payload["user_id"]},
            )

            create_found_item_controller = make_create_found_item_controller(
                session_manager.session
            )

            http_response = create_found_item_controller.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
